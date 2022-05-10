from django.urls import path
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    path("books/", views.view_books_list, name="get_books"),
    path("books/<str:id>", views.view_book),
    path("db/", views.post_books_to_database, name="post_books"),
    path("", RedirectView.as_view(pattern_name="get_books")),
]
