from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Validator, ValidationError
from pprint import pprint
import pickle
from Classes import Task, methods, data

print("Bonjour, bienvenue sur votre todo-list")

questions = [
    {
        'type': 'checkbox',
        'message': 'Que desirez-vous faire? Attention, une seule chose à la fois',
        'name': 'action',
        'choices': [
            {
                'name': 'Help',
                'value': 0
            },
            {
                'name': 'Créer une tache',
                'value': 1
            },
            {
                'name': 'Supprimer une tache',
                'value': 2
            },
            {
                'name': 'modifier une tache',
                'value': 3
            },
            {
                'name': 'Lister les taches',
                'value': 4
            },
        ]
    }
]
answers = prompt(questions, style = data.style())

if len(answers["action"]) == 0:
    raise ValueError("Vous n'avez rien séléctionné, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

elif len(answers["action"]) != 1:
    raise ValueError("Attention, veuillez ne selectionner qu'une action à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")

if answers["action"][0] == 0:
    f = open("Help.txt", "r")
    help = f.read()
    print(help)

elif answers["action"][0] == 1:
    methods.create_task()

elif answers["action"][0] == 2:
    methods.delete_task()

elif answers["action"][0] == 3:
    methods.modify_task()

elif answers["action"][0] == 4:
    methods.list_task()


