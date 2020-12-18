from PyInquirer import style_from_dict, Token, prompt
from pprint import pprint
import pickle

class Task:
    def __init__(self, list):
        self.nom = list[0]
        self.description = list[1]
        self.date_init = list[2]
        self.date_fin = list[3]
        self.status = list[4]
        self.avancement = list[5]
        self.priority = list[6]
        self.comments = list[7]
        self.sub_tasks = list[8]
        self.liste = list


class methods:
    @staticmethod
    def create_task():
        questions = [
            {
                'type': 'input',
                'message': 'Comment voulez-vous nommer cette Tâche?',
                'name': 'nom'
            },
            {
                'type': 'input',
                'message': 'Une petite description?',
                'name': 'description'
            },
            {
                'type': 'input',
                'message': 'Date de début?',
                'name': 'date_init'
            },
            {
                'type': 'input',
                'message': 'Date de fin?',
                'name': 'date_fin'
            },
            {
                'type': 'checkbox',
                'message': 'Status (Ouverte, Fermée, En Progression)?',
                'name': 'status',
                'choices': [
                    {
                        'name': 'Ouverte',
                        'value': 'Open'
                    },
                    {
                        'name': 'Fermée',
                        'value': 'Closed'
                    },
                    {
                        'name': 'En Progression',
                        'value': 'In Progress'
                    },
                ]
            },
            {
                'type': 'input',
                'message': 'Avancement?',
                'name': 'avancement'
            },
            {
                'type': 'checkbox',
                'message': 'Quelle est la priorité de cette tache? (Normale, Urgente, Non-Prioritaire',
                'name': 'priority',
                'choices': [
                    {
                        'name': 'Normale',
                        'value': 'Normale'
                    },
                    {
                        'name': 'Urgente',
                        'value': 'Urgente'
                    },
                    {
                        'name': 'Non-Prioritaire',
                        'value': 'Non-Prioritaire'
                    },
                ]
            }
        ]
        answers = prompt(questions, style = data.style())
        if len(answers["status"]) == 0:
            raise ValueError("Vous n'avez pas séléctionné de status, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

        elif len(answers["status"]) != 1:
            raise ValueError("Attention, veuillez ne selectionner qu'un status, veuillez recommencer en selectionnant une seule action avec <espace>")

        if len(answers["priority"]) == 0:
            raise ValueError("Vous n'avez pas séléctionné de priorité, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

        elif len(answers["priority"]) != 1:
            raise ValueError("Attention, veuillez ne selectionner qu'une priorité à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")
        L = []
        L.append(answers["nom"])
        L.append(answers["description"])
        L.append(answers["date_init"])
        L.append(answers["date_fin"])
        L.append(answers["status"][0])
        L.append(answers["avancement"])
        L.append(answers["priority"][0])
        L.append([])
        L.append([])
        print(L)
        with open ('Taches.txt', 'rb') as fp:
            try:
                liste_taches = pickle.load(fp)
            except EOFError:
                liste_taches = []
        liste_taches.append(L)
        with open('Taches.txt', 'wb') as fp:
            pickle.dump(liste_taches, fp)
        print("Tache ajoutée avec succès")
        
    @staticmethod
    def delete_task():
        questions = [
            {
                'type': 'input',
                'message': 'Quel est le nom de la tache à supprimer?',
                'name': 'nom'
            }
        ]
        answers = prompt(questions, style = data.style())
        nom = answers["nom"]
        print(nom)
        with open ('Taches.txt', 'rb') as fp:
            try:
                liste_taches = pickle.load(fp)
            except EOFError:
                print("Attention, aucune tache n'est enregistrée")
                exit()
        count = 0
        if len(liste_taches) == 0:
            print("Attention, aucune tache n'est enregistrée pour l'instant")
            exit()  
        for i in range(len(liste_taches)):
            if liste_taches[i][0] == nom:
                liste_taches.pop(i)
                count += 1
        if count == 0:
            raise ValueError("Aucune tache ne porte ce nom, verifiez l'orthographe")
        else:
            with open('Taches.txt', 'wb') as fp:
                pickle.dump(liste_taches, fp)
            print("Tache supprimée avec succès")
         
    @staticmethod
    def list_task():
        question = [
            {
                'type': 'checkbox',
                'message': "Voulez vous lister les taches d'une priorité particulière?",
                'name': 'priority',
                'choices': [
                    {
                        'name': 'Normale',
                        'value': 'Normale'
                    },
                    {
                        'name': 'Prioritaire',
                        'value': 'Prioritaire'
                    },
                    {
                        'name': 'Non-Prioritaire',
                        'value': 'Non-Prioritaire'
                    },
                    {
                        'name': 'Toutes les taches',
                        'value': 'All'
                    }
                ]
            }
        ]
        answers = prompt(question, style = data.style())
    
        if len(answers["priority"]) == 0:
            raise ValueError("Vous n'avez pas séléctionné de priorité, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

        elif len(answers["priority"]) != 1:
            raise ValueError("Attention, veuillez ne selectionner qu'une priorité à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")
        
        prio = answers["priority"][0]
        with open ('Taches.txt', 'rb') as fp:
            try:
                liste_taches = pickle.load(fp)
            except EOFError:
                print("Aucune tache n'est enregistrée")

        print("Voici les taches enregistrées correspondantes:")
        for u in liste_taches:
            if u[6] == prio or prio == 'All':
                print(u)
        
    @staticmethod
    def modify_task():
        questions = [
            {
                'type': 'checkbox',
                'message': 'Que desirez-vous modifier? Attention, une seule chose à la fois',
                'name': 'action',
                'choices': [
                    {
                        'name': "Modifier l'avancement d'une tache",
                        'value': 1
                    },
                    {
                        'name': "Modifier la priorité d'une tache",
                        'value': 2
                    },
                    {
                        'name': 'Ajouter un commentaire à une tache',
                        'value': 3
                    },
                    {
                        'name': 'Ajouter une sous-tache à une tache',
                        'value': 4
                    },
                ]
            },
            {
                'type': 'input',
                'message': 'Quel est le nom de la tache à modifier?',
                'name': 'nom'
            }
        ]
        answers = prompt(questions, style = data.style())

        if len(answers["action"]) == 0:
            raise ValueError("Vous n'avez rien séléctionné, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

        elif len(answers["action"]) != 1:
            raise ValueError("Attention, veuillez ne selectionner qu'une action à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")

        nom = answers["nom"]
        with open ('Taches.txt', 'rb') as fp:
            try:
                liste_taches = pickle.load(fp)
            except EOFError:
                print("Attention, aucune tache n'est enregistrée")
                exit()
    
        if len(liste_taches) == 0:
            print("Attention, aucune tache n'est enregistrée pour l'instant")
            exit()  
        
        if answers["action"][0] == 1:
            q = [
                {
                'type': 'input',
                'message': "Quelle est la nouvelle valeur d'avancement?",
                'name': 'avancement'
                }
            ]
            a = prompt(q, style = data.style())
            avancement = a["avancement"]
            count = 0
            for i in range(len(liste_taches)):
                if liste_taches[i][0] == nom:
                    liste_taches[i][5] = avancement
                    count += 1
            if count == 0:
                raise ValueError("Aucune tache ne porte ce nom, verifiez l'orthographe")
            else:
                with open('Taches.txt', 'wb') as fp:
                    pickle.dump(liste_taches, fp)
                print("Avancement modifié avec succès")
        
        elif answers["action"][0] == 2:
            q = [
                {
                    'type': 'checkbox',
                    'message': 'Quelle est la nouvelle priorité de cette tache? (Normale, Urgente, Non-Prioritaire',
                    'name': 'priority',
                    'choices': [
                        {
                            'name': 'Normale',
                            'value': 'Normale'
                        },
                        {
                            'name': 'Urgente',
                            'value': 'Urgente'
                        },
                        {
                            'name': 'Non-Prioritaire',
                            'value': 'Non-Prioritaire'
                        }
                    ]
                }
            ]
            a = prompt(q, style = data.style())
            if len(a["priority"]) == 0:
                raise ValueError("Vous n'avez pas séléctionné de priorité, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

            elif len(a["priority"]) != 1:
                raise ValueError("Attention, veuillez ne selectionner qu'une priorité à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")
            prio = a["priority"]
            count = 0
            for i in range(len(liste_taches)):
                if liste_taches[i][0] == nom:
                    liste_taches[i][6] = prio
                    count += 1
            if count == 0:
                raise ValueError("Aucune tache ne porte ce nom, verifiez l'orthographe")
            else:
                with open('Taches.txt', 'wb') as fp:
                    pickle.dump(liste_taches, fp)
                print("Priorité modifiée avec succès")

        elif answers["action"][0] == 3:
            q = [
                {
                    'type': 'input',
                    'message': 'Tapez votre commentaire',
                    'name': 'com'
                }
            ]
            a = prompt(q, style = data.style())
            com = a["com"]
            count = 0
            for i in range(len(liste_taches)):
                if liste_taches[i][0] == nom:
                    liste_taches[i][7].append(com)
                    count += 1
            if count == 0:
                raise ValueError("Aucune tache ne porte ce nom, verifiez l'orthographe")
            else:
                with open('Taches.txt', 'wb') as fp:
                    pickle.dump(liste_taches, fp)
                print("Commentaire ajouté avec succès")

        elif answers["action"][0] == 4:
            questions2 = [
                {
                    'type': 'input',
                    'message': 'Comment voulez-vous nommer cette sous-tâche?',
                    'name': 'nom'
                },
                {
                    'type': 'input',
                    'message': 'Une petite description?',
                    'name': 'description'
                },
                {
                    'type': 'input',
                    'message': 'Date de début?',
                    'name': 'date_init'
                },
                {
                    'type': 'input',
                    'message': 'Date de fin?',
                    'name': 'date_fin'
                },
                {
                    'type': 'checkbox',
                    'message': 'Status (Ouverte, Fermée, En Progression)?',
                    'name': 'status',
                    'choices': [
                        {
                            'name': 'Ouverte',
                            'value': 'Open'
                        },
                        {
                            'name': 'Fermée',
                            'value': 'Closed'
                        },
                        {
                            'name': 'En Progression',
                            'value': 'In Progress'
                        },
                    ]
                },
                {
                    'type': 'input',
                    'message': 'Avancement?',
                    'name': 'avancement'
                },
                {
                    'type': 'checkbox',
                    'message': 'Quelle est la priorité de cette tache? (Normale, Urgente, Non-Prioritaire',
                    'name': 'priority',
                    'choices': [
                        {
                            'name': 'Normale',
                            'value': 'Normale'
                        },
                        {
                            'name': 'Urgente',
                            'value': 'Urgente'
                        },
                        {
                            'name': 'Non-Prioritaire',
                            'value': 'Non-Prioritaire'
                        },
                    ]
                }
            ]
            a = prompt(questions2, style = data.style())
            if len(a["status"]) == 0:
                raise ValueError("Vous n'avez pas séléctionné de status, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

            elif len(a["status"]) != 1:
                raise ValueError("Attention, veuillez ne selectionner qu'un status, veuillez recommencer en selectionnant une seule action avec <espace>")

            if len(a["priority"]) == 0:
                raise ValueError("Vous n'avez pas séléctionné de priorité, veuillez recommencer en selectionnant ce que vous desirez faire avec <espace>")

            elif len(a["priority"]) != 1:
                raise ValueError("Attention, veuillez ne selectionner qu'une priorité à la fois, veuillez recommencer en selectionnant une seule action avec <espace>")
            sub = []
            sub.append(a["nom"])
            sub.append(a["description"])
            sub.append(a["date_init"])
            sub.append(a["date_fin"])
            sub.append(a["status"][0])
            sub.append(a["avancement"])
            sub.append(a["priority"][0])
            print(sub)
            count = 0
            for i in range(len(liste_taches)):
                if liste_taches[i][0] == nom:
                    liste_taches[i][8].append(sub)
                    count += 1
            if count == 0:
                raise ValueError("Aucune tache ne porte ce nom, verifiez l'orthographe")
            else:
                with open('Taches.txt', 'wb') as fp:
                    pickle.dump(liste_taches, fp)
                print("Sous-tache ajouté avec succès")
            
            
            

class data:
    @staticmethod
    def style():
        style = style_from_dict({
        Token.Answer: '#f44336 bold',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Question: '',
        })
        return style


