import colorsys
#https://www.google.com/maps/d/u/0/edit?mid=14Jc84ruxE90k4qW-MzQ2hXDXWJctJERd&ll=43.13480239225014%2C6.014363500000011&z=15

def nbLinesFile(filename): #renvoie le nombre de ligne d'un fichier
    file = open(filename,'r')
    lines = len(file.readlines())#nombre de lignes
    file.close()
    return lines

def chksum(inp): #renvoie le checksum d'une trame
	if not inp.startswith("$"): return False
	if not inp[-3:].startswith("*"): return False
	payload = inp[1:-3]
	checksum = 0 # GPS message checksum verification
	for i in iter(range(len(payload))):
		checksum =  checksum ^ ord(payload[i])
	return ("%02X" % checksum) == inp[-2:] #retourne true si le checksum calculer est égal à celui de la trame

def clone_ligne(filename1,filename2,filename3,nbl): #clone les lignes que nous souhaitons du fichier source (avec verifcation de checksum)
    file = open(filename1,'r')#fichier avec tout les GPS data
    file_GPGGA = open(filename2,'w')#fichier avec uniquement les $GPGGA
    file_GPVTG = open(filename3,'w')#fichier avec uniquement les $GPVTG
    for i in range(nbl):
        texte = file.readline()
        if "$GPGGA" == texte[0:6]:
            texte = texte.strip()
            if(chksum(texte)): #Ajout au fichier si le checksum est bon
                file_GPGGA.write(str(texte)+"\n")
        elif "$GPVTG" == texte[0:6]:
            texte = texte.strip()
            if(chksum(texte)):#Ajout au fichier si le checksum est bon
                file_GPVTG.write(str(texte)+"\n")
    file.close()
    file_GPGGA.close()
    file_GPVTG.close()

def read_data_pos(filename,nbl):#Lis les positions et les ajoutes à une liste
    file = open(filename,'r')
    data = []
    for i in range(nbl):
        ligne = file.readline()        
        ligne = ligne.split(",")
        d = []
        #Calcul de la Longitude
        degres = int(ligne[4][0:3])
        minute = float(ligne[4][3:])
        minute = minute/60
        if ligne[5] == "O":
            minute = -minute
        d.append(minute+degres)
        #Calcul de la Latitude
        degres = int(ligne[2][0:2])
        minute = float(ligne[2][2:])
        minute = minute/60
        if ligne[3] == "S":
            minute = -minute
        d.append(minute+degres)
        #Ajout de l'Altitude
        d.append(ligne[9])
        #Ajout des 3 à data
        data.append(d)
    file.close()
    return data

def read_data_speed(filename,nbl):#Lis les vitesses et les ajoutes à une liste
    file = open(filename,'r')
    data = []
    for i in range(nbl):
        line = file.readline()        
        line = line.split(",")
        data.append(float(line[7]))#position de la vitesse dans la chaine
    file.close()
    return data

def speedToHue( speed, speedMin, speedMax, hueMin=140,hueMax=0): #retourne la valeur de hue entre 0 et 140 proportionnellement à la vitesse
    m = -hueMin / speedMax
    p = hueMin
    hue = speed * m + p
    return hue

def colorKml(hue, sat=1, value=1): #retrourne la couleur au format KML
    (r, g, b) = colorsys.hsv_to_rgb(hue, sat, value)
    (r, g, b) = (r*255, g*255, b*255)
    kmlColor = "#FF" + ("0x%02X" % int(b))[2:] + ("0x%02X" % int(g))[2:] + ("0x%02X" % int(r))[2:] #int(r))[2:] evite d'avoir le 0x du format hex
    return kmlColor #retourne FFEA4902 par exemple

