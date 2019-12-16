from django.db import models

# Create your models here.


class Products(models.Model):
    Homme = "Homme"
    Femme = "Femme"
    Unisex = "Unisex"

    gender_choice = [
        (Homme, "Homme"),
        (Femme, "Femme"),
        (Unisex, "Unisex"),
    ]
    name = models.CharField(max_length=100)
    old_price = models.IntegerField(blank=True, null=True, default=None)
    price = models.IntegerField()
    picture = models.ImageField(blank=True, upload_to="static/images/bdd/")
    gender = models.CharField(choices=gender_choice, max_length=7, default="Unisex")
    description = models.CharField(blank=True, max_length=600, default="Pas de description actuellement")
    stars = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Produit"
        ordering = ['name']

    def __str__(self):
        return self.name

