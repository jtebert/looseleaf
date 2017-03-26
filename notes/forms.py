from django import forms
from models import Notebook, Color, Note
from django.forms.widgets import mark_safe


class ColorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return mark_safe('<div class="color-sample" style="background-color:#{}"></div> {}'.format(obj.hex, obj.name))


class NotebookForm(forms.ModelForm):
    color = ColorModelChoiceField(widget=forms.RadioSelect,
                                  queryset=Color.objects.order_by('hex'),
                                  required=True,
                                  empty_label=None)

    class Meta:
        model = Notebook
        fields = ('collaborators', 'title', 'color')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Title"}),
            #'collaborators': forms.TextInput(attrs={'placeholder': "Separate emails with commas"})
        }


class NoteForm(forms.ModelForm):
    color = ColorModelChoiceField(widget=forms.RadioSelect,
                                  queryset=Color.objects.all(),
                                  required=True,
                                  empty_label=None)

    class Meta:
        model = Note
        fields = ('content', 'color')
        widgets = {
            'content': forms.Textarea(attrs={'placehold': 'Write your note here'})
        }
