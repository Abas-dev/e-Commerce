# for the login, logout and register views , i will be using class based views. 
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPage(LoginView):
    template_name = 'login.html'
    
    def post(self, request, *args, **kwargs):
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have logged into your account')
            return redirect('shop:homePage')
        else:
            messages.error(request,'cant login, check username or password')
            return redirect('auth:login')

class RegisterPage(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        email = self.request.POST['email']
        firstName = self.request.POST['firstname']
        lastName = self.request.POST['lastname']
        password = self.request.POST['password']
        passwordConf = self.request.POST['passwordConf']
        if password != passwordConf:
            messages.error(request, 'password do not match')
            return redirect('auth:register')
        else:
            user = User.objects.create_user(username=email,email=email,first_name = firstName, last_name = lastName, password = password)
            user.save()
            messages.success(request, 'your account has been created successfully')
            return redirect('auth:login')

class LogoutView(LoginRequiredMixin,LogoutView):
    next_page = 'auth:login'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have successfully logged out.")
        return super(LogoutView, self).dispatch(request, *args, **kwargs)