from django.forms import ModelForm
from finance.models import Category , Income , Expense

class CategoryForm (ModelForm) : 
    class Meta : 
        model = Category 
        fields = "__all__"

class IncomeForm(ModelForm) : 
    class Meta : 
        model = Income
        fields = "__all__"

class ExpenseForm (ModelForm) : 
    class Meta : 
        model = Expense
        fields = "__all__"