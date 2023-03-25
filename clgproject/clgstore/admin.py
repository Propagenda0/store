from django.contrib import admin

from . models import college
from . models import teacher
# Register your models here.

admin.site.register(college)
admin.site.register(teacher)