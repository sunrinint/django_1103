from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from django.template import loader


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    return render(request, 'polls/index.html')


# def index(request):
#    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {'latest_question_list': latest_question_list}
#    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# def detail(request, question_id):
#   try:
#        question = Question.objects.get(pk = question_id)
#   except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#   return render(request, 'polls/detail.html', {'question' : question})


# def detail(request, question_id):
#     return HttpResponse("Hello, world. You're looking at question %s." % question_id)


# def results(request, question_id):
#    return HttpResponse("Hello, world. You're looking at results of question %s." % question_id)

def results(request, question_i):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', question) # 안끝남

# def vote(request, question_id):
#     return HttpResponse("Hello, world. You're voting on question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice."
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=question_id))
