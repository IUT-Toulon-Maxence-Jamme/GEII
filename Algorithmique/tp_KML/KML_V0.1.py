import colorsys

def nbLinesFile(filename):
    fichier = open(filename,'r')
    texte = fichier.readlines()
    nb = len(texte)
    fichier.close()
    return nb

def clone_ligne(filename1,filename2,filename3,nbl):
    fichier1 = open(filename1,'r')
    fichier2 = open(filename2,'w')#file with only $GPGGA
    fichier3 = open(filename3,'w')#file with only $GPVTG
    for i in range(nbl):
        texte = fichier1.readline()
        if "$GPGGA" == texte[0:6]:
            fichier2.write(str(texte))
        elif "$GPVTG" == texte[0:6]:
            texte = texte.strip()
            if(chksum(texte)):
                fichier3.write(str(texte)+"\n")

def read_data_pos(filename2,nbl):
    fichier = open(filename2,'r')
    data = []
    for i in range(nbl):
        ligne = fichier.readline()        
        ligne = ligne.split(",")
        d = []
        degres = int(ligne[2][0:2])
        minute = float(ligne[2][2:])
        minute = minute/60
        if ligne[3] == "S":
            minute = -minute
        d.append(minute+degres)
        
        degres = int(ligne[4][0:3])
        minute = float(ligne[4][3:])
        minute = minute/60
        if ligne[5] == "O":
            minute = -minute
        d.append(minute+degres)
        d.append(ligne[9])
        data.append(d)        
    return data

def creation_fichier(nouveau_fichier_name,fichier_debut_name,data,fichier_fin_name):
    nouveau_fichier = open(nouveau_fichier_name,'w')
    
    debut_texte = ""
    nbl = nbLinesFile(fichier_debut_name)
    fichier_debut = open(fichier_debut_name,'r')
    for i in range(nbl):
        debut_texte += str(fichier_debut.readline())
        
    fin_texte = ""
    nbl = nbLinesFile(fichier_fin_name)
    fichier_fin = open(fichier_fin_name,'r')
    for i in range(nbl):
        fin_texte += str(fichier_fin.readline())
        
    millieu_text = ""
    for i in range(len(data)):
        millieu_text += str(data[i][1]) + "," + str(data[i][0]) + "," + str(data[i][2])+ "\n"

    nouveau_fichier.write(str(debut_texte)+str(millieu_text)+str(fin_texte))
def speedToHue( speed, speedMin=0 , speedMax=100, hueMin=140,hueMax=0):
    if speed < 0:
        speed = 0
    elif speed > 100:
        speed = 100
    m = -hueMin / speedMax
    p = hueMin
    hue = speed * m + p
    return hue

def colorKml(hue, sat, value):
    kmlColor = colorsys.hsv_to_rgb(hue, sat, value)
    return kmlColor

def xrange(x):
    return iter(range(x))

def chksum(inp): # GPS message checksum verification
	if not inp.startswith("$"): return False
	if not inp[-3:].startswith("*"): return False
	payload = inp[1:-3]
	checksum = 0
	for i in xrange(len(payload)):
		checksum =  checksum ^ ord(payload[i])
	return ("%02X" % checksum) == inp[-2:]
    
def read_data_speed(filename7,nbl):
    fichier = open(filename7,'r')
    data = []
    for i in range(nbl):
        ligne = fichier.readline()        
        ligne = ligne.split(",")
        d = []
        d.append(ligne[7])
        data.append(d)
    return data

def creation_fichier_2(fichier_debut_name,fichier_millieu_name,fichier_fin_name,data_position,data_speed,nouveau_fichier_name,N):
    nouveau_fichier = open(nouveau_fichier_name,'w')
    
    debut_texte = ""
    nbl = nbLinesFile(fichier_debut_name)
    fichier_debut = open(fichier_debut_name,'r')
    for i in range(nbl):
        debut_texte += str(fichier_debut.readline())

    millieu_texte = ""
    nbl = nbLinesFile(fichier_millieu_name)
    fichier_millieu = open(fichier_millieu_name,'r')
    for i in range(nbl):
        millieu_texte += str(fichier_millieu.readline())
    millieu_texte = millieu_texte.replace("COULEUR", "INDEX1")
    millieu_texte = millieu_texte.replace("COORDONEE", "INDEX2")
    print(millieu_texte)
    fin_texte = ""
    nbl = nbLinesFile(fichier_fin_name)
    fichier_fin = open(fichier_fin_name,'r')
    for i in range(nbl):
        fin_texte += str(fichier_fin.readline())
        
    #place mark creation
    print(len(data_position), len(data_speed))
    #for i in data_position:
        

    #nouveau_fichier.write(str(debut_texte)+str(millieu_text)+str(fin_texte))
    
if __name__ == '__main__':
    filename1 = 'balade_gps.txt' #fichier qui sort de l'application
    filename2 = 'Clone_balade_gps.txt' #fichier avec uniquement les infos $GPGGA
    filename3 = 'Clone_balade_gps - Copie.txt' #fichier test pour $GPGGA
    filename4 = 'debut_XML.txt'
    filename5 = 'fin_XML.txt'
    filename6 = 'Fichier_XML.txt'
    filename7 = 'Clone_balade_gps_2.txt' #fichier avec uniquement les infos $GPVTG
    filename8 = 'Clone_balade_gps_2 - Copie.txt' #fichier test pour $GPVTG
    filename9 = 'debut_XML_2.txt'
    filename10 = 'millieu_XML_2.txt'
    filename11 = 'fin_XML_2.txt'
    filename12 = 'nouveau_XML.txt'
    nombre_ligne1 = nbLinesFile(filename1)
    clone_ligne(filename1,filename2,filename7,nombre_ligne1)#creation file with only good $
    
    test = 0
    if test == 0:#test code
        #nombre_ligne3 = nbLinesFile(filename3)
        #data = read_data(filename3,nombre_ligne3)
        #nombre_ligne8 = nbLinesFile(filename8)
        #verif_cksum(filename8,nombre_ligne8)
        #r,g,b =colorsys.hsv_to_rgb(speedToHue( 0, speedMin=0 , speedMax=100, hueMin=140,hueMax=0), 255, 255)
        #print(r,g,b)
        #nombre_ligne8 = nbLinesFile(filename8)
        #data_speed = read_data_speed(filename8,nombre_ligne8)
        #print(data_speed)
        hue = speedToHue( 0, speedMin=0 , speedMax=100, hueMin=140,hueMax=0)
        print(hue)
        print(colorKml(hue/360, 1, 1))
    elif test == 1: #clasic code
        nombre_ligne2 = nbLinesFile(filename2)
        data_position = read_data_pos(filename2,nombre_ligne2)
        print(data_position)

        nombre_ligne7 = nbLinesFile(filename7)
        data_speed = read_data_speed(filename7,nombre_ligne7)
        print(data_speed)
        N = 5
        creation_fichier_2(filename9,filename10,filename11,data_position,data_speed,filename12,N)
        #creation_fichier(filename6,filename4,data,filename5)#creation of KML file for trajet
    
        
        
    



    
