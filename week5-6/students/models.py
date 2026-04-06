from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True)

    def __str__(self):
        return self.full_name