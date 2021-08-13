smell = open("file-3.notpy","r")

stink_machine = True

for smell_2 in smell.readlines():
    if stink_machine == True:
        stink_machine = False
    else:
        stink_machine = True
        print(smell_2)
smell.close()
