from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserRegisterationForm
from django.contrib import messages
from .models import Passwords
from django.views.generic import ListView, CreateView, DetailView




def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.changed_data('username')
            # messages.success(f'{username} successfully registered')
            return redirect("home")
    
    else:
        form = UserRegisterationForm()
    return render(request, 'main/register.html', {'form':form})


# def passwords(request):
    
#     passwords = Passwords.objects.all().order_by('-pk')
#     return render(request, 'main/passwords.html', {'passwords':passwords})

class displayPasswords(ListView):
    model = Passwords
    template_name = 'main/passwords.html'


# def newpassword(request):
#     if request.method == "POST":
#         form = PasswordCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect('passwords')     
#     else:
#         form = PasswordCreationForm()
#     return render(request, 'main/newpassword.html' ,{'form':form})

class createPassword(CreateView):
    template_name = 'main/newpassword.html'
    model = Passwords
    fields = ["app_name", "password"]

def singlePasswordView(request,id):
    password = Passwords.objects.get(id = id)
    return render(request, "main/single-password.html", {'password':password})

# class singlePasswordView(DetailView):
#     model = Passwords
#     template_name = 'main/single-password.html'
#     context_object_name = "password"


