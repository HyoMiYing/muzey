from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from website.models import *

def home_page(request):
    oopsie_doopsie = Naslov.objects.all()
    variable = Naslov.objects.get(id=len(oopsie_doopsie))
    template = loader.get_template('website/index.html')
    context = {'variable':variable}
    return HttpResponse(template.render(context, request))

def information_page(request):
    oopsie_doopsie = OdpiralniCas.objects.all()
    AktualneInformacije = OdpiralniCas.objects.get(id=len(oopsie_doopsie))
    template = loader.get_template('website/information.html')
    context = {'AktualneInformacije':AktualneInformacije}
    return HttpResponse(template.render(context, request))

def story_page(request):
    oopsie_doopsie = Zgodba.objects.all()
    AktualnoBesediloZgodbe = Zgodba.objects.get(id=len(oopsie_doopsie))
    template = loader.get_template('website/story.html')
    context = {'AktualnoBesediloZgodbe':AktualnoBesediloZgodbe}
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
    VseKategorije = Kategorija.objects.all()
    template = loader.get_template('website/archive.html')
    context = {'VseKategorije':VseKategorije}
    return HttpResponse(template.render(context, request))

def category_page(request, kategorija):
    oopsie_doopsie = Kategorija.objects.get(ImeKategorije=kategorija) #Nevem kako to deluje hahahhahahaaa
    VseStvariVKategoriji = Stvar.objects.filter(Kategorija=oopsie_doopsie)
    template = loader.get_template('website/itecat.html')
    context =  {'VseStvariVKategoriji':VseStvariVKategoriji}
    return HttpResponse(template.render(context, request))

def item_page(request, kategorija, item_id):
    PravaStvar = Stvar.objects.get(id=item_id)
    template = loader.get_template('website/piece.html')
    context = {'PravaStvar':PravaStvar}
    return HttpResponse(template.render(context, request))