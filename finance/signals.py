from django.db.models.signals import post_save
from django.dispatch import receiver
from finance.models import Income

@receiver(post_save , sender=Income)
def income_created(sender , instance , created , **kwargs) : 
    if created : 
        print (f"{instance.fullname} درامد جدیداضافه شد")