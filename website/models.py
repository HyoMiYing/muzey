from django.db import models

NACIN_PRIDOBITVE_PREDMETA = [
    ('Dar', 'Dar'),
    ('Odkup', 'Odkup'),
    ('Najdba', 'Najdba'),
    ('Volilo', 'Volilo'),
]

STROKOVNA_KLASIFIKACIJA_CHOICES = [
    ('P01 Orožje', 'P01 Orožje'),
    ('P02 Orodje', 'P02 Orodje'),
    ('P03 Stavbna oprema', 'P03 Stavbna oprema'),
    ('P04 Bivalna oprema', 'P04 Bivalna oprema'),
    ('P05 Oblačila in osebni predmeti', 'P05 Oblačila in osebni predmeti'),
    ('P06 Prometna in transportna sredstva', 'P06 Prometna in transportna sredstva'),
    ('P07 Predmeti za igro in prosti čas', 'P07 Predmeti za igro in prosti čas'),
    ('P08 Umetniški predmeti', 'P08 Umetniški predmeti'),
    ('P09 Predmeti uporabne umetnosti', 'P09 Predmeti uporabne umetnosti'),
    ('P10 Obredni predmeti', 'P10 Obredni predmeti'),
    ('P11 Predmeti komunikacije', 'P11 Predmeti komunikacije'),
    ('P12 Grbi, zastave, nagrade in priznanja', 'P12 Grbi, zastave, nagrade in priznanja'),
    ('P13 Sredstva za trgovino in bančništvo', 'P13 Sredstva za trgovino in bančništvo'),
    ('P14 Predmeti za prikaze in ponazoritve', 'P14 Predmeti za prikaze in ponazoritve'),
    ('P15 Stroji in naprave', 'P15 Stroji in naprave'),
    ('P16 Predmeti izobraževanja, znanosti in tehnike', 'P16 Predmeti izobraževanja, znanosti in tehnike'),
    ('P17 Geološki predmeti', 'P17 Geološki predmeti'),
    ('P18 Botanični predmeti', 'P18 Botanični predmeti'),
    ('P19 Zoološki predmeti', 'P19 Zoološki predmeti'),
    ('P20 Človeški ostanki', 'P20 Človeški ostanki'),
    ('P21 Glasbila', 'P21 Glasbila'),
    ('P22 Drugi predmeti zgodovinskega pomena', 'P22 Drugi predmeti zgodovinskega pomena'),
    ('N01 Arheološka najdišča', 'N01 Arheološka najdišča'),
    ('N02 Stavbe', 'N02 Stavbe'),
    ('N03 Parki in vrtovi', 'N03 Parki in vrtovi'),
    ('N04 Stavbe s parki ali z vrtovi', 'N04 Stavbe s parki ali z vrtovi'),
    ('N05 Spominski objekti in kraji', 'N05 Spominski objekti in kraji'),
    ('N06 Drugi objekti in naprave', 'N06 Drugi objekti in naprave'),
    ('N07 Naselja in njihovi deli', 'N07 Naselja in njihovi deli'),
    ('N08 Kulturna krajina', 'N08 Kulturna krajina'),
    ('N09 Ostalo', 'N09 Ostalo'),
]

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

class Zbirka(models.Model):
    ImeZbirke = models.CharField(max_length=20)
    slika_ki_predstavlja_zbirko = models.ImageField(upload_to="category_pictures")

    def __str__(self):
        return self.ImeZbirke

class Predmet(models.Model):
    Zbirka = models.ForeignKey(Zbirka, on_delete=models.CASCADE)
    NaslovnaSlikaPredmeta = models.ImageField(blank=True, null=True, upload_to="item_pictures")
    edinstvena_inventarna_stevilka_predmeta = models.CharField(max_length=300)
    ImePredmeta = models.CharField(max_length=20)
    strokovna_klasifikacija = models.CharField(max_length=50, choices = STROKOVNA_KLASIFIKACIJA_CHOICES)

    # Opis Predmeta Ki Omogoča Prepoznavanje
    mere_material_in_tehnike = models.TextField(blank=True)
    napisi_in_oznake = models.TextField(blank=True)
    stevilo_delov_ki_sestavlja_predmet = models.IntegerField(blank=True, null=True)
    ime_avtorja_ali_izdelovalca_predmeta = models.CharField(max_length=200, blank=True)
    motiv_naslov_dela_in_signalizacija = models.TextField(blank=True)
    datacija = models.CharField(max_length=100, blank=True)
    ohranjenost_predmeta = models.TextField(blank=True)

    # Podatki O Izvoru Predmeta
    najdisce = models.CharField(max_length=200, blank=True)
    kraj_in_cas_izdelave_predmeta = models.CharField(max_length=300, blank=True)
    kraj_in_cas_uporabe_predmeta = models.CharField(max_length=300, blank=True)
    provenienca_zgodovina_predmeta_do_prihoda_v_muzej = models.TextField(blank=True)

    # Podatki O Pridobitvi Predmeta
    nacin_pridobitve_predmeta = models.CharField(max_length=15, choices=NACIN_PRIDOBITVE_PREDMETA, blank=True)
    ime_pridobitelja_predmeta = models.CharField(max_length=100, blank=True)
    cena_oziroma_ocenjena_vrednost_predmeta = models.CharField(max_length=100, blank=True)
    datum_pridobitve_predmeta = models.CharField(max_length=100, blank=True)

    # Podatki O Inventarizaciji
    ime_odgovorne_osebe = models.CharField(max_length=100, blank=True)
    datum_inventarizacije_predmeta = models.CharField(max_length=100, blank=True)
    reference_in_povezave_s_predhodnimi_dokumentacijskimi_postopki = models.TextField(blank=True)
    nahajalisce_predmeta_v_muzeju = models.TextField(blank=True)

    # Opombe
    opombe = models.TextField(blank=True)

    def __str__(self):
        return self.ImePredmeta

# --->
# Modeli, ki spadajo pod posamezne predmete
# --->

class SlikaVGaleriji(models.Model):
    Predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)
    Slika = models.ImageField(blank=True, null=True, upload_to="item_pictures")

class VideoVGaleriji(models.Model):
    Predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)
    Video = models.FileField(upload_to='videos', null=True, verbose_name="")

# class OpisPredmetaKiOmogocaPrepoznavanje(models.Model):
#     predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)

# class PodatkiOIzvoruPredmeta(models.Model):
#     predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)

# class PodatkiOPridobitviPredmeta(models.Model):
#     predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)

# class PodatkiOInventarizacijiPredmeta(models.Model):
#     predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)

# class Opombe(models.Model):
#     predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)