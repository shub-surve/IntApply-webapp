from django.shortcuts import render, redirect
from .forms import CreateUserForm, CustomLoginForm, UserProfileForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

def homepage(request):
    return render(request, 'userhome.html')

def registeruser(req):
    form = CreateUserForm()
    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()  # Call save() correctly
            return redirect('user_login')  # Redirect to login page after registration
    context = {
        'form': form,
    }
    return render(req, 'userregister.html', context)

class LoginUser (View):
    def get(self, request):
        form = CustomLoginForm()  
        return render(request, 'userlogin.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('complete_profile') 
        else:
            return redirect('user_login')  
@login_required  

@login_required
def complete_profile(request):
    # Get or create the UserProfile object
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Redirect if the profile is already completed
    if user_profile.profile_completed:
        return redirect('homepage')  # Replace 'home' with the appropriate URL name

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            user_profile.profile_completed = True 
            user_profile.save()
            return redirect('homepage')  
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'completeprofile.html', {'form': form})