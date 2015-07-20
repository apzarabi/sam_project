from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'event_small_card/$', views.event_small_card, name='event_small_card'),
    url(r'event_row_verify/$', views.event_row_verify, name='event_row_verify'),
    url(r'event_row_condition/$', views.event_row_condition, name='event_row_condition'),
    url(r'event_row_purchase/$', views.event_row_purchase, name='event_row_purchase'),
    url(r'event_row_print/$', views.event_row_print, name='event_row_print')


]
