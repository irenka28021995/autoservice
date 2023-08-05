from django.db import models


class Client(models.Model):
    ClientId = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length=50, verbose_name='Имя')
    ClientPhone = models.CharField(max_length=30, verbose_name='Телефон')
    ClientCar = models.CharField(max_length=100, verbose_name='Автомобиль')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/{self.ClientId}/update'


