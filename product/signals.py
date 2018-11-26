from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from product.models import OrderBarang


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=OrderBarang)
@receiver(post_delete, sender=OrderBarang)
def update_totalbelanja(sender, instance=None, **kwargs):
    instance.order.save()
