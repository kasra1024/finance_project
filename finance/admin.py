from django.contrib import admin

# Register your models here.

from finance.models import Income ,Expense ,Category

admin.site.register(Income) 
admin.site.register(Expense) 
admin.site.register(Category)