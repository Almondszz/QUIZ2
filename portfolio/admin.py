from django.contrib import admin
from portfolio.models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

# Register your models here.
admin.site.register(Portfolio)