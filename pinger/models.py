from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseCheck(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    url_address = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True

    def clean(self):
        if self.ip_address == '' and self.url_address == '':
            raise ValidationError(_('An IP Address or an URL Address must be provided.'))
        if self.ip_address != '' and self.url_address != '':
            raise ValidationError(_('Provide only an IP Address or only an URL Address.'))

    def __unicode__(self):
        return self.name


class PingCheck(BaseCheck):
    pass


class ResponseCheck(BaseCheck):
    string_to_find = models.CharField(max_length=255)
