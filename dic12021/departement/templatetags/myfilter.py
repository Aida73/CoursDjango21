from django import template

register = template.Library()

@register.filter(name="prenom_nom")

def prenom_nom(value: str):
    prenom, nom = value.split(" ")

    return f"Prenom: {prenom} Nom: {nom}"