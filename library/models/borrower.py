from django.db import models
from .book import Book
from .loan import Loan
class Borrower(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    borrowed_books = models.ManyToManyField(
        Book, 
        through=Loan, 
        through_fields=('borrower', 'book')
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"