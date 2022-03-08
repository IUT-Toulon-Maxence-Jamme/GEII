#------------------------------------
#             TP1 PYTHON
#             CORRECTION             
#------------------------------------

#------------------------------------
#             Erreur PDF
#    Exercice 12: B = 41 (B = 0x42)
#------------------------------------

import random

# Exercice 1)
def exercice_1(nb) :
    i = 0
    for i in range(nb+1):
       print(i, "*", i, "=", i*i)

# Exercice 2)
def exercice_2(mot) :
    nb_voyelle = 0
    for lettre in mot:
       if lettre in ['a','e','i','o','u','y']:
            nb_voyelle +=1
    s = f"Le nombre de voyelles est de {nb_voyelle}"
    print(s)

# Exercice 3)
def exercice_3(mot) :
    nouveau_mot = ""
    for lettre in mot:
        if not lettre in ['a','e','i','o','u','y']:
            nouveau_mot = nouveau_mot + lettre           
    s = f"Le nouveau mot est {nouveau_mot}"
    print(s)
    return nouveau_mot

# Exercice 4)
def exercice_4(mot) :
    return mot == mot[::-1]

# Exercice 5)
def exercice_5(a,b) :
    nouveau_mot = ""
    for e1,e2 in zip(a,b) :
        nouveau_mot += e1 + e2

    nouveau_mot += b[len(a):] + a[len(b):]
    print(nouveau_mot)

# Exercice 6)
def exercice_6() :
    liste = []
    i = 0
    while len(liste)<7:
        a = random.randint(1, 49)
        if not a in liste:            
            liste.append(a)
            i+=1
    print(liste)

# Exercice 7)
def exercice_7(binaire) :
    binaire = binaire[::-1]
    nombre = 0
    for i in range(len(binaire)):
        if binaire[i]=='1':
            nombre = nombre + 2**i
    print(nombre)

# Exercice 8)
def exercice_8(mot) :
    nouveau_mot = ""
    for lettre in mot:
        nouveau_mot += hex(ord(lettre))[2:] + " "
    print(nouveau_mot)
    return nouveau_mot

# Exercice 9)
def exercice_9(mot) :
    mot = mot.split(' ')
    if mot[-1] == '':
        del mot[-1]
    nouveau_mot = ""
    for lettre in mot:        
        nouveau_mot += chr(int(lettre,16))  
    print(nouveau_mot)


       

#----------- Programmes -------------

if __name__ == '__main__': 
    
    #------------ Exercice ------------
    
    exercice = 9
    
    #----------------------------------

    
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
        #exercice_5('abcdefgh','xyz')
        #exercice_5('xyz','abcdefgh')

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
        #exercice_9(mot)
        rep = exercice_8(mot)
        exercice_9(rep)
