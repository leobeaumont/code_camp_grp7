import argparse  # Permet de créer et vérifier les arguments de commande
import shlex     # Permet de découper une ligne de texte comme un terminal (utile dans le menu)


def create_parser():
    """
    Cette fonction crée un parseur qui connaît les commandes suivantes :
      task <fichier> add <description...>
      task <fichier> modify <id> <nouvelle description...>
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



def test_command(command_line: str):
    """
    Cette fonction prend une ligne de commande (ex: 'task fichier.txt add Acheter du pain')
    et vérifie si elle est correcte.
    """
    parser = create_parser()

    # On découpe la ligne comme le ferait un vrai terminal (gère guillemets, espaces…)
    parts = shlex.split(command_line)

    # Vérifie que la commande commence bien par "task"
    if not parts or parts[0] != "task":
        print(" La commande doit commencer par 'task'")
        return

    # On enlève le mot 'task', car argparse attend juste les arguments qui suivent
    args = parts[1:]

    try:
        # Analyse des arguments
        options = parser.parse_args(args)

        # Si tout est bon, on affiche ce qui a été compris
        print("Commande valide !")
        print("  Fichier :", options.file)
        print("  Action  :", options.command)
        if hasattr(options, "id"):
            print("  ID      :", options.id)
        if hasattr(options, "details"):
            print("  Texte   :", " ".join(options.details))

    except SystemExit:
        # argparse appelle "exit()" si erreur → on l’intercepte
        print("Erreur : commande ou arguments invalides.")



def menu():
    print("=== MENU DE TEST DU PARSEUR ===")
    print("Exemples valides :")
    print("  task todo.txt add Acheter du pain")
    print("  task todo.txt modify 1 Nouvelle description")
    print("  task todo.txt rm 2")
    print("  task todo.txt show")
    print("Tape 'quit' pour quitter.\n")

    while True:
        ligne = input(">> ")  # On lit ce que tape l’utilisateur
        if ligne.lower() in ("quit", "exit"):
            print("Au revoir ")
            break
        if not ligne.strip():  # Si l’utilisateur tape juste Entrée
            continue

        test_command(ligne)  # On teste la commande entrée



if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Mode direct : l’utilisateur a passé une commande dans le terminal
        # Exemple : python task_parser.py todo.txt add "Acheter du pain"
        command_line = "task " + " ".join(sys.argv[1:])
        test_command(command_line)
    else:
        # Sinon, on ouvre le menu interactif
        menu()
