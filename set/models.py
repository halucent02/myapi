from django.db import models
from item.models import Item

class Set(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    item   = models.ManyToManyField(Item, related_name="item_members", blank=True)

    def __str__(self):
            return  '{}'.format(self.id)

    class Meta:
        ordering = ('created',)
