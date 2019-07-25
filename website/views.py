from django.shortcuts import render
from website.models import Pessoa

# Create your views here.
def index(request):
    args = {

    }
    return render(request, 'index.html', args)

def sobre(request):
    args = {

    }
    return render(request, 'sobre.html', args)