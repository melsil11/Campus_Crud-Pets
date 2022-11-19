from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.borrower import Borrower
from ..serializers import BorrowerSerializer

# Create your views here.
#localhost:8000/library/borrowers/ get post
class BorrowersView(APIView):
    """View class for borrowers/ for viewing all and creating"""
    serializer_class = BorrowerSerializer
    def get(self, request):
        borrowers = Borrower.objects.all()
        serializer = BorrowerSerializer(borrowers, many=True)
        return Response({'borrowers': serializer.data})

    def post(self, request):
        serializer = BorrowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:8000/library/borrowers/:id get delete update
class BorrowerDetailView(APIView):
    """View class for borrowers/:pk for viewing a single borrower, updating a single borrower, or removing a single borrower"""
    serializer_class = BorrowerSerializer
    def get(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        serializer = BorrowerSerializer(borrower)
        return Response({'borrower': serializer.data})

    def patch(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        serializer = BorrowerSerializer(borrower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        borrower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)