from django.urls import path 
from .views.book_views import BooksView, BookDetailView
from .views.author_views import AuthorsView, AuthorDetailView
from .views.borrower_views import BorrowersView, BorrowerDetailView
from .views.loan_views import LoansView, LoanDetailView

urlpatterns = [
    path('books/', BooksView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('borrowers/', BorrowersView.as_view(), name='borrowers'),
    path('borrowers/<int:pk>/', BorrowerDetailView.as_view(), name='borrow'),
    path('loans/', LoansView.as_view(), name='loans'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan'),
]
