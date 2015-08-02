# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as auth_logout

from .forms import UserForm, UserInfoForm, CustomerForm, DealerForm

def make_sign_up_form():
    """ every view that has sign up button, should call this method and put the
     return form of this method to context with key='sign_up_form' """
    ret = {
        'userForm': UserForm(),
        'userInfoForm': UserInfoForm(),
        'customerForm': CustomerForm(),
        'dealerForm': DealerForm(),
    }
    return ret

def login(request):
    errors = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login_auth(request, user)
                return redirect(reverse('users:home'))
            else:
                errors = "شما نمی‌تواند وارد سامانه شوید."
        else:
            errors = "نام کاربری یا رمز عبور غلط است."

    return render(request, 'home.html', {'login_errors': errors})

def home(request):
    forms = make_sign_up_form()
    context = {}
    context.update(forms)
    print('forms: {}'.format(forms))
    print('i was here {}'.format(context))
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return redirect(reverse('users:home'))

def test(request):
    return render(request, 'base.html', {})


def sidebar(request):
    return render(request, 'right_sidebar_profile.html', {})


def dealer(request):
    return render(request, 'right_sidebar_profile_dealer.html', {})


def customer(request):
    return render(request, 'right_sidebar_profile_customer.html', {})


def admin_test(request):
    return render(request, 'right_sidebar_profile_admin.html', {})


def menu(request):
    return render(request, 'right_sidebar_menu.html', {})

def home_log_out(request):
    return render(request, 'home_log_out.html', {})

def payment(request):
    return render(request, 'payment.html', {})


def search(request):
    return render(request, 'subcategory_view.html', {})


def admin(request):
    return render(request, 'admin_profile.html', {})


def payment_success(request):
    return render(request, 'successful_payment.html', {})


def print_ticket(request):
    return render(request, 'printable_ticket.html', {})


def customer_profile(request):
    return render(request, 'customer_profile.html', {})


def dealer_profile(request):
    return render(request, 'dealer_profile.html', {})