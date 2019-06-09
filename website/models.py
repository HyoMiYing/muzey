from django.db import models

class Naslov(models.Model):
    naslov = models.CharField(max_length=20)

    def __str__(self):
        return self.naslov

class Zgodba(models.Model):
    zgodba = models.TextField()

class OdpiralniCas(models.Model):
    teden = models.CharField(max_length=20)
    vikend = models.CharField(max_length=20)
    lokacija = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Kategorija(models.Model):
    ImeKategorije = models.CharField(max_length=20)

    def __str__(self):
        return self.ImeKategorije

class Stvar(models.Model):
    Kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    SlikaStvari = models.ImageField(blank=True, null=True, upload_to="item_pictures")
    ImeStvari = models.CharField(max_length=20)
    OpisStvari = models.TextField()

    def __str__(self):
        return self.ImeStvari