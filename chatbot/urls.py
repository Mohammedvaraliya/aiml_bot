from django.urls import path
from . import views


urlpatterns = [
    path('', views.aiml_bot_response, name='home'),
]
