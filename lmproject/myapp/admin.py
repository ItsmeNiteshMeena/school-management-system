from django.contrib import admin
from .models import Student
from .models import Admin
from .models import scheduled
from .models import Query
# Register your models here.

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(scheduled)
admin.site.register(Query)