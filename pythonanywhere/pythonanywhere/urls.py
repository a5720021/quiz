from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^quiz/', include('quiz.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
