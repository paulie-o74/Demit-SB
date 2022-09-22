from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Contact admin class
    """
    list_display = ['contact_date', 'id', 'email']
    list_filter = ('email', 'contact_date')
    ordering = ('-contact_date',)


admin.site.register(Contact, ContactAdmin)
