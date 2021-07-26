while True:
    inputter = int(input("type any number between 1 and 9!(not a trap)"))
    if inputter >= 10 or inputter <= 0:
        print ("This statement is false.")
    else:
        break
smell = open("file-3.notpy","r")
counter = 0
for smell_2 in smell.readlines():
    counter +=1
    if counter%inputter == 0:
        print(smell_2)
smell.close()
