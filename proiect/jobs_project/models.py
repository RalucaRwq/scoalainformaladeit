from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=100)  # column from the database
    url = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE)
    active = models.IntegerField(default=1)


