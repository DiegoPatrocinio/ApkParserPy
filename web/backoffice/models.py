# -*- encoding=UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class Applications(models.Model):
    package_name = models.CharField(max_length=255)
    app = models.FileField(upload_to='upload', null=True, blank=True)
    package_version = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.package_name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'