from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    second_name = models.CharField(max_length=30, blank=True, verbose_name="Отчество")
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    auth_key = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def get_initials(self):
        try:
            name = self.first_name[0].upper()+"."
            lname = self.second_name[0].upper()+"."
            fname = self.last_name.title()
            initials = fname+' '+name +' '+lname 
        except:
            initials = "No data"
        return initials

    def get_fullname(self):
        name = self.first_name.title()
        lname = self.second_name.title()
        fname = self.last_name.title()
        fullname = fname+' '+name +' '+lname 
        return fullname

    def calculate_age(self):
        today = date.today()
        try:
        	age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        except:
            age = "No data"
        return age