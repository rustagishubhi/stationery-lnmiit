from django.shortcuts import render
from login.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from StationaryAPI.models import Faculty

# Create your views here.
def signin(request):
    dictionery = dict()
    if request.user.is_active:
        return HttpResponseRedirect(reverse('faculty'))
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

def signup(request):
    dictionery = dict()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            try:
                validate_password(user.password)
            except:
                dictionery['error'] = "Password Entered Is Too Week To Be Accepted."
                dictionery['user_form'] = UserForm()
                dictionery['profile_form'] = UserProfileInfoForm()
                return render(request,'signin/signup.html',context=dictionery)
            if User.objects.filter(email__iexact=user.email):
                dictionery['error'] = "Please Select A New E-Mail. This E-Mail is already In Use."
                dictionery['user_form'] = UserForm()
                dictionery['profile_form'] = UserProfileInfoForm()
                return render(request,'signin/signup.html',context=dictionery)
            else:
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return HttpResponseRedirect(reverse('login:signin'))
        else:
            dictionery['error'] = "Please Select A New User Name. This User Name is already In Use."
            dictionery['user_form'] = UserForm()
            dictionery['profile_form'] = UserProfileInfoForm()
    else:
        dictionery['user_form'] = UserForm()
        dictionery['profile_form'] = UserProfileInfoForm()

    return render(request,'signin/signup.html',context=dictionery)

@login_required
def user_logout(required):
    logout(request)
    return HttpResponseRedirect(reverse('login:signin'))
