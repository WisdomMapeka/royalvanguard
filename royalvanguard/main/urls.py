from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name="index"),
    path('about/' , views.about, name="about"),
    path('services/' , views.services, name="services"),
    path('projects/' , views.projects, name="projects"),
    path('contacts/' , views.contacts, name="contacts"),
    path('thanks/', views.sending_message_form_success, name='sending_message_form_success'),
]
