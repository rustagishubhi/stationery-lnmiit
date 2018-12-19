from django.shortcuts import render
from login.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from faculty.models import FacultyProfileInfo

# Create your views here.
def signin(request):
    dictionery = dict()
    if request.user.is_active:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")

        else:
            dictionery['error'] = True

    else:
        pass

    return render(request,'signin/index.html', context = dictionery)

@login_required
def user_logout(required):
    logout(request)
    return HttpResponseRedirect(reverse('signin:index'))
