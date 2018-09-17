from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.utils.timezone import now


class SuperModel(models.Model):
    subclass_type = models.ForeignKey(
        ContentType, verbose_name=_("Subclass Type"), 
        null=True, blank=True, default=None,
        on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._meta.parents:
            self.subclass_type = ContentType.objects.get_for_model(self)
        super(SuperModel, self).save(*args, **kwargs)

    @cached_property
    def instance(self):
        return self.subclass_type and \
            self.subclass_type.get_object_for_this_type(id=self.id) or self


class Timestamp(models.Model):
    created_at = models.DateTimeField(_('Created At'), default=now) 
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True