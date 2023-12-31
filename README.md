# Todo App - Django REST API

Cette API REST Django propose une application de gestion des tâches (Todo) avec des fonctionnalités avancées pour la planification, le suivi et la gestion des tâches. Elle offre une interface conviviale pour les utilisateurs afin d'ajouter, de modifier, de marquer comme complétées, de rechercher et de filtrer les tâches en fonction de divers critères.

## Fonctionnalités Principales

### 1. Ajout et Gestion des Tâches

- **Ajout de Tâches:** Permet aux utilisateurs d'ajouter des tâches avec des détails tels que le nom, la description, la date d'échéance, une image facultative, et le niveau d'importance.
- **Modification de Tâches:** Possibilité de modifier les détails d'une tâche existante.
- **Marquage Complet/Incomplet:** Les utilisateurs peuvent marquer une tâche comme complétée ou non complétée.

### 2. Gestion Automatique du Niveau d'Urgence

- **Niveau d'Importance Dynamique:** Le niveau d'importance des tâches est automatiquement déterminé en fonction de la date d'échéance. Les tâches sont catégorisées comme "Pas Urgent", "Peu Urgent", ou "Très Urgent".

### 3. Recherche et Filtrage

- **Recherche de Tâches:** Les utilisateurs peuvent effectuer des recherches par nom pour trouver rapidement les tâches souhaitées.
- **Filtrage des Tâches:** Possibilité de filtrer les tâches par date d'échéance, nom, niveau d'importance, et statut de complétion.

### 4. Gestion des Tâches Complétées

- **Liste des Tâches Complétées:** Affiche une liste distincte des tâches complétées avec la possibilité de les consulter.

## Installation et Utilisation

1. **Clonez le Répertoire:**
   ```bash
   git clone https://github.com/votre-utilisateur/todo-app.git
   cd todo-app

2. **Installez les Dépendances:**
   ```bash
   pip install -r requirements.txt

3. **Appliquez les Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Lancez le Serveur de Développement:**
   ```bash
   python manage.py runserver
   
L'application sera accessible à l'adresse http://localhost:8000.

## Contributions et Signalement de Problèmes
Les contributions sont les bienvenues! N'hésitez pas à signaler des problèmes ou à proposer des améliorations en ouvrant une nouvelle issue.
