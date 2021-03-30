from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.


def index(request):
    my_dict = {'home_page': "Home Page"}
    return render(request, "AppTwo/index.html", context=my_dict)


def help(request):
    my_dict2 = {'help_page': "Help Page"}
    return render(request, "AppTwo/help.html", context=my_dict2)

def users(request):
    users_list = User.objects.order_by('last_name')
    my_dict3 = {'users_page': users_list}
    return render(request, "AppTwo/users.html", context=my_dict3)
