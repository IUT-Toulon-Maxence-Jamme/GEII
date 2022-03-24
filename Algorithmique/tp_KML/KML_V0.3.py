import colorsys
#https://www.google.com/maps/d/u/0/edit?mid=14Jc84ruxE90k4qW-MzQ2hXDXWJctJERd&ll=43.13480239225014%2C6.014363500000011&z=15

def nbLinesFile(filename):
    fichier = open(filename,'r')
    nb = len(fichier.readlines())#number of lines
    fichier.close()
    return nb

def chksum(inp): # GPS message checksum verification
	if not inp.startswith("$"): return False
	if not inp[-3:].startswith("*"): return False
	payload = inp[1:-3]
	checksum = 0
	for i in iter(range(len(payload))):
		checksum =  checksum ^ ord(payload[i])
	return ("%02X" % checksum) == inp[-2:]

def clone_ligne(filename1,filename2,filename3,nbl):
    fichier1 = open(filename1,'r')#file with all GPS data
    fichier2 = open(filename2,'w')#file with only $GPGGA
    fichier3 = open(filename3,'w')#file with only $GPVTG
    for i in range(nbl):
        texte = fichier1.readline()
        if "$GPGGA" == texte[0:6]:
            texte = texte.strip()
            if(chksum(texte)): #add in file if checksum is good
                fichier2.write(str(texte)+"\n")
        elif "$GPVTG" == texte[0:6]:
            texte = texte.strip()
            if(chksum(texte)):#add in file if checksum is good
                fichier3.write(str(texte)+"\n")
    fichier1.close()
    fichier2.close()
    fichier3.close()

def read_data_pos(filename,nbl):
    fichier = open(filename,'r')
    data = []
    for i in range(nbl):
        ligne = fichier.readline()        
        ligne = ligne.split(",")
        d = []
        #Longitude
        degres = int(ligne[4][0:3])
        minute = float(ligne[4][3:])
        minute = minute/60
        if ligne[5] == "O":
            minute = -minute
        d.append(minute+degres)
        #Latitude
        degres = int(ligne[2][0:2])
        minute = float(ligne[2][2:])
        minute = minute/60
        if ligne[3] == "S":
            minute = -minute
        d.append(minute+degres)
        #Altitude
        d.append(ligne[9])
        #add in data
        data.append(d)
    fichier.close()
    return data

def read_data_speed(filename,nbl):
    fichier = open(filename,'r')
    data = []
    for i in range(nbl):
        ligne = fichier.readline()        
        ligne = ligne.split(",")
        data.append(ligne[7])
    fichier.close()
    return data

def min_max_speed(l):
    a,b = 100,0
    for i in range(len(data_speed)):
        if float(data_speed[i]) < a :
            a = float(data_speed[i])
        if float(data_speed[i]) > b :
            b = float(data_speed[i])
    return a,b

def speedToHue( speed, speedMin, speedMax, hueMin=140,hueMax=0):
    if speed < speedMin:
        speed = speedMin
    elif speed > speedMax:
        speed = speedMax
    m = -hueMin / speedMax
    p = hueMin
    hue = speed * m + p
    return hue

def colorKml(hue, sat, value):
    (r, g, b) = colorsys.hsv_to_rgb(hue, sat, value)
    (r, g, b) = (r*255, g*255, b*255)
    kmlColor = "#FF" + ("0x%02X" % int(b))[2:] + ("0x%02X" % int(g))[2:] + ("0x%02X" % int(r))[2:]
    return kmlColor #return FFEA4902 for exemple

def creation_placemark(a,l,pacemarque_texte_model):
    texte_placemark = pacemarque_texte_model
    coordonne_text = ""
    for i in range(len(l)):
        coordonne_text += str(l[i][1][0]) + "," + str(l[i][1][1]) + "," + str(l[i][1][2])+ "\n"
    hue = speedToHue( int(a), min_speed, max_speed, hueMin=140,hueMax=0)
    color = colorKml(hue/360, 1, 1)
    texte_placemark = texte_placemark.replace("COULEUR", color)
    texte_placemark = texte_placemark.replace("COORDONEE", coordonne_text)
    return texte_placemark


def creation_fichier_2(KML_sans_placemark,KML_avec_placemark,data_position,data_speed,nouveau_fichier_name,N):
    nouveau_fichier = open(nouveau_fichier_name,'w')
    texte = ""
    nbl = nbLinesFile(KML_sans_placemark)
    fichier_KML_sans_placemark = open(KML_sans_placemark,'r')
    for i in range(nbl):
        texte += str(fichier_KML_sans_placemark.readline())
    fichier_KML_sans_placemark.close()
    #separation with a word in the file.txt
    texte = texte.split("SEPARATION")
    debut_texte = texte[0]
    fin_texte = texte[1]

    pacemarque_texte_model = ""
    nbl = nbLinesFile(KML_avec_placemark)
    fichier_KML_avec_placemark = open(KML_avec_placemark,'r')
    for i in range(nbl):
        pacemarque_texte_model += str(fichier_KML_avec_placemark.readline())
    fichier_KML_avec_placemark.close()
    
        
    #place mark creation
    a = 0
    l = []
    texte_placemark = ""
    for i in range(len(data_speed)):
        if abs(a-float(data_speed[i]))>N:
            texte_placemark += creation_placemark(a,l,pacemarque_texte_model)
            test = 1
            try:
                m = l[-1]
            except IndexError:
               test = 0
            if test == 1:
                l = []
                l.append(m)
                a = float(data_speed[i])
        m = []   
        m.append(float(data_speed[i]))
        m.append(data_position[i])
        l.append(m)
    texte_placemark += creation_placemark(a,l,pacemarque_texte_model)
    
    nouveau_fichier.write(str(debut_texte)+texte_placemark+str(fin_texte))
    nouveau_fichier.close()
        
        
if __name__ == '__main__':
    filename1 = 'balade_gps.txt' #fichier qui sort de l'application
    filename2 = 'POSITION_balade_gps.txt' #fichier avec uniquement les infos $GPGGA
    filename7 = 'SPEED_balade_gps.txt' #fichier avec uniquement les infos $GPVTG
    filename9 = 'KML_sans_placemark.txt' #fichier KML sans placemark
    filename10 = 'KML_avec_placemark.txt' #fichier KML placemark uniquement
    filename12 = 'Nouveau_KML.kml'

    #creation file with only good $ 
    clone_ligne(filename1,filename2,filename7,nbLinesFile(filename1))

    #creation liste with only important data
    data_position = read_data_pos(filename2,nbLinesFile(filename2))
    print(data_position)
    data_speed = read_data_speed(filename7,nbLinesFile(filename7))
    print(data_speed)
    #find min & max in the speed data
    min_speed, max_speed = min_max_speed(data_speed)
    print("min =",min_speed, "Km/h \nmax =", max_speed,"Km/h")

    #creation du KML
    N = 30 #nombre de Km/h par segment
    creation_fichier_2(filename9,filename10,data_position,data_speed,filename12,N)
    print("Fichier uptade avec des segments variant pour",N,"Km/H")
