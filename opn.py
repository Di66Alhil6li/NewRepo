# class Tes:
# fil = open("ted.text","r")
# print(fil.readline())
# fil.close()

with open("ds.text","r") as fl:
    for i in fl.readlines():
        print(i,end="")

with open("ds.text","w") as new_f:
    new_f.write("\nI'm Diaa Sadiq is Programming devloper web & Eng Networks & ux/ui")