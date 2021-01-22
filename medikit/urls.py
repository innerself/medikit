from django.urls import path

from . import views

app_name = 'medikit'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:item>', views.items_add, name='items_add'),
]
