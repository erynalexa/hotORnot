
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import HeatExhaustion
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def inner(request):
    latest_in = HeatExhaustion.objects.latest('date')
    context = {'latest_in': latest_in}
    return render(request, 'alerts/inner_2.html', context)

@xframe_options_exempt
def alert_two(request):
    return render(request, 'alerts/alert_two.html')

@xframe_options_exempt
def next(request):
    return render(request, 'alerts/next.html')

@xframe_options_exempt
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

