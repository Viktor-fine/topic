""" Определяет схемы URL для learning_logs """
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]