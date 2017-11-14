from django.http import HttpResponse
from django.shortcuts import render #, redirect
from django.contrib.auth import authenticate, login #, logout
from django.contrib.auth.decorators import login_required
#from django.contrib import messages
from .forms import LoginForm#, UserRegistrationForm, UserEditForm, ProfileEditForm
#from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context )