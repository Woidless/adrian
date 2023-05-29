from django.db import models


class Currency:
    currency = (
        ('USD', 'dollar'),
        ('KGS', 'som'),
        ('EUR', 'euro'),        
    )


class Tariff(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(choices=Currency.currency)
    description = models.TextField(max_length=200, blank=True, null=True)
    def __sts__(self):
        return self.title