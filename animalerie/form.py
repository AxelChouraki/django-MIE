from django import forms

animal_choice = ["Tic", "Tac", "Patrick", "Totoro", "Pocahontas"]
action_choice = ["nourrir", "divertir", "coucher", "réveiller"]

class AnimalForm(forms.Form):
    animal = forms.CharField(label='animal', widget=forms.RadioSelect(choices=animal_choice))
    action = forms.CharField(label='action', widget=forms.RadioSelect(choices=action_choice))
