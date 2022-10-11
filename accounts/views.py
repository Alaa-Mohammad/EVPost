from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('logout'))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect(reverse('all_posts'))
    else:
        form = RegistrationForm()
    context = {
        'form': form,
            }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('logout'))
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('all_posts'))
        else:
            return render(request, 'accounts/login.html',{'error':'Invalid username or password'})

    return render(request, 'accounts/login.html')
    
        
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('login')
