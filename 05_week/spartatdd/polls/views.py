from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    #output = ', '.join([q.question_text for q in question_list])
    context = {
        'question_list': question_list
    }
    #return HttpResponse(output)
    return render(request, 'polls/index.html', context)