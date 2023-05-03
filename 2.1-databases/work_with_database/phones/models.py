from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.DecimalField(decimal_places=0, max_digits=6)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)
