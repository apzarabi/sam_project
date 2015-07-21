from django.conf.urls import url

urlpatterns = [
    url(r'^/test/search/category/subcategory/$', 'users.views.search', name='testsearch'),
    url(r'^test/payment/$', 'users.views.payment', name='testpayment'),
    url(r'^test/home/$', 'users.views.home', name='testhome'),
    url(r'^test/menu2/$', 'users.views.menu2', name='test'),
    url(r'^test/menu/$', 'users.views.menu', name='test'),
    url(r'^test/customer/$', 'users.views.customer', name='test'),
    url(r'^test/dealer/$', 'users.views.dealer', name='test'),
    url(r'^test/admin/$', 'users.views.admin', name='test'),
    url(r'^test/$', 'users.views.test', name='test'),
]
