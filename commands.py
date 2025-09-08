def remove_task(file, id):

    with open(file, 'r') as f:
        file_text = f.readlines()

    with open(file, 'w') as f:
        for line in file_text:
            if int(line.split(",")[0]) != id:
                f.write(line)
