# -*- coding: utf-8 -*-
import pdb
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as auth_logout
from django.contrib.auth.decorators import login_required

from events.models import *
from users.models import Dealer, Customer
from .forms import UserForm, UserInfoForm, CustomerForm, DealerForm, AddSubCategory, AddCategory, EditCategory, EditUserForm
from django.http import HttpResponse, HttpResponseRedirect
from events.forms import EventForm
from django.core import serializers


from django.views.decorators.http import condition


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
    form1 = AddSubCategory()
    form2 = AddCategory()
    edit_form1 = EditCategory()
    user = request.user
    print("is auth? {}".format(user.is_authenticated()))
    categories = Category.objects.all()
    allevents = Event.objects.all()
    if user.is_superuser:
                return render(request, 'admin_profile.html', {'user': user,
                                                              'profile_user': user,
                                                              'categories': categories,
                                                              'form1': form1,
                                                              'form2': form2,
                                                              'edit_form1': edit_form1,
                                                              'allevents': allevents})
    try:
        customer = user.userinfo.customer
        return render(request, 'customer_profile.html', {'user': user,
                                                         'profile_user': customer,
                                                         'categories': categories})
    except Customer.DoesNotExist:
        try:
            dealer = user.userinfo.dealer
            print("is auth dealer? {}".format(user.is_authenticated()))
            eventform = EventForm()
            return render(request, 'dealer_profile.html', {'user': user,
                                                           'profile_user': dealer,
                                                           'categories': categories,
                                                           'eventform': eventform})
        except Dealer.DoesNotExist:
            print('no cases {}'.format(user))

@login_required
def edit_profile(request):
    id = request.user.id
    user = User.objects.get(id=id)
    if request.method == "POST":
        ret = {
            'userForm': EditUserForm(request.POST, instance=user),
        }
    else:
        ret = {
            'userForm': EditUserForm(instance=user),
        }
    return render(request, 'auth/edit_user_page.html', ret)

@login_required  
def submit_edit_profile(request):
    user = request.user
    errors = {}
    if request.method == "POST":
        userForm = EditUserForm(request.POST, instance=user)
        if not userForm.is_valid():
                errors = errors.copy()
                errors.update(userForm.errors)
        if not errors:
            new_user = userForm.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password'])
            login_auth(request, auth_user)
            return redirect(reverse('users:home'))
        else:  # if errors
            print("sign up errors: {}".format(errors))
            return render(request, 'auth/edit_user_page.html', {'signup_customer_errors': errors,
                                                 'userForm': userForm,
            })
    else:
        return redirect(reverse('users:home'))
        
def add_subcategory(request):
    categories = Category.objects.all()
    if request.method == 'POST' and 'add_subcat' in request.POST:
        form1 = AddSubCategory(request.POST)
        if form1.is_valid():
            print("hellloooo")
            subcat = form1.save()
        return_url = reverse('users:show_profile')
        return render(request, 'info_template.html', {'message':"زیر دسته مورد نظر اضافه شد.", 'return_url': return_url})
    else:
        form1 = AddSubCategory()
        form2 = AddCategory()
    return render(request, 'admin_profile.html', {'form2': form2, 'form1': form1, 'categories':categories})

def add_category(request):
    categories = Category.objects.all()
    if request.method == 'POST' and 'add_cat' in request.POST:
        form2 = AddCategory(request.POST)
        if form2.is_valid():
            cat = form2.save()
        return_url = reverse('users:show_profile')
        return render(request, 'info_template.html', {'message':"دسته مورد نظر اضافه شد.", 'return_url': return_url})
    else:
        form1 = AddSubCategory()
        form2 = AddCategory()
    return render(request, 'admin_profile.html', {'form2': form2, 'form1': form1, 'categories':categories})

def edit_category(request):
    categories = Category.objects.all()
    if request.method == 'POST' and 'edit_cat' in request.POST:
        edit_form1 = EditCategory(request.POST)
        if edit_form1.is_valid():
            prev_cat = Category.objects.get(id= request.POST.get('subject'))
            prev_cat.name = request.POST.get('name')
            new_cat = prev_cat.save()
        return_url = reverse('users:show_profile')
        return render(request, 'info_template.html', {'message':"نام دسته مورد نظر به روزرسانی شد.", 'return_url': return_url})
    else:
        form1 = AddSubCategory()
        form2 = AddCategory()
        edit_form1 = EditCategory()
    return render(request, 'admin_profile.html', {'form1':form1, 'form2':form2, 'edit_form1':edit_form1, 'categories':categories})


def edit_subcategory(request):
    subcategories = Subcategory.objects.all()
    categories = Category.objects.all()
    print(request.POST)
    if request.method == 'POST' and 'edit_subcat' in request.POST:
        print(request.POST)
        subcat = Subcategory.objects.get(id=request.POST.get('editSub'))
        subcat.name = request.POST.get('subcat_name')
        subcat.save()
        return_url = reverse('users:show_profile')
        return render(request, 'info_template.html', {'message':"نام زیردسته مورد نظر به روزرسانی شد.", 'return_url': return_url})
    else:
        form1 = AddSubCategory()
        form2 = AddCategory()
        edit_form1 = EditCategory()
    return render(request, 'admin_profile.html', {'form1':form1, 'form2':form2, 'edit_form1':edit_form1, 'categories':categories})


def remove_subcategory(request):
    subcategories = Subcategory.objects.all()
    categories = Category.objects.all()
    print(request.POST)
    if request.method == 'POST' and 'remove_subcat' in request.POST:
        print(request.POST)
        Subcategory.objects.filter(id=request.POST.get('removeSub')).delete()
        return_url = reverse('users:show_profile')
        return render(request, 'info_template.html', {'message':"زیردسته مورد نظر حذف شد.", 'return_url': return_url})
    else:
        form1 = AddSubCategory()
        form2 = AddCategory()
        edit_form1 = EditCategory()
    return render(request, 'admin_profile.html', {'form1':form1, 'form2':form2, 'edit_form1':edit_form1, 'categories':categories})


def home(request):
    event = Event.objects.get(id=1)
    categories = Category.objects.all()
    accepted = Event.objects.filter(condition=0).all()
    time_sorted = sorted(accepted, key= lambda t: t.first_date())
    newevents = time_sorted[:6]
    
    sell_sorted = sorted(accepted, key= lambda t: t.sold_tickets_number())
    topsellerevents = sell_sorted[:6]
    
    popular_sorted = sorted(accepted, key= lambda t: t.rating())
    popularevents = popular_sorted[:6]
    return render(request, 'home.html', {'categories': categories, 'event': event, 'newevents': newevents,
                                         'topsellerevents': topsellerevents, 'popularevents': popularevents})

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


def all_json_subs(request, catpk):
    print(catpk)
    print("HHHHH")
    current_cat = Category.objects.get(pk=catpk)
    print(current_cat)
    subs = Subcategory.objects.all().filter(category=current_cat)
    print(subs)
    json_subs = serializers.serialize("json", subs)
    print(json_subs)
    return HttpResponse(json_subs)
