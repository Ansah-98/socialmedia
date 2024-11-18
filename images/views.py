from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.contrib import messages

# Create your views here.


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageForm(data = request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            new_image  = form.save(commit= False)
            new_image.user = request.user
            new_image.save()
            messages.success(request,'The image has been successfully saved')
            
            return redirect(new_image.get_absolute_url())
        
    form  = ImageForm(data = request.GET)
    return render(request,'images/image/create.html',{'section':'images','form':form})