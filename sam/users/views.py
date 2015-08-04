# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as auth_logout
from django.contrib.auth.decorators import login_required

from events.models import *
from users.models import Dealer, Customer
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

    return render(request, 'auth/login_page.html', {'login_errors': errors})


def signup(request):
    return render(request, 'auth/signup_page.html', {
                                                    'userForm': UserForm(),
                                                    'userInfoForm': UserInfoForm(),
                                                    'customerForm': CustomerForm(),
                                                    'dealerForm': DealerForm(),
    })

def signup_customer(request):
    errors = {}
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        userInfoForm = UserInfoForm(request.POST, request.FILES)
        customerForm = CustomerForm(request.POST)
        if not userForm.is_valid():
            errors = errors.copy()
            errors.update(userForm.errors)
        if not userInfoForm.is_valid():
            errors = errors.copy()
            errors.update(userInfoForm.errors)
        if not customerForm.is_valid():
            errors = errors.copy()
            errors.update(customerForm.errors)
        if not errors:
            new_user = userForm.save()
            new_user_info = userInfoForm.save(commit=False)
            new_user_info.user = new_user
            new_user_info.save()
            new_customer = customerForm.save(commit=False)
            new_customer.userInfo = new_user_info
            new_customer.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password'])
            login_auth(request, auth_user)
            return redirect(reverse('users:home'))
        else:  # if errors
            print("sign up errors: {}".format(errors))
            return render(request, 'auth/signup_page.html', {'signup_customer_errors': errors,
                                                 'userForm': userForm,
                                                  'userInfoForm': userInfoForm,
                                                  'customerForm': customerForm,
            })


def signup_dealer(request):
    errors = {}
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        userInfoForm = UserInfoForm(request.POST, request.FILES)
        dealerForm = DealerForm(request.POST)
        if not userForm.is_valid():
            errors = errors.copy()
            errors.update(userForm.errors)
        if not userInfoForm.is_valid():
            errors = errors.copy()
            errors.update(userInfoForm.errors)
        if not dealerForm.is_valid():
            errors = errors.copy()
            errors.update(dealerForm.errors)
        if not errors:
            new_user = userForm.save()
            new_user_info = userInfoForm.save(commit=False)
            new_user_info.user = new_user
            new_user_info.save()
            new_customer = dealerForm.save(commit=False)
            new_customer.userInfo = new_user_info
            new_customer.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password'])
            login_auth(request, auth_user)
            return redirect(reverse('users:home'))
        else:  # if errors
            print("sign up errors: {}".format(errors))
            return render(request, 'auth/signup_page.html', {'signup_customer_errors': errors,
                                                 'userForm': userForm,
                                                  'userInfoForm': userInfoForm,
                                                  'dealerForm': dealerForm,
            })

@login_required
def show_profile(request):
    user = request.user
    print("is auth? {}".format(user.is_authenticated()))
    categories = Category.objects.all()
    try:
        customer = user.userinfo.customer
        return render(request, 'customer_profile.html', {'user': user,
                                                         'profile_user': customer,
                                                         'categories': categories})
    except Customer.DoesNotExist:
        try:
            dealer = user.userinfo.dealer
            print("is auth dealer? {}".format(user.is_authenticated()))
            return render(request, 'dealer_profile.html', {'user': user,
                                                           'profile_user': dealer,
                                                           'categories': categories})
        except Dealer.DoesNotExist:
            if user.is_superuser:
                return render(request, 'admin_profile.html', {'user': user,
                                                              'profile_user': user,
                                                              'categories': categories})
    print('no cases {}'.format(user))


def home(request):
    event = Event.objects.get(id=1)
    forms = make_sign_up_form()
    context = {}
    context.update(forms)
    categories = Category.objects.all()
    return render(request, 'home.html', {'context': context, 'categories': categories, 'event': event})

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
    print("HOI")
    categories = Category.objects.all()
    return render(request, 'right_sidebar_profile_admin.html', {'categories': categories})


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
