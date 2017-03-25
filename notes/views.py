from django.shortcuts import render
from django.http import HttpResponse
from utils import profile_from_request

# Create your views here.
def index(request):
    profile = profile_from_request(request)

    return render(
        request, 'notes/index.html', {
            'profile': profile
        }
    )