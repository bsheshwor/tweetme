from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractUser,BaseUserManager)




class MyUserManager(BaseUserManager):
    def create_user(self,email,date_of_birth,password=None):
        if not email:
            raise ValueError('Users must have ann email address')
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

        def create_superuser(self,email,date_of_birth,password = None):
            user = self.create_user(email,password = password,date_of_birth=date_of_birth,)
            user.is_admin = True
            user.save(using = self._db)
            return user
        
class MyUser:
    email = models.EmailField(
        verbose_name = "email address",
        max_length = 255,
        unique = True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj = None):
        """For users specific permission"""
        return True
    
    def has_module_perms(self,app_label):
        """ users --> to have a permission to view the app 'app label' """
        return True
    
    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        """alll admins are staff"""
        return self.is_admin
    


