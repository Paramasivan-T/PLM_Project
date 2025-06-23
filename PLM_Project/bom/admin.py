from django.contrib import admin
from .models import BOMItem

@admin.register(BOMItem)
class BOMItemAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child', 'quantity')
    list_filter = ('parent',)
    search_fields = ('parent__part_number', 'child__part_number')
