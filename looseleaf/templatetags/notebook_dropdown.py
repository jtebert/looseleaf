from django import template
from notes.models import Notebook
from notes.utils import profile_from_request

register = template.Library()

@register.inclusion_tag('notes/notebook_dropdown.html', takes_context=True)
def notebook_dropdown(context, current_page):
    profile = profile_from_request(context['request'])
    menuitems = Notebook.objects.filter(owner=profile).order_by('title')
    return {
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }