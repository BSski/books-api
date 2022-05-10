from django.http import QueryDict
from django.test import TestCase

from booksapi.filters import AuthorSearchFilter
from booksapi.models import Book


class AuthorSearchFilterTest(TestCase):
    def test_filter_without_params_returns_all_books(self):
        query_params = QueryDict("")
        filter = AuthorSearchFilter()
        all_books = Book.objects.all()
        filtered_books = filter.filter_queryset(query_params, all_books)
        self.assertEqual(filtered_books, all_books)
