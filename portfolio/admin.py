from django.contrib import admin
from portfolio.class_Portfolio import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'portfolio_title', 'portfolio_description', 'project')

# Register your models here.
admin.site.register(Portfolio)