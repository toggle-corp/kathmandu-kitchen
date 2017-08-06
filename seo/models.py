from django.db import models


class MetaInformation(models.Model):
    meta_description = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.meta_description


class MetaKeyword(models.Model):
    information = models.ForeignKey(MetaInformation)
    keyword = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.keyword
