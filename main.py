from parser import *
from commands import *


if __name__ == "__main__":
    parseur = create_parser()
    args = parseur.parse_args()
    # Création du parseur de ligne de commande
    options = create_parser().parse_args()
    try:
        # Lecture du fichier de commandes,s’il existe
        with open(options.file, 'r') as f:
            tasks = f.readlines()
        # Exécution de la commande
        if options.command == 'add':
            add_task(options.file, ' '.join(options.details))
        elif options.command == 'modify':
            modify_task(options.file, options.id, ' '.join(options.details))
        elif options.command == 'rm':
            remove_task(options.file, options.id)
        elif options.command == 'show':
            show_tasks(tasks)
        else:
            print("Commande inconnue")
    except FileNotFoundError:
        print(f"The file {options.file} was not found")
