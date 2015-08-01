from django.shortcuts import render


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


def home(request):
    return render(request, 'home.html', {})


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
    return render(request, 'customer_profile', {})


def dealer_profile(request):
    return render(request, 'dealer_profile.html', {})