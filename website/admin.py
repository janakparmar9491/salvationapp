from django.contrib import admin
from .models import ContactForm

# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'subject',
                    'message'
                    ]
    list_display_links = ['name']
    list_filter = [
        'name',
        'email'
    ]
    search_fields = [
        'name',
        'email'
    ]

admin.site.register(ContactForm, ContactFormAdmin)
