from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Feed(models.Model):
    text = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    total_rate = models.FloatField(null=True)
    number_of_rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey('Feed', on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    class Meta:
        unique_together = ['user', 'feed']


@receiver(post_save, sender=UserRate)
def update_feed_rate(sender, **kwargs):
    instance = kwargs['instance']
    if not kwargs['created']:
        return
    if instance.feed.total_rate is None:
        instance.feed.total_rate = instance.rate
        instance.feed.number_of_rate = 1
    else:
        instance.feed.total_rate += instance.rate
        instance.feed.number_of_rate += 1
    instance.feed.save()
