from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    admin_email = models.CharField(max_length=300)
    map_tag = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Branches'
