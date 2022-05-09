from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    title = models.CharField(max_length=7000, default="No title")
    authors = models.JSONField(max_length=3000, blank=True, null=True)
    published_date = models.DateField(max_length=30, blank=True, null=True)
    categories = models.JSONField(max_length=3000, blank=True, null=True)
    average_rating = models.FloatField(max_length=10, blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(max_length=20000, blank=True, null=True)

    def __str__(self):
        return self.id
