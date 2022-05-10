import datetime

from rest_framework import serializers

from .models import Book


class BookGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "authors",
            "published_date",
            "categories",
            "average_rating",
            "ratings_count",
            "thumbnail",
        )
        optional_fields = [
            "authors",
            "published_date",
            "categories",
            "average_rating",
            "ratings_count",
            "thumbnail",
        ]


class BookPostSerializer(serializers.ModelSerializer):
    fields_case_names = {
        "title": "title",
        "authors": "authors",
        "categories": "categories",
        "averageRating": "average_rating",
        "ratingsCount": "ratings_count",
        "publishedDate": "published_date",
    }

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "authors",
            "published_date",
            "categories",
            "average_rating",
            "ratings_count",
            "thumbnail",
        )
        optional_fields = [
            "authors",
            "published_date",
            "categories",
            "average_rating",
            "ratings_count",
            "thumbnail",
        ]

    @classmethod
    def create_books_list(cls, books_json: dict) -> list:
        """Returns a list of dicts with information selected from a JSON."""
        books_to_post = []
        for json_book in books_json["items"]:
            info = json_book["volumeInfo"]
            book = {"id": json_book["id"]}
            for camelcase_name, snakecase_name in cls.fields_case_names.items():
                book[snakecase_name] = info.get(camelcase_name)
            info_image_links = info.get("imageLinks", {})
            book["thumbnail"] = info_image_links.get("thumbnail")
            books_to_post.append(book)
        books_to_post_with_complete_dates = cls.fill_incomplete_dates(books_to_post)
        return books_to_post_with_complete_dates

    @staticmethod
    def fill_incomplete_dates(books_to_post: list) -> list:
        """
        Processes publishing dates of books.
        YYYY-MM changes to YYYY-MM-01 and YYYY changes to YYYY-01-01.
        """
        books_to_post = books_to_post[:]
        for book in books_to_post:
            if book["published_date"] is None:
                continue
            date_fields = book["published_date"].split("-")
            date_fields = map(int, date_fields)
            new_date = [None, 1, 1]
            for idx, value in enumerate(date_fields):
                new_date[idx] = value
            book["published_date"] = datetime.date(*new_date)
        return books_to_post
