from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

def login_page(request):
    """Allow users to login to an account."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nom utilisateur ou mot de passe incorrect')
    context = {}
    return render(request, 'user/login_page.html', context)

def logoutUser(request):
    """Allow users to logout of an account."""
    logout(request)
    return redirect('home')

def register_page(request):
    """Allow users to create an account."""
    form = UserCreationForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte à été créé pour' + user)
    context = {'form': form}
    return render(request, 'user/register_page.html', context)
