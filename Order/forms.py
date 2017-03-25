from django import forms
from django.forms import ModelForm
from .models import Order

class new_ord(ModelForm):
    class Meta:
        model=Order
        fields=['order_id','order_stat','order_source','prod_name','prod_url','cost_price']
        labels={
               
               'order_id': 'Order#',
               'order_stat': 'Status',
               'order_source': 'Source',
               'prod_name':'Name',
               'prod_url':'Link',
               'cost_price':'Cost',
               }
               
        def __init__(self,*args,**kwargs):
            
            super(new_ord,self).__init__(*args,**kwargs)
            self.fields['order_id'].required=True
            self.fields['order_stat'].required=True
            self.fields['order_source'].required=True
            self.fields['prod_name'].required=True
            self.fields['cost_price'].required=True
        