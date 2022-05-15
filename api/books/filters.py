from functools import reduce
import operator

from django.db import models
from django.db.models.query import QuerySet
from django.http.request import QueryDict

from rest_framework import filters


class AuthorSearchFilter(filters.SearchFilter):
    """Enables querying the database for books of multiple authors simultaneously."""

    search_param = "author"

    def get_search_terms(self, query_params: QueryDict) -> list:
        """Returns authors extracted from the request and strips null characters."""
        params = query_params.getlist(self.search_param, "")
        for idx, param in enumerate(params):
            params[idx] = param.replace("\x00", "")
        return params

    def filter_queryset(self, query_params: QueryDict, queryset: QuerySet) -> QuerySet:
        """Finds books written by authors enumerated in the query."""
        search_fields = ["authors"]
        search_terms = self.get_search_terms(query_params)
        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field)) for search_field in search_fields
        ]

        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term}) for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.and_, queries))  # originally or_
        queryset = queryset.filter(reduce(operator.or_, conditions))  # originally and_
        return queryset
