smell = open("file-3.notpy","r")
basic_phonics = []
babys_first_calculus = []
for line in smell.readlines():
    for ch in ".,!()\n\"":
        line = line.replace(ch," ")
    for word in line.split(" "):
        if word == "":
            continue
        try:
            level_of_basic_phonics = basic_phonics.index(word)
            babys_first_calculus[level_of_basic_phonics] +=1
        except:
            basic_phonics.append(word)
            babys_first_calculus.append(1)
smell.close()
for i in range(len(babys_first_calculus)):
    print(basic_phonics[i],babys_first_calculus[i])

