from django.db import models

class Order(models.Model):
    order_stat = models.CharField(max_length=10,)
    order_id = models.CharField(max_length=50,unique=True)
    order_source = models.CharField(max_length=50)
    prod_name = models.CharField(max_length=50,)
    prod_url = models.CharField(max_length=500, blank=True, null=True)
    cost_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'
        
    def __str__(self):
        return(self.prod_name)
        