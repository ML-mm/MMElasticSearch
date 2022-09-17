from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=28)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.title}'


ARTICLE_TYPE = [
    ('UN', 'Unspecified'),
    ('TU', 'Tutorial'),
    ('RS', 'Research'),
    ('RW', 'Review'),
]


class Article(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPE, default='UN')
    categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def type_to_string(self):
        if self.type == 'UN':
            return 'Unspecified'
        elif self.type == 'TU':
            return 'Tutorial'
        elif self.type == 'RS':
            return 'Research'
        elif self.type == 'RW':
            return 'Review'

    def __str__(self):
        return f'{self.author}: {self.name} ({self.created_on.date()})'
