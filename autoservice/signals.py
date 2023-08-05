from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save
from autoservice.models import Client




@receiver(post_save, sender=Client)
def create_user(sender, instance, created, **kwargs):
    if created:
        print(f'Пользователь {instance.ClientName} оставил заявку')
    else:
        print(f'Пользователь {instance.ClientName} изменил заявку')


@receiver(post_delete, sender=Client)
def delete_user(sender, instance, *args, **kwargs):
    print(f'Пользователь {instance.ClientName}  удалил заявку')
