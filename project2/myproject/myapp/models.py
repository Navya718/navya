from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)  # Consider using IntegerField if appropriate
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
