import re
import os

def check_integrity(file):
    if os.path.isfile(file) == False:
        return True
    
    with open(file, "r") as f:
        lines = f.readlines()

    correct_line = r"[0-9]+,[^,]+,[^,]+"

    for line in lines:
        if not re.fullmatch(correct_line, line):
            return False
    return True
