from email.policy import default
from ftplib import all_errors
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    country = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='author/', default='author/no-photo.jpg')
    def __str__(self):
        return f'{self.surname} {self.name}'

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    year = models.IntegerField(validators=[MinValueValidator(1)], null=False, default=1)
    slug = models.SlugField(default='', null=True, blank=True, allow_unicode=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} id {self.id}'




