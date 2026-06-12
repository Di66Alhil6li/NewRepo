tota = 0.0

def read_file(name_file="text.text"):
    global tota
    with open(name_file, "r") as read:
        for line in read:
            is_not_full = line.strip()
            if is_not_full:
                tota += float(is_not_full)


def creat_file(name_file=None):
    global tota
    if name_file is None:
        name_file = f"name{tota}.texe"
    with open(name_file, "w") as all_sal:
        all_sal.write(f"Total salary_day: {tota}")

read_file("read_myfile.text")

creat_file()
