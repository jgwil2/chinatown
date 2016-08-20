from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<book_id>[0-9]+)/$', views.book, name='book')
]
