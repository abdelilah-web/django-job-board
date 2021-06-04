from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import ProfileForm, UserForm
from django.urls import reverse
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts/profile')
    else:
        form = SignupForm()
    context= {
        'form' : form
    }

    return render(request,'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'accounts/profile.html', {'profile':profile})


def edit_profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        formuser = UserForm(request.POST,instance=request.user)
        formprofile = ProfileForm(request.POST,request.FILES, instance=profile)
        if formuser.is_valid() and formprofile.is_valid():
            formuser.save()
            myprofile = formprofile.save(commit= False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else :
        formuser = UserForm(instance=request.user)
        formprofile = ProfileForm(instance=profile)

    context = {
        'formuser': formuser,
        'formprofile': formprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)