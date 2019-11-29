from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class T(models.Model):
    username = models.CharField('Username', max_length=200, blank=False)
    tname = models.CharField('Task Name', max_length=200)
    des = models.CharField('Description', max_length=200)


    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return  reverse('t_edit', kwargs={'pk': self.pk})
