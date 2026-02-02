from django.contrib import admin
from .models import Student, StudentProfile, Project, Technology

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Project)
admin.site.register(Technology)
