#------------------------------------
#             TP2 PYTHON
#------------------------------------

import random

#------------ Fonctions -------------

# Exercice 1)
def writeToFile(s, filename) :
    return
   

# Exercice 2)
def appendToFile(s, filename) :    
    fi = open(filename,s)    
    fi.write("\nBLABLAA")
    fi.close()

# Exercice 3)
def writeData(filename) :    
    fi = open(filename,'w')    
    text = ""
    i = -10
    while i <=10:
        calcule = i*i+2*i+4
        text += str(i) + ";" + str(calcule) + "\n"
        i +=1
    fi.write(str(text))
    fi.close()

# Exercice 4)
def writeFunction(filename,function,mini,maxi):
    fi = open(filename,'w')
    text = ""
    i = mini
    while i <=maxi:
        calcule = function(i)
        text += str(i) + ";" + str(calcule) + "\n"
        i +=1
    fi.write(str(text))
    fi.close()

def function(x):
    return x*x+2*x+4

# Exercice 5)
def nbCarFile(filename):
    fi = open(filename,'r')
    nb = 0
    for c in fi.read():
        nb += 1
    print(nb)
    fi.close()

# Exercice 6)
def nbBytesFile(filename):
    fichier = open(filename,'rb')
    nb = 0
    while 1:
        b = fichier.read(1)        
        if b==b'': # b'' est un byte vide
            break
        nb += 1
        # exploiter b
    print(nb)
    fichier.close()


# Exercice 7)
def nbLinesFile(filename):
    fichier = open(filename,'rb')
    texte = fichier.readlines()
    nb = len(texte)
    fichier.close()
    return nb

# Exercice 8)
def exercice_8(filename,c):
    fichier = open(filename,'w')
    chaine = ""
    c = c.split(":")
    for i in c:
        chaine += "0x" + i + ','
    texte = "{" + chaine[:-1]+ "};"    
    print(texte)    
    fichier.close()    

# Exercice 9)
def removeChar(firstList,toRemoveList):
    liste = []
    for i in range(len(firstList)):
        for j in toRemoveList:
            if firstList[i] == j or firstList[i] == "":
                liste.append(i)
                break
    liste = liste[::-1]
    for i in range(len(liste)):
        del firstList[liste[i]]
    #print(firstList)
    return firstList

# Exercice 10)
def compteMots(filename):
    nbligne = nbLinesFile(filename)
    nbm = 0
    toRemoveList = ["!", "?", ":"]
    fichier = open(filename,'r')
    for i in range(nbligne):
        texte = fichier.readline()
        texte = texte.strip()
        texte = texte.split(' ')
        removeChar(texte,toRemoveList)
        for i in range(len(texte)):
            mot = removePunct(texte[i])
            print(mot)
        nbm = nbm + len(texte)
    fichier.close() 
    return nbm

# Exercice 11)
def removePunct(mot):
    remove = ['!', '?', ',', ';', ':', '.']
    for i in remove:
        mot = mot.replace(i, '')
    return mot

# Exercice 12)
def dicoMots(filename) :

    D = {}
    nbligne = nbLinesFile(filename)
    toRemoveList = ["!", "?", ":"]
    fichier = open(filename,'r')
    for i in range(nbligne):
        texte = fichier.readline()
        texte = texte.strip()
        texte = texte.split(' ')
        removeChar(texte,toRemoveList)
        for i in range(len(texte)):
            mot = removePunct(texte[i])
            if mot in D:
                D[mot] += 1
            else:
                D[mot] = 1
    fichier.close() 
    return D
    
# Exercice 13)    
def maxDico(d) :
    maxi = 0
    maxi_mot = ""
    for mot in d :
        if maxi < d.get(mot):
            maxi_mot = mot
            maxi = d.get(mot)
    print("Le mot avec le plus d'occurence est :",maxi_mot," il a exactement", maxi,"occurences")

def facto(n):
    if n == 0:
        return 1
    else:
        return n*facto(n-1)
    
#----------- Programmes -------------

if __name__ == '__main__': 
    
    #------------ Exercice ------------
    
    exercice = 13
    
    #----------------------------------

    
    # Exercice 1)
    if exercice == 1:         
        filename = 'fichier.txt'
        s = 'r'
        writeToFile(s, filename)

    # Exercice 2)
    if exercice == 2:         
        filename = 'fichier.txt'
        s = 'a'
        appendToFile(s, filename)
        mot = removePunct(mot)
        print(mot)
    # Exercice 3)
    if exercice == 3:         
        filename = 'fichier.txt'
        writeData(filename)
        
    # Exercice 4)
    if exercice == 4:         
        filename = 'fichier.txt'
        mini = -10
        maxi = 10
        writeFunction(filename,function,mini,maxi)

    # Exercice 5)
    if exercice == 5:         
        filename = 'fichier.txt'
        nbBytesFile(filename)

    # Exercice 6)
    if exercice == 6:         
        filename = 'fichier - Copie.txt'
        nbCarFile(filename)

    # Exercice 7)
    if exercice == 7:         
        filename = 'fichier.txt'
        nbLinesFile(filename)

    # Exercice 8)
    if exercice == 8:
        filename = 'fichier.txt'
        c = "14:87:20:6B:C4:8A:50:99:5C:8F:8F:7A:68:3B:96:F5:08:BA:60:94"
        exercice_8(filename, c)

    # Exercice 9)
    if exercice == 9:
        firstList=['un','deux','cinq','trois','quatre','cinq','six','','trois','quatre','']

        toRemoveList=['trois','cinq','six']

        new_liste = removeChar(firstList,toRemoveList)
        print(new_liste)
    # Exercice 10)
    if exercice == 10:
        nbm = compteMots(filename)
        print('Nombre de mots =', nbm)
        
    # Exercice 11)
    if exercice == 11:
        mot = "Bon,jour!"
        print(mot)
        mot = removePunct(mot)
        print(mot)

    # Exercice 12)
    if exercice == 12:
        filename = 'fichier.txt'
        print(dicoMots(filename))

    # Exercice 13)
    if exercice == 13:
        filename = 'fichier.txt'
        d = dicoMots(filename)
        maxDico(d)
        print(max(d))

    # Exercice 14)
    if exercice == 14:
        x = 8
        x = facto(x)
        print(x)
