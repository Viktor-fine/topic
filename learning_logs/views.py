from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
    """ Главная страница приложения """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Выводит список тем """
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Выводит одну тему и все её записи. """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Добовляет новую тему """
    if request.method != 'POST':
        # Данные не отправились, а создаётся пустая форма
        form = TopicForm()
    else:
        #Отправленны данные POST, ещё проверить введённые данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #Вывести пустую или не действительную форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context) 

def new_entry(request, topic_id):
    """Добавляет запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Данные не отправились, создаётся пустая форма
        form = EntryForm()
    else:
        # Отправленные данные POST, обработать данные
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

        #Вывести пустую или недействительную форму
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context) 
