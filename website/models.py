from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    preferred_location = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)
    current_company = models.CharField(max_length=150, default='DEFAULT VALUE', blank=True, null=True)
    notice_period = models.CharField(max_length=200, default='DEFAULT VALUE', blank=True, null=True)
    last_working_day = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)
    work_mode = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True) 
    profile = models.CharField(max_length=200, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    