
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# Create your views here.

def inner(request):
    return render(request, 'alerts/inner_2.html')

def alert_two(request):
    return render(request, 'alerts/alert_two.html')

def next(request):
    return render(request, 'alerts/next.html')

def over(request):
    return render(request, 'alerts/over.html')
#def index(request):
    #template = loader.get_template('login/alert_two_next.html')
#return render(request, 'alerts/alert_two_next.html')
    #username = Accounts.objects.only('user_name')[0]
#return HttpResponse("Welcome to hotOrnot. You're at the login page, %s." % username)

#def detail(request, user_name):
#user_name = Accounts.objects
#return HttpResponse("Hi %s!" % user_name)

