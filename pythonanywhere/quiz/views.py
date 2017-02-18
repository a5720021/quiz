from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse ,Http404
from django.urls import reverse
from .models import Choice, Question ,User_answer

def index(request):
    return render(request, 'quiz/index.html')

def answer(request):
    context = {'question': Question.objects.all()}
    return render(request, 'quiz/answer.html',context)

def result(request):
    choice_all = Choice.objects.count()
    question_all = Question.objects.count()
    score = 0
    for i in range(1,choice_all):
    	checkans = str(request.POST.get(str(i),False))
        if checkans == 'True':
            score += 1
    user_name = request.POST.get('uname',False)
    u = User_answer(user_name=user_name,score=score)
    u.save()
    context = {'score':score,'question':question_all,'uname':user_name}
    return render(request, 'quiz/result.html',context)

def quizanswer(request):
    context = {'question': Question.objects.all()}
    return render(request, 'quiz/quizanswer.html',context)

def ranking(request):
    topscore_list = User_answer.objects.order_by('-score')[:20]
    context = {'user': topscore_list}
    return render(request, 'quiz/ranking.html',context)

