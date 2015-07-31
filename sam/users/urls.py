from django.conf.urls import url

urlpatterns = [
    url(r'^test/ticket/$', 'users.views.print_ticket', name='ticket'),
    url(r'^test/home/user/$', 'users.views.home_log_out', name='homelogout'),
    url(r'^test/payment/successful/$', 'users.views.payment_success', name='success'),
    url(r'^test/search/category/subcategory/$', 'users.views.search', name='testsearch'),
    url(r'^test/payment/$', 'users.views.payment', name='testpayment'),
    url(r'^test/home/$', 'users.views.home', name='home'),
    url(r'^test/home/logout$', 'users.views.home_log_out', name='home_logout'),
    url(r'^test/menu2/$', 'users.views.menu2', name='test'),
    url(r'^test/menu/$', 'users.views.menu', name='test'),
    url(r'^test/customer/$', 'users.views.customer', name='test_customer'),
    url(r'^test/dealer/$', 'users.views.dealer', name='test'),
    url(r'^test/admin/$', 'users.views.admin_test', name='test'),
    url(r'^test/$', 'users.views.test', name='test'),
    url(r'^admin/$', 'users.views.admin', name='admin'),
    url(r'^profile/username', 'users.views.customer_profile', name='customer_profile'),
    url(r'^profile/dealer', 'users.views.dealer_profile', name='dealer_profile'),
]
