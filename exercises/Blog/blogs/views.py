from django.shortcuts import render, redirect
from .models import Blogpost
from .forms import CreateForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index_view(request):
    posts = Blogpost.objects.order_by('date')
    context={'posts' : posts}

    return render(request, 'blogs/index.html', context)

@login_required
def create_view(request):
    if request.method != 'POST':
        form=CreateForm()
    else:
        form=CreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context= {'form':form}

    return render(request, 'blogs/new_post.html',context) 

@login_required
def edit_view(request, blog_id):
    blogpost = Blogpost.objects.get(id=blog_id)


    if request.method != 'POST':
        form=CreateForm(instance=blogpost)
    else:
        form=CreateForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context= {'blogpost':blogpost,'form':form}        


    return render(request, 'blogs/edit_post.html',context)                    