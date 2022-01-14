from django.contrib import admin
from core_api import models

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['employee_name', 'email', 'department']
    list_display = ['employee_name', 'email', 'department']
    search_fields = ['employee_name', 'email', 'department']

# Register your models here.
