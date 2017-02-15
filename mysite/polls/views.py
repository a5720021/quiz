from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse ,Http404
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)  

def add_q(request):
    q_new = request.POST.get('q_add', False)
    if q_new != False:
       q = Question(question_text=q_new,pub_date=timezone.now())
       q.save()
    return render(request, 'polls/add_q.html') 

def add_c(request):
    context = {'question': Question.objects.all()}
    c_new = request.POST.get('c_add', False)
    if c_new != False:
       q_id = request.POST.get('q_num', False)
       q = Question.objects.get(pk=q_id)
       q.choice_set.create(choice_text=c_new,votes=0)
    return render(request, 'polls/add_c.html',context)

def viewall(request,question_id):
    context = {'question': Question.objects.all()}
    return render(request, 'polls/viewall.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
