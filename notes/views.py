import json
import markdown
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from notes.utils import profile_from_request
from notes.models import Notebook, Color, Note
from notes.forms import NotebookForm, NoteForm
from accounts.models import UserProfile

# Create your views here.
def index(request):
    # Overview of the notebooks, if a user is logged in.
    # Otherwise, some welcome page
    profile = profile_from_request(request)
    notebooks = Notebook.objects.filter(owner=profile).order_by('title')

    return render(
        request, 'notes/index.html', {
            'profile': profile,
            'notebooks': notebooks
        }
    )

def notebook(request, pk):
    # Page view for a specific notebook
    # Bulk of functionality goes here
    notebook = Notebook.objects.get(pk=pk)
    notes = Note.objects.filter(notebook=notebook).order_by('x_pos')
    profile = profile_from_request(request)
    form = NoteForm()

    # Get list of collaborators + owner of notebook
    # Check if current user is in list
    # Give permissions error if not allowed
    if (notebook.owner == profile) | (profile in notebook.collaborators.all()):
        return render(
            request, 'notes/notebook.html',
            {
                'notebook': notebook,
                'profile': profile,
                'form': form,
                'notes': notes,
            }
        )
    else:
        raise PermissionDenied("That's not your notebook! The owner of this notebook needs to give you permission in order to join it.")


@login_required
def add_notebook(request):
    profile = profile_from_request(request)

    if request.method == 'POST':
        notebook_form = NotebookForm(request.POST)
        collab_emails = request.POST.get('collaborators').replace(' ', '').split(',')
        print collab_emails
        collabs = UserProfile.objects.filter(user__email=collab_emails)
        print collabs
        notebook_form.collaborators = collabs
        if notebook_form.is_valid():
            notebook = notebook_form.save(commit=False)
            notebook.owner = profile_from_request(request)
            notebook = notebook.save()
            messages.success(request, "Notebook added.")
            return HttpResponseRedirect(reverse("notes:index"))
    else:  # GET
        notebook_form = NotebookForm()

    return render(
        request, 'notes/add_notebook.html',
        {
            'profile': profile,
            'notebook_form': notebook_form,
        }
    )

def get_notes(request):
    if request.method == 'GET':
        notebook_id = request.GET.get('notebook')
        notes_json = []
        notes = Note.objects.filter(notebook=notebook_id)
        for note in notes:
            notes_json.append({
                'id': note.id,
                'x': note.x_pos,
                'y': note.y_pos,
                'width': note.width,
                'height': note.height,
                'content_html': markdown.markdown(note.content),
                'color': note.color.hex,
                'text_color': note.color.text_color
            })
        return JsonResponse(json.dumps(notes_json), safe=False)


def add_note(request):
    # Add a new note to the notebook
    if request.method == 'POST':
        response_data = {}
        note = Note(
            notebook=Notebook.objects.get(pk=request.POST.get('notebook')),
            #x_pos=request.POST.get('x'),
            x_pos=0,
            y_pos=0,
            width=2,
            height=3,
            #y_pos=request.POST.get('y'),
            #width=request.POST.get('width'),
            #height=request.POST.get('height'),
            color=Color.objects.get(pk=request.POST.get('color')),
            content=request.POST.get('content_raw')
        )
        note.save()
        response_data['x'] = note.x_pos
        response_data['y'] = note.y_pos
        response_data['width'] = note.width
        response_data['height'] = note.height
        response_data['id'] = note.pk
        response_data['color'] = note.color.hex
        response_data['text_color'] = note.color.text_color
        response_data['content_html'] = note.content

        return JsonResponse(response_data)

def move_notes(request):
    # Update positions of notes when dragged/resized
    if request.method == 'POST':
        notes_tmp = request.POST.get('coords')
        notes = json.loads(notes_tmp)
        for n in notes:
            note = Note.objects.get(pk=n['id'])
            note.x_pos = n['x']
            note.y_pos = n['y']
            note.width = n['width']
            note.height = n['height']
            note.save()
        return JsonResponse({"Hi": "mom"})

def edit_note(request):
    # Edit an existing note in the notebook
    if request.method == 'POST':
        response_data = {}
        note = Note.objects.get(pk=request.POST.get('id'))
        note.x_pos = request.POST.get('x')
        note.y_pos = request.POST.get('y')
        note.width = request.POST.get('width')
        note.height = request.POST.get('height')
        note.color = Color.objects.get(pk=request.POST.get('color'))
        note.content = request.POST.get('content_raw')
        note.save()
        response_data['x'] = note.x_pos
        response_data['y'] = note.y_pos
        response_data['width'] = note.width
        response_data['height'] = note.height
        response_data['id'] = note.pk
        response_data['color'] = note.color.hex
        response_data['text_color'] = note.color.text_color
        response_data['content_html'] = note.content

        return JsonResponse(response_data)
