smell = open("file-3.notpy","r")
stink_machine = True
for smell_2 in smell.readlines():
    if stink_machine == True:
        stink_machine = False
        print(smell_2)
    else :
        stink_machine = True

smell.close()
