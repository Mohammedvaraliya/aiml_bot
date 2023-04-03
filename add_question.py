from chatbot.models import Question, Category

questions = [
    'Who is the founder of college',
    'Who is the trustee of college',
    'who is the director of college',
    'who is the principal of college',
    'who is the admin of college',
    'who is the accountant of college',
    'who is the coordinator of cs department',
    'who is th coordinator of IT department',
    'who is the coordinator of Biotech department',
    'who is the coordinator of BAMMC department',
    'name the faculty members of cs department',
    'name the faculty member of IT department',
    'name the faculty member of Biotech department',
    'name the faculty member of BAMMC department',
    'who is the clerk of the college',
    'who is the head of cultural commitee',
    'who is the cricket coach of college',
    'wo is the football coach of college',
    'who is librarian of college',
    'who is the incharge of sports room',
    'who is the head of cleaning staff',
    'who is the head of security'
]

for question in questions:
    category = Category.objects.create(name='staffs')
    Question.objects.create(text=question, category=category)