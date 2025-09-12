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

- `task lestaches.txt add <description> [-o owner]`
   Ajoute au fichier `lestaches.txt` une nouvelle tâche et retourne son identifiant.

- `task lestaches.txt modify id [-d nouvelle description] [-o nouveau propiétaire]`  
   Remplace la description de la tâche d’identifiant `id` dans `lestaches.txt`. Renvoie un message d’erreur si la tâche n’est pas trouvée.

- `task lestaches.txt rm id`  
   Retire la tâche d’identifiant `id` du fichier `lestaches.txt`. Renvoie un message d’erreur si la tâche n’est pas trouvée.

- `task lestaches.txt show`  
   Affiche la liste des tâches du fichier, triées par identifiant, sous la forme suivante :

   ```
   [id] description
   ```

## Extension 1 : Propriétaire (owner)

Les tâches peuvent être associées à un propriétaire grâce aux commandes suivantes :

- `task lestaches.txt add <description> -o <owner>`  
   Ajoute une nouvelle tâche avec le propriétaire spécifié.

- `task lestaches.txt modify id <nouvelle description> -o <owner>`  
   Modifie la description et/ou le propriétaire de la tâche d’identifiant `id`.

Le propriétaire est affiché dans la liste des tâches sous la forme :

```
[id] description owner
```
## Extension 2 : Fichier de log

Chaque action effectuée par le programme doit être enregistrée dans un fichier `log.txt`. Le fichier log contient une ligne pour chaque commande exécutée, précisant l'action, le résultat et le type d'erreur le cas échéant.

Exemples de lignes ajoutées au fichier `log.txt` :

- Pour la commande `task lestaches.txt show` :  
   ```
   Action : show task, Result : Success, Type error : None
   ```

- Pour la commande `task lestaches.txt add <description> [-o owner]` :  
   ```
   Action : add task, Result : Success, Type error : None
   ```
   En cas d'échec :
   ```
   Action : add task, Result : Failure, Type error : <description de l'erreur>
   ```

- Pour la commande `task lestaches.txt rm id` :  
   ```
   Action : remove task, Result : Success, Type error : None
   ```
   En cas d'échec :
   ```
   Action : remove task, Result : Failure, Type error : Task not found
   ```

- Pour la commande `task lestaches.txt modify id [-d nouvelle description] [-o nouveau propriétaire]` :  
   ```
   Action : modify task, Result : Success, Type error : None
   ```
   En cas d'échec :
   ```
   Action : modify task, Result : Failure, Type error : Task not found
   ```

Chaque ligne du fichier log doit refléter précisément l'action réalisée, son résultat et le type d'erreur éventuel.

## Extension 3 : Vérification de format

Après chaque action susceptible de modifier le fichier des tâches, le logiciel vérifie la conformité du format du fichier.

- Pour chaque ligne du fichier, le format attendu est :
  
  ```
  int: ID, str: description, str: owner
  ```

- Un fichier vide ou inexistant est considéré comme conforme.

- Par exemple, après une commande de modification (`task lestaches.txt modify id [-d nouvelle description] [-o nouveau propriétaire]`), le programme vérifie que chaque ligne respecte ce format.

- En cas de non-conformité, une erreur doit être signalée et enregistrée dans le fichier `log.txt`.
