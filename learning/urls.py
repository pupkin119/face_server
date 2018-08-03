from django.urls import path

from . import views

app_name = 'learning'
urlpatterns = [
    path('startlearning/', views.statrtLearning, name = 'startLearning'),
]
