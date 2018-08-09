from django.urls import path

from . import views

app_name = 'getmodel'
urlpatterns = [
    path('', views.getModel),
]