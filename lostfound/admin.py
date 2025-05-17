from django.contrib import admin
from .models import LostItem, Profile

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'posted_by', 'created_at', 'found')
    list_filter = ('category', 'found', 'created_at')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number')
    search_fields = ('user__username', 'contact_number')