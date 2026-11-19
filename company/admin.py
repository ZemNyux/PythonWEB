from django.contrib import admin

from .models import Client, Contract, Department, Employee, Project


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code', 'head_name')
    prepopulated_fields = {'code': ('name',)}
    list_per_page = 10


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email', 'department')
    list_filter = ('department',)
    search_fields = ('full_name', 'email', 'position')
    list_per_page = 10


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'status', 'budget', 'start_date')
    list_filter = ('status',)
    search_fields = ('title', 'code')
    list_per_page = 10


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'country', 'is_active')
    list_filter = ('is_active', 'country')
    search_fields = ('name', 'contact_email')
    list_per_page = 10


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'client', 'amount', 'signed_on')
    list_filter = ('signed_on',)
    search_fields = ('number', 'title', 'client__name')
    list_per_page = 10
