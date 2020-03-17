from django.db import models
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


"""Writing user authentication backend"""
class SettingsBackend(BaseBackend):

    def authenticate(self, request, username = None, password= None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password,settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                user = User(username = username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None

"""Handling authorization in custom backends"""
class MagicAdminBackend(BaseBackend):
    def has_perm(self,user_obj,perm,obj=None):
        return user_obj.username == settings.ADMIN_LOGIN



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length = 100)


