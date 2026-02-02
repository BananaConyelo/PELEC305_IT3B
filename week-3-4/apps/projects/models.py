from django.db import models
from django.core.exceptions import ValidationError
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()
    year_level = models.IntegerField()

    def __str__(self):
        return f"{self.student.name}'s Profile"
    
class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    technologies = models.ManyToManyField(Technology)
    is_active = models.BooleanField(default=True)

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError('Project title should be 5 or more characters')
    
    def deactivate(self):
        self.is_active = False
        self.save()
    
    def __str__(self):
        return self.title