from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'users.views.login', name="login"),
    url(r'^logout/$', 'users.views.logout', name="logout"),
    url(r'^test/signup', 'users.views.signup', name='signup'),
    url(r'^signup/customer', 'users.views.signup_customer', name='signup_customer'),
    url(r'^signup/dealer', 'users.views.signup_dealer', name='signup_dealer'),
    url(r'^home/$', 'users.views.home', name='home'),
    url(r'^show_profile/$', 'users.views.show_profile', name='show_profile'),
    url(r'^ticket/(?P<return_code>\d+)/$', 'users.views.print_ticket', name='ticket'),
    url(r'^test/home/user/$', 'users.views.home_log_out', name='homelogout'),
    url(r'^payment/successful/$', 'users.views.payment_success', name='success'),
    url(r'^payment/$', 'users.views.payment', name='payment'),
    url(r'^cancel_payment/$', 'users.views.cancel_payment', name='cancel_payment'),
    url(r'^test/search/category/subcategory/$', 'users.views.search', name='testsearch'),
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
    url(r'^add_category', 'users.views.add_category', name='add_category'),
    url(r'^add_subcategory', 'users.views.add_subcategory', name="add_subcategory"),
    url(r'^edit_category', 'users.views.edit_category', name="edit_category"),
    url(r'^edit_profile', 'users.views.edit_profile', name='edit_profile'),
    url(r'^submit_edit_profile', 'users.views.submit_edit_profile', name='submit_edit_profile'),
]
