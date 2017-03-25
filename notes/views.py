from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from notes.utils import profile_from_request
from notes.models import Notebook
from notes.forms import NotebookForm

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
    # TODO: restrict access based on collaborators
    notebook = Notebook.objects.get(pk=pk)
    profile = profile_from_request(request)

    # Get list of collaborators + owner of notebook
    # Check if current user is in list
    # Give permissions error if not allowed
    if (notebook.owner == profile) | (profile in notebook.collaborators.all()):
        return render(
            request, 'notes/notebook.html',
            {
                'notebook': notebook,
                'profile': profile,
            }
        )
    else:
        raise PermissionDenied("That's not your notebook! The owner of this notebook needs to give you permission in order to join it.")


def add_notebook(request):
    profile = profile_from_request(request)

    if request.method == 'POST':
        notebook_form = NotebookForm(request.POST)
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
