from django.conf.urls import url

urlpatterns = [
    url(r'^test/$', 'users.views.test', name='test'),
    url(r'^show/(?P<movie_id>([0-9])+)/$', 'movies.views.show_movie', name='show_movie'),
]
