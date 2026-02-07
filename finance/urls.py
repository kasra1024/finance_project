# api
from django.urls import path , include
from finance.views import *
from finance.api import *
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register("all_income" ,IncomeViewset ,basename="all_income")
router.register("all_expense" ,ExpenseViewSet ,basename= "all_expense")
router.register("profit" , IncomeModelViewSet , basename="profit")

urlpatterns = [
    path ('api/all_category/' , CategoryApiView.as_view()),
    path ('api/all_category/<int:pk>/', CategoryApiView.as_view()),
    path ('api/register/' , RegisterApiView.as_view()),
    path ('api/login/' , LoginApiView.as_view()),
    path ('api/logout/' , LogoutApiView.as_view()),
    path ("api/" ,include(router.urls)) 
]
urlpatterns = urlpatterns + router.urls
# ----------------------------------------------------------------------------------------------------
# template
from django.urls import path 
from finance.views_template import *

app_name = "finance"

urlpatterns = [
    path ("tem/categories/list/" , CategoryListView.as_view() , name="list_category"),
    path ("tem/categories/add/" , CategoryCreateView.as_view() , name="create_category"), 
    path ("tem/income/" ,dashboard , name='dashboard') , 
    path ("tem/income/create/" , IncomeCreateView.as_view() , name='income_create'),
    path ("tem/expense/create/" , ExpenseCreateView.as_view() , name='expense_create'),
    path ("tem/profit/" , MonthlyReportView.as_view() , name='profit'),
]