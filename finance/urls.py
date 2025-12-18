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
