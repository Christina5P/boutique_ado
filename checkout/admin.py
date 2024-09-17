from django.contrib import admin
from . models import Order,  OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
    )

fields = ('order-Date', 'date', 'full_name', 'email', 'phone_number','delivery_cost', 'order_total', 'grand_total')

list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost', 'grand_total')

ordering = ('date',)

admin.site.register(Order, OrderAdmin)