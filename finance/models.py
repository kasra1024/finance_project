from django.db import models
from django.utils import timezone

class Category (models.Model) : 
    name = models.CharField(max_length=128) 
    def __str__(self):
        return self.name

# هر درامد فقط توی ی دسته جا میشه 
class Income(models.Model) : 
    fullname = models.CharField(max_length=64 , default="")
    amount = models.IntegerField() 
    descriptions = models.CharField(max_length=256 , blank=True , null=True) 
    date = models.DateField(default=timezone.now) 
    category = models.ForeignKey(Category , on_delete= models.SET_NULL , null=True , blank=True , related_name="income") 
    def __str__(self):
        return f"{self.fullname} "

# هر هزیت=نه هم توی دسته جا میشه 
class Expense (models.Model) : 
    fullname = models.CharField(max_length=64 , default="")
    amount = models.IntegerField() 
    descriptions = models.CharField(max_length=256 , blank=True , null=True) 
    date = models.DateField(default=timezone.now) 
    category = models.ForeignKey(Category , on_delete= models.SET_NULL , null=True , blank=True , related_name="expense") 
    def __str__(self):
        return f"{self.fullname}"
