from django.db import models

DAYS_OF_THE_WEEK = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
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
            self.branch.name, str(self.start_time), str(self.end_Time))

    class Meta:
        ordering = ['day']
        unique_together = ('day', 'branch')
