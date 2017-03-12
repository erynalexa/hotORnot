
from django.http import HttpResponse

from .models import Accounts

# Create your views here.
def index(request):
    username = Accounts.objects.only('user_name')[0]
    
    return HttpResponse("Welcome to hotOrnot. You're at the login page, %s." % username)

def detail(request, user_name):
    user_name = Accounts.objects
    return HttpResponse("Hi %s!" % user_name)

