from django.contrib import admin

from .models import Branch, CompanyFact, HistoryEvent


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'city', 'established', 'sort_order')
    prepopulated_fields = {'slug': ('city',)}
    search_fields = ('name', 'city', 'focus')


@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'sort_order')


@admin.register(CompanyFact)
class CompanyFactAdmin(admin.ModelAdmin):
    list_display = ('badge', 'title', 'sort_order')
