from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .aiml_bot import AIMLBot

aiml_bot = AIMLBot()

@csrf_exempt
def aiml_bot_response(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        response = aiml_bot.respond(input_text)
        return HttpResponse(response)
    else:
        return render(request, 'home.html')
