from django.db import models
from .book import Book

class Loan(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,       
    )

    borrower = models.ForeignKey(
        'Borrower',
        on_delete=models.CASCADE,        
    )

    due_date = models.DateTimeField()
   
    def __str__(self):
        return self.due_date