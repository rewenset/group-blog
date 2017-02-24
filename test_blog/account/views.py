from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string

from .forms import LoginForm, UserRegistrationForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    profile = Profile.objects.get(user=user)
                    if profile.activation_key != '0':
                        messages.error(request, 'Confirm email')
                    else:
                        login(request, user)  # set the user in the current session
                        return redirect('blog:post_list')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Your email and password didn\'t match. Please try again.')
    else:
        form = LoginForm()  # instantiate a new log in form

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.username = new_user.email
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            new_user.save()

            activation_key = get_random_string(length=33)
            url = request.build_absolute_uri(reverse('activation', args=[activation_key]))

            p = Profile(
                user=new_user,
                activation_key=activation_key
            )
            p.save()

            subject = 'Registration'
            message = 'Please confirm sign-up \n'
            message += url
            from_email = settings.EMAIL_HOST_USER
            to_list = [new_user.email]
            send_mail(subject, message, from_email, to_list)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def confirm_signup(request, key):
    profile = get_object_or_404(Profile, activation_key=key)
    profile.activation_key = '0'
    profile.save()
    messages.success('Email confirmed. Now you can sign-in.')
    return redirect('login')
