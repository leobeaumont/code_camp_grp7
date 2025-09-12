from parser import *
from commands import *
from file_integrity import *
""" Programme principal pour l'application de gestion de tâches."""


if __name__ == "__main__":
    parseur = create_parser() 
    args = parseur.parse_args()
    # Création du parseur de ligne de commande
    options = create_parser().parse_args()
    try:
        # Exécution de la commande
        # Commande add
        if options.command == 'add':
            add_task(options.file, options.details, options.owner)
            if not file_integrity(options.file):
                print("File integrity check failed after add operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after add operation\n")
        # Commande modify
        elif options.command == 'modify':
            modify_task(options.file, options.id, options.details, options.owner)
            if not file_integrity(options.file):
                print("File integrity check failed after modify operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after modify operation\n")
        # Commande remove
        elif options.command == 'rm':
            remove_task(options.file, options.id)
            if not file_integrity(options.file):
                print("File integrity check failed after remove operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after remove operation\n")
        # Commande show
        elif options.command == 'show':
            show_tasks(options.file)
        # Message d'erreur si la commande n'est pas reconnue
        else:
            print("Commande inconnue")
    except FileNotFoundError:
        print(f"The file {options.file} was not found")
