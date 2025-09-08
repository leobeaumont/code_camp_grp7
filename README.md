README du codechamp GR7
 Le butducodecampestlaproductiond’unlogiciel simple de gestion de tâches.
 Le point de départ est commun à tous les groupes et consiste à réaliser les commandes suivantes :

-  ajout, modification et suppression de tâches. Une tâche a une description (un texte sans retour chariot)
 et unidentifiant donné à sa création. Il conviendra également de fournir un moyen de voir la liste des
 tâches.
 L’interaction avec l’utilisateur doit rester simple; nous optons pour une interaction en ligne de commande dans un terminal(CLI–CommandLineInterface).
 Chaque exécution du programme recevra en paramètre un nom de fichier dans lequel sont contenues
 les tâches déjà créées. Le résultat de l’exécution modifiera généralement le contenu de ce fichier.
 Vous êtes libres du choix du format du fichier,mais nous recommandons de rester simple(par exemple,
 un format texte avec une ligne par tâche).
 Cette première version doit donc permettre d’exécuter les commandes suivantes nous supposons
 que votre programme s’appelle task :
 — task lestaches.txt add <la description sur le reste de la ligne> : ajoute au fi
chier lestaches.txt la ligne de la tâche, retourne son identifiant;
 — task lestaches.txt modify id <la nouvelle description sur le reste de la ligne>:
 remplace la description de la tâche d’identifiant id dans lestaches.txt, renvoie un message
 d’erreur si la tâche n’est pas trouvée;
 — task lestaches.txt rm id : retire la ligne du fichier lestaches.txt contenant la tâche
 d’identifiant id, renvoie un message d’erreur si la tâche n’est pas trouvée;
 — task lestaches.txt show: affiche la liste des tâches du fichier sous la forme ci-dessous en
 les triant par leurs identifiants.