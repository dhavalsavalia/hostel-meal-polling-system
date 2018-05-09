from django import forms
from .models import Choice

QUESTION_CHOICES = (
    ("vada_paw", "Vada Paw"),
    ("paw_bhaji", "Paw Bhaji"),
    ("ghughra", "Ghughra"),
    ("pani_puri", "Pani Puri"),
    ("dal_pakwan", "Dal Pakwan"),
    ("fruit_salad", "Fruit Salad"),
    ("sandwhich", "Sandwhich"),
    ("bhajiya", "Bhajiya"),
    ("punjabi", "Punjabi"),
    ("pizza", "Pizza"),
    ("dabeli", "Dabeli"),
    ("manchurian", "Manchurian"),
)


class ChoiceForm(forms.Form):
    choices = forms.ChoiceField(
        choices=QUESTION_CHOICES, widget=forms.RadioSelect())
