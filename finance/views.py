from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet , ViewSet
from rest_framework.response import Response
from finance.models import Category ,Income ,Expense
from rest_framework import status
from finance.serializer import CategorySerializer ,IncomeSerializer ,ExpenseSerializer
from django.contrib import messages
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated 
from finance.permissions import IsAdminUserCustom , IsOwner
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import Mypagination
from django.db.models import Sum
from datetime import date 


class CategoryApiView(APIView):
    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category , id=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else : 
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try : 
            Category1 = Category.objects.get(id = pk)
            Category1.delete()
            return Response (status=status.HTTP_200_OK)
        except Category.DoesNotExist : 
            return Response (status=status.HTTP_404_NOT_FOUND)
# ---------------------------------------------------------------


class IncomeViewset (ModelViewSet) : 
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer 
    permission_classes = [IsAuthenticated | IsAdminUserCustom]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category' , 'fullname' , 'date']
    pagination_class = Mypagination



class ExpenseViewSet (ModelViewSet) : 
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer 
    permission_classes = [IsAuthenticated | IsOwner]


# ----------------------------------------------------------------
class IncomeModelViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    @action(detail=False, methods=["get"])
    def monthly_report(self, request):
       today = date.today()

       total_income = Income.objects.filter(
           date__year = today.year , date__month =today.month
           ).aggregate(total = Sum("amount"))["total"] or 0
       
       total_expense = Expense.objects.filter(
           date__year = today.year , date__month = today.month
       ).aggregate(total = Sum("amount"))["total"] or 0 

       return Response ({
           "month" : today.month,
           "total_income" : total_income,
           "total_expense" : total_expense,
           "profit" : total_income - total_expense
       })
