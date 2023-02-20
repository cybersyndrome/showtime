from django.contrib import admin
from .models import Order, OrderItem
from typing import Sequence, Union, Type, Tuple
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields: Sequence[str] = ['product']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ['id', 'first_name', 'last_name', 
                                   'email', 'address', 'postal_code', 
                                   'city', 'paid', 'created', 'updated']
    list_filter = \
                ['paid', 'created', 'updated']

    inlines = [OrderItemInline]