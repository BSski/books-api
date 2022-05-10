from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .filters import AuthorSearchFilter
from .models import Book
from .serializers import BookGetSerializer, BookPostSerializer
from .utils import fetch_json_from_google_api


@api_view(["GET"])
def view_books_list(request: Request) -> Response:
    """
    A view for /books endpoint.
    Possible parameters:
    - /books?published_date=2022,
    - /books?sort=published_date,
    - /books?author=<author>,
    - /books?author=<author1>&author=<author2> [&author=<author3>...].
    """
    published_date = request.query_params.get("published_date")
    sorting_key = request.query_params.get("sort")
    author = request.query_params.getlist("author")

    if published_date:
        books = Book.objects.all().filter(published_date__year=published_date)
    elif sorting_key:
        books = Book.objects.order_by(sorting_key)
    elif author:
        filter = AuthorSearchFilter()
        books = filter.filter_queryset(request.query_params, Book.objects.all())
    else:
        books = Book.objects.all()

    serializer = BookGetSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def view_book(request: Request, id: str) -> Response:
    """A view for /books/<str:id> endpoint."""
    book = get_object_or_404(Book, pk=id)
    serializer = BookGetSerializer(book, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def post_books_to_database(request: Request) -> Response:
    """
    Adds 10 books from Google Books API to the app's database.
    Books are chosen based on a passed "q" parameter.
    """
    books_json = fetch_json_from_google_api(request.data.get("q"))
    if books_json["totalItems"] == 0:
        return Response(
            "No books found for this keyword.", status=status.HTTP_404_NOT_FOUND
        )

    books = BookPostSerializer.create_books_list(books_json)

    for book_idx, book in enumerate(books):
        books[book_idx], created = Book.objects.update_or_create(
            id=book["id"],
            defaults=book,
        )

    serializer = BookPostSerializer(data=books, many=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
