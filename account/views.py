from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import LoginForm
from django.contrib.auth import login, authenticate 


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            user = authenticate(username = cd.username, 
                                password = cd.password)
            if user is not None:
                if user.is_active:
                    login(user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('User has been deactivated')
        return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,'account/login',{'form':form})