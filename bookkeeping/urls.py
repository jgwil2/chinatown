from django.conf.urls import url

from .views import Index, Book, Expense

urlpatterns = [
    # ex: /
    url(r'^$', Index.as_view(), name='index'),
    # ex: /5/
    url(r'^(?P<book_id>[0-9]+)/$', Book.as_view(), name='book')
]
