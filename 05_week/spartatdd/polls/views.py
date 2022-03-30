from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    #output = ', '.join([q.question_text for q in question_list])
    context = {
        'question_list': question_list
    }
    #return HttpResponse(output)
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    return render(request, 'polls/detail.html', {'question': question})