from django.db import models

from branch.models import Branch


class MenuCategory(models.Model):
    branch = models.ForeignKey(Branch)
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to='images', null=True, blank=True,
                             default=None)

    def __str__(self):
        return self.name + ' (' + self.branch.name + ')'

    class Meta:
        verbose_name_plural = 'Menu categories'


class FoodTag(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    category = models.ForeignKey(MenuCategory)
    tags = models.ManyToManyField(FoodTag, blank=True)
    image = models.FileField(upload_to='images', null=True, blank=True,
                             default=None)
    price = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
