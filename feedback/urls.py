from django.urls import path
from . import views


urlpatterns = [
    path('error', views.error, name='error'),
    path('question', views.question, name='question'),
    path('idea', views.idea, name='idea'),
]