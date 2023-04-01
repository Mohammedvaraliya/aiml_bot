from django.urls import path
from .views import AIMLBotView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bot/', AIMLBotView.as_view(), name='bot'),
]
