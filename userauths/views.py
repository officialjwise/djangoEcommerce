from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL


def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("store:index")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/register.html", context)


def loginView(request):
    # Checking if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("store:index")

    if request.method == "POST":
        email_or_username = request.POST.get("email_or_username")
        password = request.POST.get("password")

        # Using try and except block to filter the errors
        try:
            # Check if email_or_username contains "@" symbol
            if '@' in email_or_username:
                user = User.objects.get(email=email_or_username)
            else:
                user = User.objects.get(username=email_or_username)
        except User.DoesNotExist:
            messages.warning(request, f"No user found with {email_or_username}. Please check your credentials or register.")
            return redirect("userauths:register")

        # Authenticate using either email or username, not both
        user = authenticate(request, username=user.username, password=password) or \
               authenticate(request, email=user.email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You're logged in!")
            return redirect("store:index")
        else:
            messages.warning(request, f"Invalid login credentials.")

    context = {}
    return render(request, "userauths/login.html", context)
