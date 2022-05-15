from datetime import date

from django.test import TestCase

from books.models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_book = Book(
            id="1",
            title="TestTitle",
            authors=["TestAuthor"],
            published_date=date(2022, 3, 22),
            categories=["TestCategory"],
            average_rating=5.0,
            ratings_count=15,
            thumbnail="http://www.test.com/test",
        )

    def test_book_str_equals_book_id(self):
        self.assertEqual(str(self.test_book), self.test_book.id)
