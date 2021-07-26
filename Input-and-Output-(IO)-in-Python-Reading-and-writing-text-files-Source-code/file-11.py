#!/usr/bin/python3.8
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

def search(word):
    for i in range(len(basic_phonics)):
        if basic_phonics[i][0] == word:
            return i
    raise RuntimeError("sorry, we couldn't find the george you're looking for")
#print (search("fish"))

def binary_search(word):
    lo = 0
    hi = len(basic_phonics)-1
    while True:
        if (hi-lo) < 3:
            while lo <= hi:
                if basic_phonics [lo][0] == word :
                    return lo
                lo +=1
            raise RuntimeError("hey! you! you're searching for a nonexistent word! if its not in our dictionary, it's not a word!")

        mid = int((lo + hi) / 2)
        print(f"mid = {mid}")
        if basic_phonics[mid][0] < word:
            lo = mid
        elif basic_phonics[mid][0]== word:
            return mid
        else:
            hi = mid
index = binary_search("fish")
print(f"{index} {basic_phonics[index][0]}")

