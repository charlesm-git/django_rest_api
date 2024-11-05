# Django API REST
Ce repository contient l'ensemble des fichiers nécessaire à l'installation en local d'une API REST Django. Cette API permet la gestion de données de projets (project, issues, commentaires).
## Installation
Afin de pouvoir faire fonctionner cette API en local, veuillez suivre les instructions suivantes :
### Téléchargement
* Télécharger l'ensemble des fichiers présent sur le répository
* Placer les dans le dossier qui vous servira de dossier principal pour votre projet
### Installation de Python
Cette API est codé en Python, vous avez donc besoin d'avoir Python installé sur votre machine pour le faire fonctionner. L'utilisation de Python 3.13 est recommandée. Si ce n'est pas déjà fait, vous pouvez vous rendre sur le site officiel de Python pour le télécharger.
### Installation des packages nécessaire
Pour le bon fonctionnement de l'API, un certain nombre de bibliothèques sont nécessaires.
Pour cela :
* Ouvrir la console et se rendre dans le dossier principal du projet
* Créer un environnement python avec la commande : `python -m venv .venv`.

La gestion des dépendances est réalisé avec l'outil Poetry. Pour l'installer, veuillez vous rendre sur le site officiel de Poetry.
Une fois installé, vous devez :
* Activer l'environnement python avec la commande : `poetry shell`
* Installer les dépendences nécessaires avec la commande : `poetry install`
### Lancement du serveur local
Vous avez maintenant installé tout ce qui est nécessaire pour le bon fonctionnement de l'API. Pour lancer le serveur local, via le terminal rendez-vous dans le dossier principal du projet et lancer la commande : `python .\django_api_rest\manage.py runserver`.

Vous pouvez maintenant utiliser l'API en local grace à un outil tel que Postman.
## Comptes de test
### Comptes utilisateurs
Des comptes de test ont été créé pour que vous puissiez découvrir l'API. Ces derniers ont pour username :
* Charles
* Kylian
* Lucie
Le mot de passe est identique pour tous les comptes : `123456`
### Compte admin
Un compte admin permettant d'accéder au panneau d'administration a été créé :
* Username : admin
* password : admin
Vous pouvez simplement accéder à l'adresse `http://127.0.0.1:8000/admin/` sur votre navigateur pour y accéder
## Endpoint de l'API
Un certain nombre de endpoint vont vous permettre d'utiliser l'API. 
Attention, tous les endpoints nécessitent une authentification. Vous devez donc faire une demande de JSON Web Token après de l'API et renseigner le token d'accès dans l'ensemble de vos requêtes.

Demande de token : 
requête POST sur l'endpoint `/api/token/` en renseignant un username et un password.

Endpoint principaux :
* `/api/projects/` : permet d'accéder à la liste des projects auquel l'utilisateur a accès et à créer un projet.
* `/api/projects/<int>` : permet d'accéder à la vue détail d'un projet, faire une modification ou supprimer un projet.
* `/api/issues/` : permet d'accéder à la liste des issues auquel l'utilisateur a accès et à créer une issue.
* `/api/issues/<int>` : permet d'accéder à la vue détail d'une issue, faire une modification ou supprimer une issue.
* `/api/comments/` : permet d'accéder à la liste de commentaire auquel l'utilisateur a accès et à créer un commentaire.
* `/api/comments/<int>` : permet d'accéder à la vue détail d'un commentaire, faire une motification ou supprimer un commendaire.
* `/api/contributors/` : permet d'accéder à la liste des contributeurs auquel l'utilisateur a accès et à créer un contributeur.
* `/api/contributors/<int>` : permet faire une motification ou supprimer un contributeur.


* `/api/users/` : permet d'accéder à la liste des utilisateurs (uniquement via un compte admin)
* `/api/users/<int>` : permet d'accéder au détail, modifié ou supprimer un utilisateur (uniquement par un compte admin ou par l'utilisateur lui-même)

A noter :

Les utililisateurs n'ont accès qu'aux projets (et contenus de projets) auxquels ils sont contributeurs. De plus, seul l'auteur d'un post peut le modifier ou le supprimer.

Seul un utilisateur déjà contributeur d'un projet peut ajouter/supprimer/modifier d'autres contributeurs.