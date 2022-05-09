from datetime import date

from django.test import TestCase
from django.urls import reverse

from booksapi.models import Book

# coverage run --source='booksapi' manage.py test && coverage report & coverage html


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.books_list_url = reverse("get_books")
        cls.post_books_url = reverse("post_books")
        Book.objects.create(id="1", title="TestTitle")


class BooksListHttpMethodsTest(BaseTest):
    def test_can_use_get_method_to_books_list_endpoint(self):
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, 200)

    def test_cant_use_post_method_to_books_list_endpoint(self):
        response = self.client.post(self.books_list_url, format="text/html")
        self.assertEqual(response.status_code, 405)

    def test_cant_use_put_method_to_books_list_endpoint(self):
        response = self.client.put(self.books_list_url, format="text/html")
        self.assertEqual(response.status_code, 405)

    def test_cant_use_delete_method_to_books_list_endpoint(self):
        response = self.client.delete(self.books_list_url, format="text/html")
        self.assertEqual(response.status_code, 405)


class BooksListViewTest(BaseTest):
    def test_can_view_books_list(self):
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, 200)

    def test_can_filter_books_by_publishing_date(self):
        response = self.client.get(self.books_list_url + "?published_date=2022")
        self.assertEqual(response.status_code, 200)

    def test_can_sort_books_by_publishing_date(self):
        response = self.client.get(self.books_list_url + "?sort=published_date")
        self.assertEqual(response.status_code, 200)

    def test_can_sort_books_by_negative_publishing_date(self):
        response = self.client.get(self.books_list_url + "?sort=-published_date")
        self.assertEqual(response.status_code, 200)

    def test_can_filter_books_by_single_author(self):
        response = self.client.get(self.books_list_url + "?author=Test1")
        self.assertEqual(response.status_code, 200)

    def test_can_filter_books_by_many_authors(self):
        response = self.client.get(self.books_list_url + "?author=Test1&author=Test2")
        self.assertEqual(response.status_code, 200)

    def test_cant_use_nonexistent_parameters(self):
        response = self.client.get(self.books_list_url + "?nonexistant=1")
        self.assertEqual(response.status_code, 400)


class SingleBookViewTest(BaseTest):
    def test_can_view_existent_book_correctly(self):
        response = self.client.get(self.books_list_url + "1")
        self.assertEqual(response.status_code, 200)

    def test_cant_view_nonexistent_book_correctly(self):
        response = self.client.get(self.books_list_url + "-1")
        self.assertEqual(response.status_code, 404)


class PostBooksHttpMethodsTest(BaseTest):
    def test_can_use_post_method_to_post_books_endpoint(self):
        response = self.client.post(self.post_books_url, format="text/html")
        self.assertEqual(response.status_code, 201)

    def test_cant_use_get_method_to_post_books_endpoint(self):
        response = self.client.get(self.post_books_url, format="text/html")
        self.assertEqual(response.status_code, 405)

    def test_cant_use_put_method_to_post_books_endpoint(self):
        response = self.client.put(self.post_books_url, format="text/html")
        self.assertEqual(response.status_code, 405)

    def test_cant_use_delete_method_to_post_books_endpoint(self):
        response = self.client.delete(self.post_books_url, format="text/html")
        self.assertEqual(response.status_code, 405)


class PostBooksTest(BaseTest):
    def test_can_post_books_with_keyword(self):
        response = self.client.post(
            self.post_books_url, {"q": "war"}, format="text/html"
        )
        self.assertEqual(response.status_code, 201)

    def test_can_not_find_any_books_with_keyword(self):
        response = self.client.post(
            self.post_books_url, {"q": "pppwwwtttrrrmmm"}, format="text/html"
        )
        self.assertEqual(response.status_code, 404)
