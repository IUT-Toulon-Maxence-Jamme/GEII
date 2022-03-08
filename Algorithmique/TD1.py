#monty python le pont de la mort (spam)
'''
    -Variables :
        x = 8
        type(x) -> <class 'int'>
        x='bonjour'
        type(x) -> <calss 'str'>
   
    -Fonction :
        def m(a,b):
            return a*b;
        def f(x):
            return 2*x;
            
    -Print
        print('a', end='') -> a>>> #ne fais pas de retour à la ligne

    -Input

    -Calcul:
        a,b = 3,4
        a,b = b,a

        a = 6
        b = 10
        a/b -> 0.6
        a//b -> 0 #Force le calcul à se faire en entier

    -Tuple/nuplet:
        a,b -> (4,3) #c'est juste une constante
    
    -Iterable
        s = 'bonjour'   l = [1, 2, 3]    t = (2, 3, 4) #Tuple
        s[0] -> 'b'     l[0] -> 1        t[0] -> 2
        s = 'bonjour'
        for c in s[::-1]
            print(s[c])-> 'r', 'u', 'o', 'j', 'n', 'o', 'b'
        for c in s[::2]
            print(s[c])-> 'b', 'n', 'o', 'r' #prends 1 sur 2

    -Zip
        s1 = 'abcd'
        s2 = '12345678'
        for e1,e2 in zip(s1,s2):
            print(e1,e2) -> 'a 1', 'b 2', 'c 3', 'd 4' #s'arrete quand 1/2 liste vide

    -Chaine de caractères
        s = 'bonjour'
         0  1  2  3  4  5  6
         B  O  N  J  O  U  R
        -7 -6 -5 -4 -3 -2 -1

        print(s[7]) -> ça plante
        print(s[-1]) -> 'R' #donne le dernier char

        On veut s = 'Bonjour'
        s[0] = 'B' -> ça plante
        s = 'B' + s[1:] -> 'Bonjour'1

        s = s[:-1] ->Lève le dernier char de la chaine

    -Liste
        s = 'bonjour'
        l = list(s)
        print(l)
        ['b', 'o', 'n', 'j', 'o', 'u', 'r']
        l[0]='B'
        print(l)
        ['B', 'o', 'n', 'j', 'o', 'u', 'r']

    -Tranches de chaines
        s[1:4] ->'onj'
        s[1:5] -> 'onjo'
        s[1:10] -> 'onjour'
        s[::-1] -> 'ruojnob' #donne la chaine à l'envers

    -Ajouter lettre dans une chaine
        s[0:3] + 'XXX' + s[3:7] -> 'bonXXXjour'
        ajoute avant le char selectionné
        s[:3] + 'XXX' + s[3:] -> 'bonXXXjour'
    
        
    -While Else
        while i<a/2:
            if a%i == 0:
                print(a, 'est divisible par', i)
                break
            i = i + 1
        else :
            print (a, 'est nombre premier)


    -Boucle For         While ( à la façon C)
                            i = 0
    for e in s :            while i < len(s):
        print(e)                print(s[i])
                                i+=1
    -Tester lettre dans str
    s = 'bonjour'
    if 'j' in s :


    -Exception
        import sys
        a = input("Entrez un nombre")
        try :
            a = float(a)
        except ValueError :
            print("Entrez un nombre svp")
            sys.exit()
        print("Merci")


        try :
            a = int(a)
            b = 1/a
        except ValueError :
            b=a=1
            print("Erreur de conversion dee a: a=1")
        except ZeroDivisionError:
            b = 10000
            print("a=0 donc b très grand (b=10000)")
        print("suite")

    -Affichage
        name = 'Casimir'
        weight = 140
        s = f"Il s'appelle {name} et pèse {weight} kilos"
        print(s)
        >>>Il s'appelle Casimir et pèse 140 kilos
        pi = 3.14159
        print(f'pi={pi :.2f}') -> 3.14
        
'''
print('bonjour')

#Structure IF / ELIF / ELSE
'''
a = 9
if a== 8 :
    print(a)
    a=a+1
elif a == 7:
    a = 5
else :
    if a == 9:
        a = 0
    else :
        a = 1
print('fin')
'''
#Print lettre par lettre chaine de char
'''
s = 'bonjour'
for e in s :
    print(e)
'''
#Definition d'une fonction
'''
def f(x):
    return 2*x;
'''
#Les slices
'''
#s = 'Monty Python'
s = 'bonjour'
print(s[6:10])
print(s[::-1])
'''
#Exercice
s = 'Hello Python!'
print(s[-1:-4:-1])
