from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .aiml_bot import AIMLBot
from datetime import datetime


aiml_bot = AIMLBot()

# Create your views here.
def home(request):
    return render(request, 'home.html')


class AIMLBotView(View):
    def get(self, request):
        now = datetime.now()
        if now.hour < 12:
            greeting = "Good morning"
        elif now.hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        context = {
            'greeting': greeting
        }
        return render(request, 'chat_bot.html', context)
        

    @csrf_exempt
    def post(self, request):
        input_text = request.POST.get('input_text', '')
        response = aiml_bot.respond(input_text)
        return HttpResponse(response)
