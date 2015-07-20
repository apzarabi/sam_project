from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'event_cards/$', views.event_cards, name='event_cards'),
    url(r'event_row_verify/$', views.event_row_verify, name='event_row_verify')
]
