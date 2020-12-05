from .models import Animal, Equipement
from django.shortcuts import render, get_object_or_404

def animal_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    animaux = Animal.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animaux': animaux})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animalerie/animal_detail.html', {'animal': animal})