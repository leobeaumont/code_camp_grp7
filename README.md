# README du Codecamp GR7

Le but du codecamp est la production d’un logiciel simple de gestion de tâches.

## Fonctionnalités principales

Le point de départ est commun à tous les groupes et consiste à réaliser les commandes suivantes :

- **Ajout, modification et suppression de tâches.**
   - Une tâche possède une description (texte sans retour chariot) et un identifiant attribué à sa création.
   - Il est nécessaire de fournir un moyen de voir la liste des tâches.

## Interaction utilisateur

L’interaction avec l’utilisateur doit rester simple ; nous optons pour une interface en ligne de commande (CLI – Command Line Interface).

À chaque exécution, le programme reçoit en paramètre un nom de fichier contenant les tâches existantes. Le résultat de l’exécution modifie généralement le contenu de ce fichier.

Vous êtes libres du choix du format du fichier, mais il est recommandé de rester simple (par exemple, un format texte avec une ligne par tâche).

## Commandes à implémenter

Supposons que votre programme s’appelle `task` :

- `task lestaches.txt add <description>`  
   Ajoute au fichier `lestaches.txt` une nouvelle tâche et retourne son identifiant.

- `task lestaches.txt modify id <nouvelle description>`  
   Remplace la description de la tâche d’identifiant `id` dans `lestaches.txt`. Renvoie un message d’erreur si la tâche n’est pas trouvée.

- `task lestaches.txt rm id`  
   Retire la tâche d’identifiant `id` du fichier `lestaches.txt`. Renvoie un message d’erreur si la tâche n’est pas trouvée.

- `task lestaches.txt show`  
   Affiche la liste des tâches du fichier, triées par identifiant, sous la forme suivante :

   ```
   [id] description owner
   ```


