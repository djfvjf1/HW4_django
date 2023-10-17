from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ProblemForm
from .models import Problem


def prehome(request):
    return render(request, "prehome/prehome.html", {"prehome": prehome})


def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'create_problem.html', {'form': form})
    

def problem_list(request):
    if not request.user.is_authenticated:
        problems = Problem.objects.filter(resolved='not resolved')
    else:
        problems = Problem.objects.all()
    
    return render(request, 'problem_list.html', {'problems': problems})

def profile_view(request):
    return render(request, 'login\profile.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('problem_list')
        else:
            return render(request, 'login\login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login\login.html')

def logout_view(request):
    logout(request)
    return redirect('prehome')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login\signup.html'