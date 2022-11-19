from django.db import models
from .author import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='written_books'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, written by {self.author}. Last updated at: {self.updated_at}"

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
        }