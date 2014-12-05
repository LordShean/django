from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Choice


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

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})