from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from django.urls import reverse_lazy
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Sum
from datetime import date


class CategoryListView (View) : 
    html = "finance/category_list.html"
    def get (self , request) : 
        category_list = Category.objects.all()
        print (category_list)
        return render (request , self.html ,{"category_list" : category_list})
# ---------------------------------------------------------------------------------

class CategoryCreateView(View):
    template_name = 'finance/category_form.html'

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:list_category")
        return render(request, self.template_name, {"form": form})
    
# -----------------------------------------------------------------------------------

@login_required
def dashboard(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.filter(user=request.user)

    total_income = sum(i.amount for i in incomes)
    total_expense = sum(e.amount for e in expenses)

    return render(request, 'finance/base.html', {
        'total_income': total_income,
        'total_expense': total_expense,
        'incomes': incomes,
        'expenses': expenses,
    })

# -------------------------------------------------------------------------------------

class IncomeCreateView(LoginRequiredMixin , CreateView) : 
    model = Income
    form_class = IncomeForm
    template_name = 'finance/income_form.html' 
    success_url = reverse_lazy('finance:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# --------------------------------------------------------------------------------------

class ExpenseCreateView(LoginRequiredMixin , CreateView) : 
    model = Expense
    form_class = ExpenseForm
    template_name = 'finance/expense_form.html' 
    success_url = reverse_lazy('finance:dashboard')

    def form_valid(self, form):
        obj = form.save(commit=False) 
        obj.user = self.request.user
        obj.save() 
        return super().form_valid(form)

# ------------------------------------------------------------------------------------------

class MonthlyReportView(LoginRequiredMixin, View):
    def get(self, request):
        today = date.today()
        user = request.user

        
        total_income_dict = Income.objects.filter(
            user=user,
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))

        total_expense_dict = Expense.objects.filter(
            user=user,
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))

        
        total_income = total_income_dict['total'] or 0
        total_expense = total_expense_dict['total'] or 0
        profit = total_income - total_expense

        context = {
            "user": user.username,
            "month": today.month,
            "total_income": total_income,
            "total_expense": total_expense,
            "profit": profit
        }
        return render(request, "finance/profit.html", context)