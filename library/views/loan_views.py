from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.loan import Loan
from ..serializers import LoanSerializer, LoanReadSerializer

# Create your views here.
#localhost:8000/library/Loans/ get post
class LoansView(APIView):
    """View class for Loans/ for viewing all and creating"""
    serializer_class = LoanSerializer
    def get(self, request):
        Loans = Loan.objects.all()
        serializer = LoanReadSerializer(Loans, many=True)
        return Response({'Loans': serializer.data})

    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:8000/library/Loans/:id get delete update
class LoanDetailView(APIView):
    """View class for Loans/:pk for viewing a single Loan, updating a single Loan, or removing a single Loan"""
    serializer_class = LoanSerializer
    def get(self, request, pk):
        Loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanReadSerializer(Loan)
        return Response({'Loan': serializer.data})

    def patch(self, request, pk):
        Loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanSerializer(Loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Loan = get_object_or_404(Loan, pk=pk)
        Loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)