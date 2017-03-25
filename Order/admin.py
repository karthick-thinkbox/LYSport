from django.contrib import admin
from .models import Order
class inv_admin(admin.ModelAdmin):
    search_fields=('order_stat','prod_name')
    list_display=('order_id','order_source','prod_name','cost_price')
    list_filter=('order_source',)
    
admin.site.register(Order,inv_admin)

admin.site.site_header = 'LYSportAdmin'