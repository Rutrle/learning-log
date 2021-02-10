from django.shortcuts import render,redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''shows all topics'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html' ,context)

@login_required
def topic(request, topic_id):
    '''shows all topics'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    check_topic_owner(topic, request)
    return render(request,'learning_logs/topic.html' ,context)

@login_required
def new_topic(request):
    '''add a new topic'''
    if request.method != 'POST':
        #if no data is submitted present a blank form
        form = TopicForm()
    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        #post data submitted, process submitted data
    context = {'form' :form}        

    return render(request,'learning_logs/new_topic.html', context)   

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    # display blank or invalid form
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html',context)   

@login_required
def edit_entry(request, entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    check_topic_owner(topic, request)


    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    # display blank or invalid form
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html',context) 


def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404