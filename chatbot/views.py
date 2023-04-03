from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .aiml_bot import AIMLBot
from datetime import datetime
from .models import Question


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
    
class QuestionView(View):
    template_name = 'questions.html'
    context_object_name = 'questions'

    def get(self, request, *args, **kwargs):
        locations = Question.objects.filter(category__name='locations')
        staff = Question.objects.filter(category__name='staffs')
        history = Question.objects.filter(category__name='histories')
        course = Question.objects.filter(category__name='courses')
        sport = Question.objects.filter(category__name='sports')
        other = Question.objects.filter(category__name='others')
        context = {
            'locations': locations,
            'staffs': staff,
            'histories': history,
            'courses': course,
            'sports': sport,
            'others': other,
        }
        return render(request, self.template_name, context)
