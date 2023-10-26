from django.contrib import admin
from .models import School, Course, Paper , Unit
# Register your models here.

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Paper)