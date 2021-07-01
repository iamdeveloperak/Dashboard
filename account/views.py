from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'dashboard.html', context)
        else:
            return redirect('/login/')


class LoginViewUser(LoginView):
    template_name = "sign-in.html"

class SignupViewUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'sign-up.html'
    success_url = '/signin/'


@login_required
def logout_view(request):
    logout(request)
    return redirect("/signin/")