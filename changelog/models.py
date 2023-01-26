from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'


class ChangeLog(models.Model):
    TYPE_ACTION_ON_MODEL = (
        (ACTION_CREATE, _('Create')),
        (ACTION_UPDATE, _('Update')),
        (ACTION_DELETE, _('Delete')),
    )
    changed = models.DateTimeField(auto_now=True, verbose_name=u'Date/time update')
    model = models.CharField(max_length=255, verbose_name=u'Table', null=True)
    record_id = models.IntegerField(verbose_name=u'ID add', null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=u'Author',
        on_delete=models.CASCADE, null=True)
    action_on_model = models.CharField(
        choices=TYPE_ACTION_ON_MODEL, max_length=50, verbose_name=u'Moved', null=True)

    data = models.JSONField(verbose_name=u'Change models', default=dict)
    ipaddress = models.CharField(max_length=15, verbose_name=u'IP adress', null=True)

    class Meta:
        ordering = ('-changed',)
        verbose_name = _('Change log')
        verbose_name_plural = _('Change logs')

    def __str__(self):
        return f'{self.id}'

    @classmethod
    def add(cls, instance, user, ipaddress, action_on_model, data, id=None):
        """Create in journal"""
        log = ChangeLog.objects.get(id=id) if id else ChangeLog()
        log.model = instance.__class__.__name__
        log.record_id = instance.pk
        if user:
            log.user = user
        log.ipaddress = ipaddress
        log.action_on_model = action_on_model
        log.data = data
        log.save()
        return log.pk