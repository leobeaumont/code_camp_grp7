import argparse  # Permet de créer et vérifier les arguments de commande


def create_parser():
    """
    Cette fonction crée un parseur qui connaît les commandes suivantes :
      task.py <fichier> add <description...> [owner]
      task.py <fichier> modify <id> <nouvelle description...> [new owner]
      task.py <fichier> rm <id>
      task.py <fichier> show
    """
    parser = argparse.ArgumentParser(prog="task")  # Le programme s’appelle "task"

    # Premier argument obligatoire : le fichier texte où sont stockées les tâches
    parser.add_argument("file", help="Nom du fichier des tâches")

    # On ajoute des sous-commandes (add, modify, rm, show)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- add ---
    parser_add = subparsers.add_parser("add", help="Ajouter une nouvelle tâche")
    parser_add.add_argument("details", nargs="+", help="Description de la tâche")

    # --- modify ---
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche")
    parser_modify.add_argument("id", type=int, help="Numéro (id) de la tâche")
    parser_modify.add_argument("details", nargs="+", help="Nouvelle description")

    # --- rm ---
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id", type=int, help="Numéro (id) de la tâche")

    # --- show ---
    subparsers.add_parser("show", help="Afficher toutes les tâches")

    return parser