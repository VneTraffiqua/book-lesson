from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]