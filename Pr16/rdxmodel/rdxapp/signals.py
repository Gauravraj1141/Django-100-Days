from django.db.models.signals import post_delete

from django.dispatch import receiver


from .models import Trade1


@receiver(post_delete, sender=Trade1)
def after_delte_trade(sender, instance, **kwargs):
    print(instance.usname)
    print(instance.price)
    print(instance.stockname)

    # when we delete our Trade1 then user will not delete that created this trade1 list so if we want to delte this user when we delete our trade1 with that particular user so we need to send post signal and delete user by our own hand
    # instance.usname.delete()
