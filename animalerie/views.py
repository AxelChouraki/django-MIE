from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import Animal, Equipement
from django.shortcuts import render, get_object_or_404
from .form import AnimalForm
from . import controleur

def animal_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    animaux = Animal.objects.all()
    msg = gestion_form(request)
    return render(request, 'animalerie/animal_list.html', {'animaux': animaux, "msg": msg})

def animal_list_et_detail(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    msg = gestion_form(request)
    return render(request, 'animalerie/animal_list_et_detail.html', {'animaux': animaux, "equipements": equipements, "msg": msg})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    return render(request, 'animalerie/animal_detail.html', {'animal': animal})

def gestion_form(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():

            action = form.data['action']
            animal = form.data['animal']
            if action == "nourrir":
                msg = controleur.nourrir(animal)
            elif action == "divertir":
                msg = controleur.divertir(animal)
            elif action == "coucher":
                msg = controleur.coucher(animal)
            elif action == "réveiller":
                msg = controleur.réveiller(animal)

            return msg

    else:
        #form = AnimalForm()
        return "test"
