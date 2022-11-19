from rest_framework import serializers

from .models.book import Book
from .models.author import Author
from .models.borrower import Borrower
from .models.loan import Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book

class BookReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Author

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Borrower

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Loan

class LoanReadSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    borrower = serializers.StringRelatedField()   
    class Meta:
        fields = '__all__'
        model = Book