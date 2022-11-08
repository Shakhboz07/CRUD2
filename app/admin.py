from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import Employee


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ['id', 'name', 'status']
    list_filter = ['name', 'age', 'status']
    search_fields = ['name', 'address']
