import argparse

def create_parser():
  # Création du parseur de ligne de commande
  parser = argparse.ArgumentParser(description='Simple task manager')

  # Ajout d’un argument positionnel (le fichier contenant les tâches)
  parser.add_argument('file', help='The tasks file')

  # Ajout d’un sous-parseur pour les sous-commandes
  subparsers = parser.add_subparsers(help='The commands to manage orders', dest='command', required=True)

  # Création du parseur pour la commandeadd
  parser_add = subparsers.add_parser ('add', help='Add a new task.')
  parser_add.add_argument('details', nargs='*', default="no details",help="task details")

  # Création du parseur pour la commandemodify
  parser_modify = subparsers.add_parser('modify',help='Modify a task givenits id')
  parser_modify.add_argument('id', help="the task id")
  parser_modify.add_argument('details', nargs='*', default="no details", help="the new details")

  # Création du parseur pour la commanderm
  parser_rm = subparsers.add_parser('rm', help='Remove an task given its id')
  parser_rm.add_argument('id', help="the task id")
 
  # Création du parseur pour la commandeshow
  parser_show = subparsers.add_parser('show', help='Show the tasks')
  return parser