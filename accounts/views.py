from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegistrationForm, UserForm, ProfileForm, updateProfileForm, updateUserForm
from payment.models import DonateLineItem, Details
from django.contrib.auth import update_session_auth_hash

# This def creates the login capability and uses the login form from the forms.py file

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "Welcome to Help the Homeless!")
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
        else:
            login_form.add_error(None, "Incorrect username or password, please try again.")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

# This section deals with the logout function

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Thank you for visiting, please come again")
    return redirect(reverse('index'))

# this section contains the registration def used to allow new users to register an account

def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)  
              
        if registration_form.is_valid():
            registration_form.save() 
                       
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome to Help the Homless")
            else:
                messages.error(request, "Something went wrong, please try again")
    else:
        registration_form = RegistrationForm()
    return render(request, 'registration.html',
                  {"registration_form": registration_form})
@login_required
def profile(request):
    return render(request, 'profile.html')
@login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        u_form = updateUserForm(request.POST,
                                instance=request.user)
        p_form = updateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your Profile Has Been Updated")
            return redirect('profile')
    else:
        u_form = updateUserForm(instance=request.user)
        p_form = updateProfileForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changePassword.html', {
        'form': form
    })

def delete_user(request, id):
    obj = get_object_or_404(User, id=id)
    #POST request
    if request.method == "POST":
        #confirming deletion
        obj.delete()
        return redirect('index.html')
    context = {
        "object": obj
    }
    return render(request,"profile.html", context)
    