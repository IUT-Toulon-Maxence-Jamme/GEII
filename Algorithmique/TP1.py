#------------------------------------
#             TP1 PYTHON
#------------------------------------

import random

#------------ Fonctions -------------
def multiplie(a,b) : 
 return a*b

# Exercice 0)
def exercice_0(a) :
    i = 0
    for i in range(a+1):
        k = i
        for j in range(2, int(k/2)+1):
             if (k % j) == 0:                
                break
        else:
            if i != 0 and i != 1:
                print("i =", i*i)

# Exercice 1)
def exercice_1(a) :
    i = 0
    for i in range(a+1):
       print("i =", i, "le carré = ", i*i)


# Exercice 2)
def exercice_2(a) :
    s = ['a','e','i','o','u','y']
    nb_voyelle = 0
    for i in range(len(a)):
       for j in range(len(s)):
           if a[i]==s[j]:
               nb_voyelle +=1
    s = f"Le nombre de voyelles est de {nb_voyelle}"
    print(s)

# Exercice 3)
def exercice_3(a) :
    s = ['a','e','i','o','u','y']
    nouveau_mot = ""
    for i in range(len(a)):
        voyelle = 0
        for j in range(len(s)):
            if a[i]==s[j]:
                voyelle = 1
        if voyelle == 0:
            nouveau_mot = nouveau_mot + a[i]            
               
    s = f"Le nouveau mot est {nouveau_mot}"
    print(s)
    return nouveau_mot


# Exercice 4)
def exercice_4(a) :
    s = a[::-1]
    if s == a:
        return "vrai"
    else :
        return "faux"

# Exercice 5)
def exercice_5(a,b) :
    nouveau_mot = ""
    if len(a) < len(b):
        for i in range(len(a)):
            nouveau_mot = nouveau_mot + a[i] + b[i]
        nouveau_mot = nouveau_mot + b[len(a):]
    else:
        for i in range(len(b)):
            nouveau_mot = nouveau_mot + a[i] + b[i]
        nouveau_mot = nouveau_mot + a[len(b):]
    print(nouveau_mot)
            
# Exercice 6)
def exercice_6() :
    liste = []
    i = 0
    while len(liste)<7:
        a = random.randint(1, 19)
        double = 0        
        for j in range(len(liste)):
            if a == liste[j]:
                double = 1
        if double != 1:
            liste.append(a)
            i+=1
    print(liste)

# Exercice 7)
def exercice_7(a) :
    a = a[::-1]
    nombre = 0
    for i in range(len(a)):
        if a[i]=='1':
            nombre = nombre + 2**i
    print(nombre)

# Exercice 8)
def exercice_8(mot) :
    nouveau_mot = ""
    for lettre in mot:
        nouveau_mot += hex(ord(lettre))
    nouveau_mot = nouveau_mot.replace('0x', ' ')
    print(nouveau_mot)
    return nouveau_mot

# Exercice 9)
def exercice_9(mot) :
    mot = mot.split(' ')
    if mot[0] == '':
        del mot[0]
    nouveau_mot = ""
    for lettre in mot:        
        nouveau_mot += chr(int(lettre,16))  
    print(nouveau_mot)


    
#----------- Programmes -------------

if __name__ == '__main__': 
    #r=multiplie(3,4)
    #- Exercice -
    
    exercice = 5
    
    #------------

    
    # Exercice 0)
    if exercice == 0:
        nombre_max = int(input("Entrez un nombre maximun : "))
        exercice_0(nombre_max)

    # Exercice 1)
    if exercice == 1:
        nombre_max = int(input("Entrez un nombre maximun : "))
        exercice_1(nombre_max)

    # Exercice 2)
    if exercice == 2:
        mot = input("Entrez un mot : ")
        exercice_2(mot)

    # Exercice 3)
    if exercice == 3:
        mot = input("Entrez un mot : ")
        exercice_3(mot)

    # Exercice 4)
    if exercice == 4:
        mot = input("Entrez un mot : ")
        test = exercice_4(mot)
        print(test)

    # Exercice 5)
    if exercice == 5:
        mot1 = input("Entrez un mot : ")
        mot2 = input("Entrez un second mot : ")
        exercice_5(mot1,mot2)
        exercice_5('abcdefgh','xyz')
        exercice_5('xyz','abcdefgh')

    # Exercice 6)
    if exercice == 6:
        print("Début du tirage...")
        exercice_6()

    # Exercice 7)
    if exercice == 7:
        nombre = input("Entrez un binaire : ")
        exercice_7(nombre)

    # Exercice 8)
    if exercice == 8:
        mot = input("Entrez un mot : ")
        exercice_8(mot)
        #exercice_8('Abc B0c')
        
    # Exercice 9)
    if exercice == 9:
        mot = input("Entrez un mot : ")
        exercice_9(mot)
        #rep = exercice_8(mot)
        #exercice_9(rep)
       
 
