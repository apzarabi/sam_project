from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'users.views.login', name="login"),
    url(r'^logout/$', 'users.views.logout', name="logout"),
    url(r'^test/signup', 'users.views.signup', name='signup'),
    url(r'^signup/customer', 'users.views.signup_customer', name='signup_customer'),
    url(r'^signup/dealer', 'users.views.signup_dealer', name='signup_dealer'),
    url(r'^home/$', 'users.views.home', name='home'),
    url(r'^show_profile/$', 'users.views.show_profile', name='show_profile'),

    url(r'^test/ticket/$', 'users.views.print_ticket', name='ticket'),
    url(r'^test/home/user/$', 'users.views.home_log_out', name='homelogout'),
    url(r'^test/payment/successful/$', 'users.views.payment_success', name='success'),
    url(r'^test/search/category/subcategory/$', 'users.views.search', name='testsearch'),
    url(r'^test/payment/$', 'users.views.payment', name='testpayment'),
    # url(r'^test/home/$', 'users.views.home', name='home'),
    # url(r'^test/home/logout$', 'users.views.home_log_out', name='home_logout'),
    url(r'^test/menu/$', 'users.views.menu', name='test'),
    url(r'^test/customer/$', 'users.views.customer_profile', name='test_customer'),
    url(r'^test/dealer/$', 'users.views.dealer_profile', name='test'),
    url(r'^test/admin/$', 'users.views.admin', name='test_admin'),
    url(r'^test/$', 'users.views.test', name='test'),
    url(r'^admin/$', 'users.views.admin', name='admin'),
    url(r'^profile/username', 'users.views.customer_profile', name='customer_profile'),
    url(r'^profile/dealer', 'users.views.dealer_profile', name='dealer_profile'),
]
