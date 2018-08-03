from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    # path('', views.Index)
    path('', views.addNewId),
    path('<uuid:client_id>/edit/', views.editId, name='editId'),
    path('<uuid:client_id>/', views.deleteId, name='delete'),
    # path('authentication/', views.authentication),
]
