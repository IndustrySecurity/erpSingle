from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AnonymousUser

def get_anonymous_user_instance(User):
    # Create an instance of your CustomUser
    anon_user = User()
    # Set up attributes for the anonymous user
    # Example: Set a username or any required fields
    anon_user.username = 'AnonymousUser'
    # anon_user.is_anonymous = True
    anon_user.is_active = False
    
    # Set other fields to desired default values
    # ...

    return anon_user

class CustomUser(AbstractUser):
    department = models.CharField(max_length=100, verbose_name="部门")
    position = models.CharField(max_length=100, verbose_name="职位")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
