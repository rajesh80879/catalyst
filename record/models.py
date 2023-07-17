from django.db import models

# Create your models here.

class Record(models.Model):

    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField()

    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)

    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255,default=None)
    country = models.CharField(max_length=255)
    
    linkedin_url = models.URLField()
    current_employees = models.PositiveIntegerField()
    total_employees = models.PositiveIntegerField()

    def __str__(self):
        return self.name