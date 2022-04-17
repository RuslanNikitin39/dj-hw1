from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    # price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exists}; {self.slug}"

