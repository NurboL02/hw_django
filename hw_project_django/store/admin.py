from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'choose', 'details_link']
    list_filter = ['choose']
    search_fields = ['title', 'choose']

    def details_link(self, obj):
        link = reverse('product_detail', args=[obj.id])
        return format_html('<a href="{}" target="_blank">Подробнее</a>', link)
    details_link.short_description = 'Подробнее'

admin.site.register(Product, ProductAdmin)

