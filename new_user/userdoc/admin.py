from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name', 'cell_phone', 'created_at', 'updated_at', 'slug')
    prepopulated_fields = {'slug': ('user_name',)}

admin.site.register(Employee, EmployeeAdmin)

