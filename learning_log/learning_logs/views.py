from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.


def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''shows all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html' ,context)

def topic(request, topic_id):
    '''shows all topics'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'learning_logs/topic.html' ,context)

def new_topic(request):
    '''add a new topic'''
    if request.method != 'POST':
        #if no data is submitted present a blank form
        form = TopicForm()
    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        #post data submitted, process submitted data
    context = {'form' :form}        

    return render(request,'learning_logs/new_topic.html', context)   