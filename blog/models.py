from django.db import models
from datetime import date, datetime


class AbstractUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    username = models.CharField(max_length=30)
    date_register = models.DateField()

    def save(self, *args, **kwargs):
        try:
            self.date_register = datetime.strptime(self.date_register, '%d-%m-%Y').date()
        except Exception:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=80)
    authors = models.ManyToManyField(Author, related_name='articles', through='Publication')

    def __str__(self):
        return self.title


class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='publications')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='publications')
    date_published = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.article} {self.author}'
