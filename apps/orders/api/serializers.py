from rest_framework import serializers
from api.arepas_rest.apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'quantity', 'price_per_unit', 'total_price', 'paid', 'creation_date']