from chatbot.models import Question, Category

questions = [
    'What are the timings available for parents to meet',
    'What are the committees present in the college',
    'Is there a gym',
    'What payment methods available',
    'what is the website of college',
    'what dish is available in Canteen',
    'what is the average price of canteen dish',
    'Does vadapao is avalable in canteen',
    'What various activities held in the college',
    'Who is the student head of the promotion committee',
    'What is the fine for not wearing an ID card',
    'what are various food stalls present outside college'
]

for question in questions:
    category = Category.objects.create(name='others')
    Question.objects.create(text=question, category=category)