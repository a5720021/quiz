from django.conf.urls import url
from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^answer/$', views.answer, name='answer'),
    url(r'^result/$', views.result, name='result'),
    url(r'^quizanswer/$', views.quizanswer, name='quizanswer'),
    url(r'^ranking/$', views.ranking, name='ranking')
]

