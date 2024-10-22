from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile
# Create your views here.
from .forms import LoginForm
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForms,UserEdit,ProfileEdit
from django.contrib import messages


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
                    return redirect(dashboard)
                else:
                    return HttpResponse('User has been deactivated')
        return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def register(request):
    if request.method =='POST':
        user_form = UserCreationForms(request.post)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user  = new_user
            Profile.objects.create(user = user)

            return render('account/register_done.html',{'user':user})
    user_form = UserCreationForms()
    return render(request,'account/register.html',{'form':user_form})

@login_required
def logout_user(request):
    logout(request)
    return redirect(login_user)


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})
@login_required
def edit(request):
    if request.method =='POST':
        user_form = UserEdit(instance=request.user,
                             data=request.POST)
        profile_form = ProfileEdit(instance = request.user.profile,
                               data  = request.POST,
                               files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile has been updated successfully')
        else:
            messages.error(request,'Error updating your profile')
    else:
        user_form = UserEdit(instance = request.user)
        profile_form = ProfileEdit(instance = request.user.profile)
        
    return render(request,'account/edit.html',{'user_form':user_form,
                                                      'profile_form':profile_form})