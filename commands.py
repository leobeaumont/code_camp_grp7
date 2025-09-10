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
            print("ID: {}  |  Desc: {}".format(attr[0], attr[1]))
