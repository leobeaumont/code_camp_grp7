import os.path

def get_id(file):
    if os.path.isfile(file) == False:
        return 0
    
    with open(file, 'r') as f:
        content = f.read()

    if len(content) == 0:
        return 0

    return max([int(line.split(",")[0]) for line in content.split("\n")])

def add_task(file, description, owner=None):
    exist=os.path.isfile(file)
    id = get_id(file)

    if exist:
        with open(file, "r") as f:
            content = f.read()

    with open(file, 'a+') as f:
        if exist:
            if len(content) != 0:
                f.write(f"\n{id},{description},{owner}")
                return
        f.write(f"{id},{description},{owner}")

def remove_task(file, id):

    with open(file, 'r') as f:
        file_text = f.readlines()

    with open(file, 'w') as f:
        for line in file_text:
            if int(line.split(",")[0]) != id:
                f.write(line)

def show_tasks(file):
    with open(file, "r") as f:
        for line in f.readlines():
            attr = line.strip("\n").split(",")
            print("ID: {}  |  Desc: {}  |  Owner: {}".format(attr[0], attr[1], attr[2]))

def modify_task(file, id, description, owner=None):
    with open(file, 'r') as f:
        lines = f.readlines()

    for line_number,line in enumerate(lines):
        alt = line.split(",")
        if int(alt[0]) == id:
            lines[line_number] = f"{alt[0]},{description},{owner}\n"

    with open(file, 'w') as f:
        f.writelines(lines)
