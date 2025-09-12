import os.path

def get_id(file):
    if os.path.isfile(file) == False:
        return 0
    
    with open(file, 'r') as f:
        content = f.read()

    if len(content) == 0:
        return 0

    return max([int(line.split(",")[0]) for line in content.split("\n")])

def log_action(command, result, log_file="log.txt"):
    """Ajoute une commande et son résultat dans le fichier journal"""
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"commande: {command} | resultat: {result}\n")

def add_task(file, description, owner=None):
    exist=os.path.isfile(file)
    id = get_id(file)
    # Journaliser la commande et le résultat exact
    command_str = f"add {description}"
    line = f"{id},{description},{owner}"
    try :
        if exist:
            with open(file, "r") as f:
                content = f.read()

        with open(file, 'a+') as f:
            if exist:
                if len(content) != 0:
                    f.write(f"\n{id + 1},{description},{owner}")
                    log_action(command_str, line)
                    return
            f.write(f"{id},{description},{owner}")
            log_action(command_str, line)

    except Exception as e:
        # Journaliser l’échec
        command_str = f"add {description}"
        log_action(command_str, f"Échec - Erreur: {str(e)}")
        raise

def remove_task(file, id):

    with open(file, 'r') as f:
        file_text = f.readlines()

    with open(file, 'w') as f:
        modified = False
        for line in file_text:
            if int(line.split(",")[0]) != id:
                f.write(line)
            else:
                modified = True
    
    if not modified:
        print("Invalid ID: {}, nothing removed".format(id))

def show_tasks(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f.readlines():
                attr = line.strip("\n").split(",")
                print("ID: {}  |  Desc: {}  |  Owner: {}".format(attr[0], attr[1], attr[2]))
                error_status = False
    except Exception as e: #catch all exceptions to print them in log
        print(f"Error reading file: {e}")
        error_status = True
        error_type = type(e).__name__
    with open("log.txt", 'a') as f:
        f.write("Action : show tasks , Result : {}, Error Type : {}\n".format("Success" if not error_status else "Failure", error_type if error_status else "None"))

    
def modify_task(file, id, description=None, owner=None):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        modified = False
        for line_number,line in enumerate(lines):
            alt = line.split(",")
            if int(alt[0]) == id:
                modified = True
                lines[line_number] = f"{alt[0]},{description if description is not None else alt[1]},{owner + "\n" if owner is not None else alt[2]}"

        with open(file, 'w') as f:
            f.writelines(lines)

        if not modified:
            print("Invalid ID: {}, no line modified".format(id))
            raise IndexError
        
        with open("log.txt", "a") as f:
            f.write(f"Command:\nmodify file: {file}, new description: {description}, new owner: {owner}\nResult:\nSuccess\n\n")
    except Exception as e:
        with open("log.txt", "a") as f:
            f.write(f"Command:\nmodify file: {file}, new description: {description}, new owner: {owner}\nResult:\n{type(e)}\n\n")
            raise e
