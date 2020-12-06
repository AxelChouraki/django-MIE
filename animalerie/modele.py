from .models import Animal, Equipement

liste_états = ['affamé', 'fatigué', 'repus', 'endormi']


def lit_état(animal_id):
    try:
        return Animal.objects.get(id_animal = animal_id).etat
    except:
        print('Désolé, ' + animal_id + ' n\'est pas un animal connu')
        print("Exception reçue")
        return None


def lit_lieu(animal_id):
    try:
        return Animal.objects.get(id_animal = animal_id).lieu.id_equip
    except:
        print('Désolé, ' + animal_id + ' n\'est pas un animal connu')
        print("Exception reçue")
        return None


def vérifie_disponibilité(équipement_id):
    try:
        return Equipement.objects.get(id_equip = équipement_id).disponibilite
    except:
        print('Désolé, ' + équipement_id + ' n\'est pas un équipement connu')
        print("Exception reçue")
        return None


def cherche_occupant(lieu):
    if(lieu != "litière"):
        try:
            return Animal.objects.get(lieu = lieu)

        except:
            print("Exception reçue")
            return None
    else:
        return None



def change_état(id_animal, état):
    try:
        if état != 'affamé' and état != 'fatigué' and état != 'repus' and état != 'endormi':
            print('Seuls les états affamé, fatigué, repus, endormi sont autorisés.')
            return None
        else:
            animal = Animal.objects.get(id_animal=id_animal)
            animal.etat = état
            animal.save()
    except:
        print("Exception reçue")
        return None


def change_lieu(id_animal, lieu):
    animal = Animal.objects.get(id_animal=id_animal)
    equipement = Equipement.objects.get(id_equip = lieu)

    try:
        if lieu != "liti\u00e8re" and lieu != "mangeoire" and lieu != "roue" and lieu != "nid":
            print("Ce lieu n'existe pas")
            return None
        elif equipement.disponibilite == "libre" or lieu == "liti\u00e8re":  # le changement de lieu se fait ici

            # changement état de l'ancien lieu
            animal.lieu.disponibilite = "libre"
            animal.lieu.save()

            # changement état du nouveau lieu
            if lieu == "liti\u00e8re":
                equipement.disponibilite = "libre"
            else:
                equipement.disponibilite = "occup\u00e9"
            equipement.save()

            # changement lieu de l'animal
            animal.lieu = equipement
            animal.save()


        else:
            print('Lieu occupé')
            return None
    except:
        print("Exception reçue")
        return None
