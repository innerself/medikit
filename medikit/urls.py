from django.urls import path, include

from . import views

app_name = 'medikit'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('edit/kits/', views.edit_kits, name='edit_kits'),
    path('edit/kits/<int:kit_id>/', views.edit_kit, name='edit_kit'),
    path('edit/medications/', views.edit_medications, name='edit_medications'),
    path('remove/kit/<int:kit_id>/', views.remove_kit, name='remove_kit'),
    path('remove/medication/<int:medication_id>/', views.remove_medication, name='remove_medication'),
    path('edit/<str:item_type>/<int:item_id>/', views.edit_one, name='edit_one'),
]
