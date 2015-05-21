print 'Welcome to the Pig Latin Translator!'
print "Enter your text, seperated with spaces."
print "Please type compound words with spaces. eg. 'bed room' or 'camp site'."
def translateNew():
    translated = []
    strings = []
    word = raw_input("What are your words to translate?")
    x = 0
    while x < len(word):
        if word[x] == " ":
            if x == 0: 
                l = list(word) #Delete works on arrays (or lists), but not strings. You cannot delete characters from strings. These three lines convert string to array, delete array element, convert back to string
                del(l[x])
                word = "".join(l) #Converts array elements to carracters. str() will print the elements, including appostrophes used to define array elements                           
                x = x - 1
            if x > 0:
                strings.append(word[:x]) #Add word before space to the first array element
                word = word[x + 1:] #The original input 'word' is now the rest of the sentence without the space
                x = 0
            else: 
                x = x + 1
        else:
            x = x + 1
    strings.append(word) #This adds the last word with no spaces as an array element
    print " "
    print "- Your translated words - "
    for x in range (0, len(strings)):
        exclaimer = []
        y = 0
        wordLength = len(strings[x])
        strings[x] = strings[x].lower()
        while y < wordLength: 
            if strings[x][y] in "~/\[]{}<>@#$%^&*()_.,-+=?!;:'":
                if x == (len(strings) - 1):
                    if strings[x][y] in "?!.":
                        exclaimer.append(strings[x][y])
                else:
                    exclaimer.append("")
                l = list(strings[x]) #To array You
                del(l[y])
                strings[x] = "".join(l) #To string. 
                wordLength = wordLength - 1
                y = y - 1
            y = y + 1    
        strings[x] = strings[x].lower()
        firstLetter = strings[x][0]
        exclaimer = "".join(exclaimer)
        if x == 0:
            if firstLetter in "aeiou":
                if strings[x][len(strings[x])-1] == "y":
                    translated.append(strings[x][0].upper() + strings[x][1:] + "ay")
                else:
                    translated.append(strings[x][0].upper() + strings[x][1:] + "yay")
            elif strings[x][1] not in "aeiou":
                secondLetter = strings[x][1]
                translated.append(strings[x][2].upper() + strings[x][3:] + firstLetter + secondLetter + "ay" + exclaimer)
            else:
                translated.append(strings[x][1].upper() + strings[x][2:] + firstLetter + "ay" + exclaimer)
        else:
            if firstLetter in "aeiou":
                if strings[x][len(strings[x])-1] == "y":
                    translated.append(strings[x] + "ay")
                else:
                    translated.append(strings[x] + "yay")
            elif strings[x][1] not in "aeiou":
                secondLetter = strings[x][1]
                translated.append(strings[x][2:] + firstLetter + secondLetter + "ay" + exclaimer)
            else:
                translated.append(strings[x][1:] + firstLetter + "ay" + exclaimer)       
        print strings[x] + " - " + translated[x]
    print ""
    translated = " ".join(translated)
    print " - Your translated sentence - "
    print translated
    print ""
    translateNew()
translateNew()
