from django.db import models
from apps.users.models import UserProfile


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.quantity} {self.user.name}'