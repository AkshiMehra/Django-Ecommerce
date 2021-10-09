from django.shortcuts import render, redirect
from .forms import register_form

# Create your views here.

def register(request):
    if(request.method == "POST"):
        form = register_form(request.POST)
        if form.is_valid:
            form.save()

            return redirect('login')
    else:
        form = register_form()
    
    return render(request, 'users/register.html',{'form':form,})
