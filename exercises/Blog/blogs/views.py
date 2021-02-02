from django.shortcuts import render
from .models import Blogpost

# Create your views here.

def index_view(request):
    posts = Blogpost.objects.order_by('date')
    context={'posts' : posts}

    return render(request, 'blogs/index.html', context)