def creation_placemark(speed,l,placemarque_texte_model):
    texte_placemark = placemarque_texte_model
    coordonne_text = ""
    for i in range(len(l)):
        coordonne_text += str(l[i][1][0]) + "," + str(l[i][1][1]) + "," + str(l[i][1][2])+ "\n"
    hue = speedToHue( int(speed), min_speed, max_speed, hueMin=140,hueMax=0)
    color = colorKml(hue/360, 1, 1)#division par 360(max) pour normaliser entre 0 et 1
    texte_placemark = texte_placemark.replace("COULEUR", color) ##Fichier placemark modifier COULEUR -> place de la vrai couleur
    texte_placemark = texte_placemark.replace("COORDONEE", coordonne_text)##idem, fichier placemark modifier COORDONEE -> place des vrai coordonées au bon format
    return texte_placemark #return un block place mark avec aucune modif à rajouter


def creation_file_kml(KML_sans_placemark,KML_avec_placemark,data_position,data_speed,nouveau_fichier_name,N):
    nouveau_fichier = open(nouveau_fichier_name,'w')
    texte = ""
    nbl = nbLinesFile(KML_sans_placemark)
    fichier_KML_sans_placemark = open(KML_sans_placemark,'r')
    for i in range(nbl):
        texte += str(fichier_KML_sans_placemark.readline())
    fichier_KML_sans_placemark.close()
    #separe le fichier file.txt en deux à partir du mot "SEPARATION" 
    texte = texte.split("SEPARATION")
    debut_texte = texte[0]
    fin_texte = texte[1]

    #creation de la string pacemarque_texte_model
    pacemarque_texte_model = ""
    nbl = nbLinesFile(KML_avec_placemark)
    fichier_KML_avec_placemark = open(KML_avec_placemark,'r')
    for i in range(nbl):
        pacemarque_texte_model += str(fichier_KML_avec_placemark.readline())
    fichier_KML_avec_placemark.close()
    
        
    #Remplissage des placemarks
    speed = 0
    list_position = []
    texte_placemark = ""
    for i in range(len(data_speed)):
        if abs(speed-float(data_speed[i]))>N:#permet de faire des segments de N Km/H
            texte_placemark += creation_placemark(speed,list_position,pacemarque_texte_model)#ajoute à la string le segment actuel
            test = 1
            try:
                m = l[-1] #permet de garder le dernier point en mémoire
            except IndexError: #lorsqu'on a une liste vide -> IndexError
               test = 0
            if test == 1:
                list_position = []
                list_position.append(m)
                speed = float(data_speed[i])
        m = []   
        m.append(float(data_speed[i]))
        m.append(data_position[i])
        list_position.append(m)
    texte_placemark += creation_placemark(speed,list_position,pacemarque_texte_model)#ajouter le dernier segment qui n'est pas pris dans la boucle

    #ecrit le fichier KML avec les 3 string
    nouveau_fichier.write(str(debut_texte)+texte_placemark+str(fin_texte))
    nouveau_fichier.close()
        
        
if __name__ == '__main__':
    #fichier requis
    filename1 = 'balade_gps.txt' #fichier qui sort de l'application
    filename9 = 'KML_sans_placemark.txt' #fichier KML sans placemark
    filename10 = 'KML_avec_placemark.txt' #fichier KML placemark uniquement
    #fichier crée
    filename2 = 'POSITION_balade_gps.txt' #fichier avec uniquement les infos $GPGGA
    filename7 = 'SPEED_balade_gps.txt' #fichier avec uniquement les infos $GPVTG
    filename12 = 'Nouveau_KML.kml' #fichier KML 

    #creation des fichiers avec les bonnes trames
    clone_ligne(filename1,filename2,filename7,nbLinesFile(filename1))

    #creation de listes avec uniquement les informations souhaiter
    data_position = read_data_pos(filename2,nbLinesFile(filename2))
    data_speed = read_data_speed(filename7,nbLinesFile(filename7))
    
    #definition de la vitesse min & max pour avoir une meilleur variation des couleurs sur le rendu
    min_speed, max_speed = min(data_speed),max(data_speed)

    #creation du KML
    N = 3 #nombre de Km/h par segment
    creation_file_kml(filename9,filename10,data_position,data_speed,filename12,N)
    print("Fichier uptade avec des segments variant pour",N,"Km/H")
