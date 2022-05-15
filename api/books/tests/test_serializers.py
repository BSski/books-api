from datetime import date

from django.test import TestCase

from books.serializers import BookPostSerializer


class BookPostSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book_list_complete_date = [
            {
                "id": "1",
                "title": "TestTitle1",
                "published_date": "2001-02-03",
            }
        ]
        cls.book_list_date_without_day = [
            {
                "id": "2",
                "title": "TestTitle2",
                "published_date": "2001-02",
            }
        ]
        cls.book_list_date_without_day_and_month = [
            {
                "id": "3",
                "title": "TestTitle3",
                "published_date": "2001",
            }
        ]
        cls.book_list_without_date = [
            {
                "id": "4",
                "title": "TestTitle4",
                "published_date": None,
            }
        ]

    def test_serializer_keeps_full_dates_unchanged(self):
        self.assertEqual(
            BookPostSerializer.fill_incomplete_dates(self.book_list_complete_date)[0][
                "published_date"
            ],
            date(2001, 2, 3),
        )

    def test_serializer_fills_day_in_incomplete_date(self):
        self.assertEqual(
            BookPostSerializer.fill_incomplete_dates(self.book_list_date_without_day)[
                0
            ]["published_date"],
            date(2001, 2, 1),
        )

    def test_serializer_fills_day_and_month_in_incomplete_date(self):
        self.assertEqual(
            BookPostSerializer.fill_incomplete_dates(
                self.book_list_date_without_day_and_month
            )[0]["published_date"],
            date(2001, 1, 1),
        )

    def test_serializer_doesnt_change_none_date(self):
        self.assertEqual(
            BookPostSerializer.fill_incomplete_dates(self.book_list_without_date)[0][
                "published_date"
            ],
            None,
        )
