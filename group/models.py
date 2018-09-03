from django.db import models
from set.models import Set

class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    set     = models.ManyToManyField(Set, related_name="set_members", blank=True)

    def __str__(self):
            return self.id

    class Meta:
        ordering = ('created',)