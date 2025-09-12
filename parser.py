import argparse  # Permet de créer et vérifier les arguments de commande


def create_parser():
  """
  Cette fonction crée un parseur qui connaît les commandes suivantes :
    task <fichier> add <description...> <propriétaire>
    task <fichier> modify <id> <nouvelle description...> <propriétaire>
    task <fichier> rm <id>
    task <fichier> show
  """
  parser = argparse.ArgumentParser(prog="task")  # Le programme s’appelle "task"

  # Premier argument obligatoire : le fichier texte où sont stockées les tâches
  parser.add_argument("file", help="Nom du fichier des tâches")

  # On ajoute des sous-commandes (add, modify, rm, show)
  subparsers = parser.add_subparsers(dest="command", required=True)

  # --- add ---
  parser_add = subparsers.add_parser("add", help="Ajouter une nouvelle tâche")
  parser_add.add_argument("details", help="Description de la tâche", type=str)
  parser_add.add_argument("-o", "--owner", help="Propriétaire de la tâche")  # optionnel
  parser_add.add_argument("-p", "--project", help="Projet de la tâche")  # optionnel

  # --- modify ---
  parser_modify = subparsers.add_parser("modify", help="Modifier une tâche")
  parser_modify.add_argument("id", type=int, help="Numéro (id) de la tâche")
  parser_modify.add_argument("-d", "--details", help="Nouvelle description", type=str)
  parser_modify.add_argument("-o", "--owner", help="Propriétaire de la tâche")  # optionnel
  parser_add.add_argument("-p", "--project", help="Projet de la tâche")  # optionnel

  # --- rm ---
  parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
  parser_rm.add_argument("id", type=int, help="Numéro (id) de la tâche")

  # --- show ---
  subparsers.add_parser("show", help="Afficher toutes les tâches")

  return parser