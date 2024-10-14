from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import LoginForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            user = authenticate(username = cd['username'], 
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('User has been deactivated')
        return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})