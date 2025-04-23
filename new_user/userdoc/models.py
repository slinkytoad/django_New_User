import datetime
from django.db import models
from django.utils import timezone
    
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_username(self):
        return self.user_name
    def get_cellphone(self):
        return self.cell_phone

    
