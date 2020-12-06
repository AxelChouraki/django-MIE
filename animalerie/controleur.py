from . import modele

def nourrir(id_animal):
    if modele.lit_état(id_animal) != 'affamé':
        print("Désolé, "+ id_animal +"n'a pas faim!")
        return "Désolé, "+ id_animal +"n'a pas faim!"
    elif modele.vérifie_disponibilité("mangeoire") == "occupé":
        print("Impossible, la mangeoire est actuellement occupée par " + str(modele.cherche_occupant("mangeoire")))
        return "Impossible, la mangeoire est actuellement occupée par " + str(modele.cherche_occupant("mangeoire"))
    else:
        modele.change_lieu(id_animal,"mangeoire")
        modele.change_état(id_animal,"repus")
        print("Félicitations, " + id_animal + " a rejoint le mangeoire et est maintenant repus.")
        return "Félicitations, " + id_animal + " a rejoint le mangeoire et est maintenant repus."

def divertir(id_animal):
    if modele.vérifie_disponibilité("roue") == "occupé":
        print("Impossible, la roue est actuellement occupée par " + str(modele.cherche_occupant("roue")))
        return "Impossible, la roue est actuellement occupée par " + str(modele.cherche_occupant("roue"))
    if modele.lit_état(id_animal) != "repus":
        print("Désolé, " + id_animal + " n'est pas en état de faire du sport!")
        return "Désolé, " + id_animal + " n'est pas en état de faire du sport!"
    else:
        modele.change_lieu(id_animal, "roue")
        modele.change_état(id_animal, "fatigué")
        print("Félicitations, " + id_animal + " a rejoint la roue et est maintenant fatigué.")
        return "Félicitations, " + id_animal + " a rejoint la roue et est maintenant fatigué."

def coucher(id_animal):
    if modele.vérifie_disponibilité("nid") == "occupé":
        print("Impossible, le nid est actuellement occupée par " + str(modele.cherche_occupant("nid")))
        return "Impossible, le nid est actuellement occupée par " + str(modele.cherche_occupant("nid"))
    if modele.lit_état(id_animal) != "fatigué":
        print("Désolé, " + id_animal + " n'est pas fatigué!")
        return "Désolé, " + id_animal + " n'est pas fatigué!"
    else:
        modele.change_lieu(id_animal, "nid")
        modele.change_état(id_animal, "endormi")
        print("Félicitations, " + id_animal + " a rejoint le nid et est maintenant endormi.")
        return "Félicitations, " + id_animal + " a rejoint le nid et est maintenant endormi."

def réveiller(id_animal):
    if modele.lit_état(id_animal) != "endormi":
        print("Désolé, " + id_animal + " ne dort pas")
        return "Désolé, " + id_animal + " ne dort pas"
    else:
        modele.change_lieu(id_animal, "liti\u00e8re")
        modele.change_état(id_animal, "affamé")
        print("Félicitations, " + id_animal + " a rejoint la litière et est maintenant affamé.")
        return "Félicitations, " + id_animal + " a rejoint la litière et est maintenant affamé."