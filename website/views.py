from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from website.models import *

def home_page(request):
    opsie_dopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(opsie_dopsie))
    oopsie_doopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(oopsie_doopsie))
    VseZbirke = Zbirka.objects.all()
    template = loader.get_template('website/index.html')
    context = {'variable':variable, 'VseZbirke':VseZbirke, 'variable':variable}
    return HttpResponse(template.render(context, request))

def information_page(request):
    opsie_dopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(opsie_dopsie))
    oopsie_doopsie = OdpiralniCas.objects.all()
    AktualneInformacije = OdpiralniCas.objects.get(id=len(oopsie_doopsie))
    template = loader.get_template('website/information.html')
    context = {'AktualneInformacije':AktualneInformacije, 'variable':variable}
    return HttpResponse(template.render(context, request))

def story_page(request):
    opsie_dopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(opsie_dopsie))
    oopsie_doopsie = Zgodba.objects.all()
    AktualnoBesediloZgodbe = Zgodba.objects.get(id=len(oopsie_doopsie))
    template = loader.get_template('website/story.html')
    context = {'AktualnoBesediloZgodbe':AktualnoBesediloZgodbe, 'variable':variable}
    return HttpResponse(template.render(context, request))

def archive_page(request):

    # xxxxx
    # q = Category.objects.get(pk=1)
    # w = q.item_set.all()
    # # p = w[-1]
    # last_element = w.last()
    # Stvar = Item.objects.get(ImeStvari=last_element)
    # print(Stvar)
    # Dodaj stvar v context dictionary.
    # xxxxx
    VseZbirke = Zbirka.objects.all()
    template = loader.get_template('website/archive.html')
    context = {'VseZbirke':VseZbirke}
    return HttpResponse(template.render(context, request))

def category_page(request, zbirka):
    opsie_dopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(opsie_dopsie))
    oopsie_doopsie = Zbirka.objects.get(ImeZbirke=zbirka) #Nevem kako to deluje hahahhahahaaa
    VsiPredmetiVZbirki = Predmet.objects.filter(Zbirka=oopsie_doopsie)
    template = loader.get_template('website/itecat.html')
    context =  {'VsiPredmetiVZbirki':VsiPredmetiVZbirki, 'variable':variable}
    return HttpResponse(template.render(context, request))

def item_page(request, zbirka, item_id):
    opsie_dopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(opsie_dopsie))

    PraviPredmet = Predmet.objects.get(id=item_id)

    opis_predmeta_ki_omogoca_prepoznavanje = [
        PraviPredmet.mere_material_in_tehnike, PraviPredmet.napisi_in_oznake, PraviPredmet.stevilo_delov_ki_sestavlja_predmet, PraviPredmet.ime_avtorja_ali_izdelovalca_predmeta, PraviPredmet.motiv_naslov_dela_in_signalizacija, PraviPredmet.datacija, PraviPredmet.ohranjenost_predmeta, 
        ]

    naslov_za_opis_predmeta_ki_omogoca_prepoznavanje = any(opis_predmeta_ki_omogoca_prepoznavanje)


    podatki_o_izvoru_predmeta = [
        PraviPredmet.najdisce,
        PraviPredmet.kraj_in_cas_izdelave_predmeta,
        PraviPredmet.kraj_in_cas_uporabe_predmeta,
        PraviPredmet.provenienca_zgodovina_predmeta_do_prihoda_v_muzej,
    ]

    naslov_za_podatki_o_izvoru_predmeta = any(podatki_o_izvoru_predmeta)


    podatki_o_pridobitvi_predmeta = [
        PraviPredmet.nacin_pridobitve_predmeta,
        PraviPredmet.ime_pridobitelja_predmeta,
        PraviPredmet.cena_oziroma_ocenjena_vrednost_predmeta,
        PraviPredmet.datum_pridobitve_predmeta,
    ]

    naslov_za_podatki_o_pridobitvi_predmeta = any(podatki_o_pridobitvi_predmeta)


    podatki_o_inventarizaciji = [
        PraviPredmet.ime_odgovorne_osebe,
        PraviPredmet.datum_inventarizacije_predmeta,
        PraviPredmet.reference_in_povezave_s_predhodnimi_dokumentacijskimi_postopki,
        PraviPredmet.nahajalisce_predmeta_v_muzeju,
    ]

    naslov_za_podatki_o_inventarizaciji = any(podatki_o_inventarizaciji)

    opombe = PraviPredmet.opombe

    SlikeVGaleriji = SlikaVGaleriji.objects.filter(Predmet_id=item_id)
    VideiVGaleriji = VideoVGaleriji.objects.filter(Predmet_id=item_id)
    template = loader.get_template('website/piece.html')
    context = {
        'PraviPredmet':PraviPredmet, 
        'SlikeVGaleriji':SlikeVGaleriji, 
        'VideiVGaleriji':VideiVGaleriji,
        'NaslovZaOpisPredmetaKiOmogocaPrepoznavanje':naslov_za_opis_predmeta_ki_omogoca_prepoznavanje, 'NaslovZaPodatkeOIzvoruPredmeta':naslov_za_podatki_o_izvoru_predmeta,
        'NaslovZaPodatkeOPridobitviPredmeta':naslov_za_podatki_o_pridobitvi_predmeta, 
        'NaslovZaPodatkeOInventarizaciji':naslov_za_podatki_o_inventarizaciji,
        'NaslovZaOpombe': opombe,
        'variable':variable,
    }
    return HttpResponse(template.render(context, request))