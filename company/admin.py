from django.contrib import admin
from .models import Company
from unit.models import Unit

class UnitInline(admin.TabularInline):
    model = Unit

class CompanyAdmin(admin.ModelAdmin):
    inlines = [UnitInline]

admin.site.register(Company, CompanyAdmin)