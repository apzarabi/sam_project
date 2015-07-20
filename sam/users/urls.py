from django.conf.urls import url

urlpatterns = [
    url(r'^test/customer/$', 'users.views.customer', name='test'),
    url(r'^test/dealer/$', 'users.views.dealer', name='test'),
    url(r'^test/admin/$', 'users.views.admin', name='test'),
    url(r'^test/$', 'users.views.test', name='test'),
]
