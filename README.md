# TP : API de réservation de salles

> **À compléter par votre groupe avant le dernier push.**

## Groupe

| Membre | Compte GitHub | Rôle / tâches principales |
|--------|---------------|---------------------------|
| Nana Ivana Cindy   | https://github.com/NanaIvana/Reservations.git           | Execute all task                    |

## Installation

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

The API is available at http://127.0.0.1:8000/api/.
Login for the Browsable API: http://127.0.0.1:8000/api-auth/login/

Comptes de test (mot de passe : `motdepasse123`) : `alice`, `bob`, `charlie`.
Super-utilisateur : `admin` / `admin123`.

## Endpoints

> À compléter : listez les routes de votre API, les méthodes autorisées et qui a le droit de les appeler.

| Route | Methods | Permissions |
|-------|---------|----------------|
| `/api/salles/` | GET | Everyone |
| `/api/salles/` | POST | Staff only |
| `/api/salles/{id}/` | GET | Everyone |
| `/api/salles/{id}/` | PUT, PATCH, DELETE | Staff only |
| `/api/salles/{id}/occupation/` | GET | Everyone |
| `/api/reservations/` | GET | Everyone |
| `/api/reservations/{id}/` | GET | Everyone |

## Choix de conception et difficultés rencontrées
-At the level of occupation I was bloacked
-Then for permissions wasn't sure at the level of admin autorisations  

> Quelques lignes : comment avez-vous défini le chevauchement ? Qu'est-ce qui vous a posé problème ?
