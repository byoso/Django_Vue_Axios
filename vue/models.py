from django.db import models

class Poulet(models.Model):
    nom = models.CharField(max_length=31, verbose_name="Nom", unique=True, null=False)
    poids = models.FloatField(verbose_name="poids", null=True, blank=True)

    def __str__(self):
        return self.nom
