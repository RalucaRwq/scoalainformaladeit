from django.db import models

# Create your models here.


class Job(models.Model):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE)
    active = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} {self.url} {self.description} {self.customer} {self.active}"
