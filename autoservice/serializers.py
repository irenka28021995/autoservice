from rest_framework import serializers

from autoservice.models import Client


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('CustomerId', 'CustomerName', 'CustomerPhone', 'CustomerCar', 'time_create', 'time_update')