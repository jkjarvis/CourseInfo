from django.conf import settings
from django.db import models
from django.utils import timezone

ratings = (
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
    (0, 0),
)


class Course(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    teacher = models.CharField(max_length=100)
    SubjectField = models.CharField(max_length=200, null=True)
    rating = models.IntegerField(choices=ratings, default=5)
