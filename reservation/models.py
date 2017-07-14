from django.db import models
from branch.models import Branch

RESERVATION_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)


class Reservation(models.Model):
    branch = models.ForeignKey(Branch)
    date = models.DateField()
    time = models.TimeField()
    persons = models.IntegerField()
    email = models.CharField(max_length=300)
    status = models.CharField(max_length=10,
                              choices=RESERVATION_CHOICES,
                              default='pending')

    def __str__(self):
        return '{} - {} by {}'.format(
            str(self.date), str(self.time), self.email
        )
