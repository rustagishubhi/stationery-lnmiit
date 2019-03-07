from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #if request.user.is_active:
    #    return HttpResponseRedirect(reverse('signin'))

    return render(request,'faculty/index.html')
