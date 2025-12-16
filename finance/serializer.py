from rest_framework import serializers
from finance.models import Category ,Income ,Expense


class CategorySerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Category
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer) : 
    category = serializers.SerializerMethodField()
    class Meta : 
        model = Income
        fields = "__all__" 
    def get_category (self , obj) : 
        return obj.category.name



class ExpenseSerializer(serializers.ModelSerializer) : 
    category = serializers.SerializerMethodField()
    class Meta : 
        model = Expense
        fields = "__all__"
    
    def get_category (self , obj) : 
        return obj.category.name


