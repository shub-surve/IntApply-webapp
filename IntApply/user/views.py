from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CustomLoginForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile , Education


def homepage(request):
    return render(request, 'userhome.html')


def registeruser(req):
    form = CreateUserForm()
    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            user = form.save()
            messages.success(req, "Registration successful! Please log in.")
            return redirect('user_login')
        else:
            messages.error(req, "There was an error with your registration. Please try again.")
    context = {'form': form}
    return render(req, 'userregister.html', context)





def LoginUser(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            
            user = authenticate(request, username=username, password=password)
            if user:
               
                user_profile , created = UserProfile.objects.get_or_create(user=user)
                
                
                login(request, user)
                
                
                if user_profile.profile_completed:
                    messages.success(request, f"Welcome back, {user.username}!")
                    return redirect('dashboard' , username = user.username)
                else:
                    messages.info(request, "Please complete your profile to proceed.")
                    return redirect('complete_profile')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "Please correct the highlighted errors in the form.")
    else:
        form = CustomLoginForm()  # Initialize a blank form for GET requests

    # Render the login form
    return render(request, 'userlogin.html', {'form': form})


@login_required
def complete_profile(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if user_profile.profile_completed:
        return redirect('homepage')
    

    form = UserProfileForm(request.POST or None, instance=user_profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        user_profile.profile_completed = True
        user_profile.save()
        messages.success(request, "Profile completed successfully!")
        
        return redirect('dashboard') 
    return render(request, 'completeprofile.html', {'form': form , 'profile_complete_percent' : user_profile.calculate_percent()})


def logoutuser(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('user_login')



@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    educations = Education.objects.filter(user__username=username)
    skills = user_profile.skills.all()
    completion_percentage = user_profile.calculate_percent()
    context = {
        'user_profile': user_profile,
        'educations': educations,
        'skills': skills,
        'completion_percentage': completion_percentage,
    }
    # print(educations)
    return render(request, 'userprofile.html', context)

