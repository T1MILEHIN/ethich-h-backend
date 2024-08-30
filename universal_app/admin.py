from django.contrib import admin
from .models import UniversalFormInput

@admin.register(UniversalFormInput)
class UniversalFormInputAdmin(admin.ModelAdmin):
    list_display = ['users', 'field_name', 'field_value', 'unique_link']
    search_fields = ['users__username', 'field_name']

