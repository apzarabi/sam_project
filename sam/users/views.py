from django.shortcuts import render


# Create your views here.


def test(request):
    return render(request, 'base.html', {})


def sidebar(request):
    return render(request, 'right_sidebar_profile.html', {})


def dealer(request):
    return render(request, 'right_sidebar_profile_dealer.html', {})


def customer(request):
    return render(request, 'right_sidebar_profile_customer.html', {})


def admin(request):
    return render(request, 'right_sidebar_profile_admin.html', {})


def menu(request):
    return render(request, 'right_sidebar_menu.html', {})


def menu2(request):
    return render(request, 'right_sidebar_menu2.html', {})


def home(request):
    return render(request, 'home.html', {})


def home_log_out(request):
    return render(request, 'home_log_out.html', {})


def payment(request):
    return render(request, 'payment.html', {})