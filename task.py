from parser import *
from commands import *
from file_integrity import *
from file_integrity import check_integrity
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
            if not check_integrity(options.file):
                print("File integrity check failed after add operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after add operation\n")
            else :
                add_task(options.file, options.details, options.owner,options.project)
            
        # Commande modify
        elif options.command == 'modify':
            if not check_integrity(options.file):
                print("File integrity check failed after modify operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after modify operation\n")
            else :
                modify_task(options.file, options.id, options.details, options.owner,options.project)
            
        # Commande remove
        elif options.command == 'rm':
            if not check_integrity(options.file):
                print("File integrity check failed after remove operation")
                with open("log.txt", 'a') as f:
                    f.write("File integrity check failed after remove operation\n")
            else :
                remove_task(options.file, options.id)
            
        # Commande show
        elif options.command == 'show':
            show_tasks(options.file)
        # Message d'erreur si la commande n'est pas reconnue
        else:
            print("Commande inconnue")
    except FileNotFoundError:
        print(f"The file {options.file} was not found")
