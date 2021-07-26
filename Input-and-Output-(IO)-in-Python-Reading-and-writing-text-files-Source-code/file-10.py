smell = open("file-3.notpy","r")
basic_phonics = []
def sorty_mc_wordplay(words):
    go = True
    while go:
        go = False
        for i in range(len(words)-1):
            left = words[i]
            right = words[i+1]
            if right[0].lower() < left[0].lower():

                temp = words[i+1]
                words[i+1] = words[i]
                words[i] = temp
                go = True



for line in smell.readlines():
    for ch in ".,!()\n\"":
        line = line.replace(ch," ")
    for word in line.split(" "):
        if word == "":
            continue
        modified = False
        for i in range(len(basic_phonics)):
            if basic_phonics[i][0] == word:
                basic_phonics[i][1] += 1
                modified = True
                break
        if modified == False:
            basic_phonics.append([word,1])
    sorty_mc_wordplay(basic_phonics)
smell.close()
for item in basic_phonics:
    print(item)

