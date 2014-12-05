from django.http import HttpResponse      #Iteration 1a 1b
#from django.template import RequestContext, loader     #Iteration 2
from django.shortcuts import render     #Iteration 3
#from django.http import Http404     #404 Manager
from django.shortcuts import get_object_or_404    #404 management 2
from polls.models import Question


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")    #Iteration 1a

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #output = ', '.join([p.question_text for p in latest_question_list])    #Iteration 1b
    #return HttpResponse(output)

    #template = loader.get_template('polls/index.html')     Iteration 2
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))

    context = {'latest_question_list': latest_question_list}    #Iteration 3
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)    #iteration 1

    #try:                                                   #404 management 1
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404
    #return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)    #404 management 2
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)