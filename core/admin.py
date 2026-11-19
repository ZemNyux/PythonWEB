from django.contrib import admin

from .models import (
    CompanyPrinciple,
    CompanyStat,
    ContactInquiry,
    ContactLocation,
    ContactOffice,
    NewsArticle,
    ServiceDirection,
    TeamMember,
)


class ContactLocationInline(admin.TabularInline):
    model = ContactLocation
    extra = 1


@admin.register(ContactOffice)
class ContactOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'city', 'sort_order')
    prepopulated_fields = {'code': ('name',)}
    inlines = [ContactLocationInline]


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_on', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'summary')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'sort_order')


@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'sort_order')


@admin.register(ServiceDirection)
class ServiceDirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order')


@admin.register(CompanyPrinciple)
class CompanyPrincipleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order')


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    readonly_fields = ('created_at',)
