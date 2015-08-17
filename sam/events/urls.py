from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register_event/$', views.register_event, name="register_event"),
    url(r'event_small_card/$', views.event_cards, name='event_small_card'),
    url(r'event_row_verify/$', views.event_row_verify, name='event_row_verify'),
    url(r'event_row_condition/$', views.event_row_condition, name='event_row_condition'),
    url(r'event_row_purchase/$', views.event_row_purchase, name='event_row_purchase'),
    url(r'event_row_print/$', views.event_row_print, name='event_row_print'),
    url(r'event_cards/$', views.event_cards, name='event_cards'),
    url(r'^edit_event/(?P<event_id>\d+)/(?P<done>\d+)$', views.event_edit_page, name='event_edit'),
    url(r'event_row_verify/$', views.event_row_verify, name='event_row_verify'),
    url(r'^remove_category/$', views.remove_category, name='remove_category'),
    url(r'^subcategory/(?P<category_id>([0-9])+)/(?P<subcategory_id>([0-9])+)/$', views.show_subcategory, name='show_subcategory'),
    url(r'^(?P<event_id>\d+)/$', views.event_view, name='event_view'),
    url(r'^delete_event/(?P<event_id>\d+)/$', views.delete, name='delete'),
    url(r'^info_template/', views.info_template, name="info_template"),
    url(r'^edit_event_details/$', views.edit_event_details, name="edit_event_details"),
]
