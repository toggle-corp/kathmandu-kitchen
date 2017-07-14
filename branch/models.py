from django.db import models
from django.utils.translation import ugettext_lazy as _


DAYS_OF_THE_WEEK = (
    (1, _('Monday')),
    (2, _('Tuesday')),
    (3, _('Wednesday')),
    (4, _('Thursday')),
    (5, _('Friday')),
    (6, _('Saturday')),
    (7, _('Sunday')),
)


class Branch(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=100, blank=True)
    admin_email = models.CharField(max_length=300)

    address = models.TextField(blank=True)
    map_tag = models.TextField(blank=True)

    facebook = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Branches'


class OpeningHour(models.Model):
    branch = models.ForeignKey(Branch)
    day = models.IntegerField(choices=DAYS_OF_THE_WEEK)
    start_time = models.TimeField(default=None, blank=True, null=True)
    end_time = models.TimeField(default=None, blank=True, null=True)
    remarks = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return '{} ({} - {})'.format(
            self.branch.name, str(self.start_time), str(self.end_time))

    class Meta:
        ordering = ['day']
        unique_together = ('day', 'branch')
