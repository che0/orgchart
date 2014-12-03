from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class DummyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=email)
        user.save(self._db)
        return user
    
    def create_superuser(self, email, password):
        return self.create_user(email)

class DummyUser(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    
    objects = DummyUserManager()
    
    @property
    def is_staff(self):
        return True
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return app_label != 'default'
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
