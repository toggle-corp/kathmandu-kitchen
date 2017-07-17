from django.db import models
from branch.models import Branch

RESERVATION_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)


class Reservation(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=300)

    special_request = models.TextField(blank=True, default='')

    branch = models.ForeignKey(Branch)
    date = models.DateField()
    time = models.TimeField()
    persons = models.IntegerField()
    status = models.CharField(max_length=10,
                              choices=RESERVATION_CHOICES,
                              default='pending')

    def __str__(self):
        return '{} - {} by {}'.format(
            str(self.date), str(self.time), self.email
        )
