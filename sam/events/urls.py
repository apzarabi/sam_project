from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'event_small_card/$', views.event_small_card, name='event_small_card')
]
