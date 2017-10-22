# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup
import unidecode


ponct_liste = ['.',',','!','?',';',':']
midi_liste = ["midi","dejeuner","déjeuner","dejeune"]
cafete_liste = ["cafet","cafeteriat","cafetariat","bar","cafet"]
horaire_liste = ["horaire","horaires"]

#DOWNLOAD MENU
def download_menu():
    req = urllib.request.Request('http://services.telecom-bretagne.eu/rak/')
    the_page = urllib.request.urlopen(req)
    page = the_page.read()
    soup = BeautifulSoup(page, 'html.parser')
    plats = soup.find_all("td", attrs={"class" : "col-md-4"})
    nom_plats = soup.find_all("td", attrs={"align" : "left"})
    result = []
    premier_plat=0
    for i in range(len(plats)):
        a = str(plats[i].getText())
        b = str(nom_plats[i].getText())
        result.append([a[1:-1],b[2:-2]])
        if b[2:-2]=="Plat 1":
            if premier_plat==1:
                index = i
            else:
                premier_plat+=1
    return result,index



# BOITE A OUTILS
def depaquetage(sender,paquet,me,ponct_liste):
    if sender == me :                   # C'est un ack
        print('Reponse bien envoyee')
        return ['ack_msg']
    else :                              # Tous les messages que je reçois
        messaging = paquet['entry'][0]['messaging'][0]
        if 'message' in messaging.keys() :
            message = paquet['entry'][0]['messaging'][0]['message']
            if 'text' in message.keys():
                texte = message['text']  # Ce qu on nous a envoyé
                texte_notponct = extract_ponct(texte) # On retire la ponctuation
                mots_du_msg = texte_notponct.split(' ') # Nous séparons les mots
                return ['text_msg', texte, mots_du_msg]
            elif 'attachments' in message.keys():
                if message['attachments'][0]['type']=='location':
                    location = message['attachments'][0]['payload']['coordinates']
                    latitude = location['lat']
                    longitude = location['long']
                    return ['location_msg', latitude, longitude]
                elif message['attachments'][0]['type']=='image':
                    return ['image_msg']
                else : 
                    print(paquet)
                    print('message avec attachment inconnu!')           
            elif ('attachments'in message.keys()) and ('text' in paquet['entry'][0]['messaging'][0]['message'].keys()):
                print('Rien à répondre / attachment et text présent')
                return ['unknow_msg']
        elif 'postback' in messaging.keys() :
            postback = messaging['postback']['payload']
            return ['postback_msg' , postback]
        elif 'delivery' in messaging.keys() :
            return ['delivery_msg']
        elif 'read' in messaging.keys() :
            return ['read_msg']
        else : 
            print('Non identifié')
            print(paquet)
            return ['unknow_msg'] ## PAS UTILISE ENCORE


def similitudes (a,b):
    return list(set(a).intersection(b))

def extract_ponct(texte):
    texte = unidecode.unidecode(texte).lower()
    return texte

def build_choix():
    choix_dict = {}
    list_menu = ["Menu midi", "Menu soir", "Menu cafet", "Horaires", "Partager"]
    i=0
    for item in list_menu:
        choix_dict[i] = item
        i+=1
    return choix_dict

def construct_text(menu,mots_du_msg, index):
    texte = ''
    if ("menu" in mots_du_msg):
        if len(menu)<10: #Cas ou c'est le weekend et il n'y a pas de cafetariat
            if (similitudes(midi_liste, mots_du_msg) != []):
                texte = "Menu du midi :" + '\n\n'
                for i in range(len(menu)-4):
                    texte = texte + menu[i][1] + " : " + menu[i][0] + '\n\n'
            elif ("soir" in mots_du_msg):
                texte = "Menu du soir :" + '\n\n'
                for i in range(len(menu)-4,len(menu)):
                    texte = texte + menu[i][1] + " : " + menu[i][0] + '\n\n'
            elif similitudes(cafete_liste, mots_du_msg) != []:
                texte = "Il n'y a pas de menu de cafetariat aujourd'hui."
        else: # en semaine avec la cafetariat
            if (similitudes(midi_liste, mots_du_msg) != []):
                texte = "Menu du midi :" + '\n\n'
                for i in range(index):
                    texte = texte + menu[i][1] + " : " + menu[i][0] + '\n\n'
            elif ("soir" in mots_du_msg):
                texte = "Menu du soir :" + '\n\n'
                for i in range(index, len(menu) - 6):
                    texte = texte + menu[i][1] + " : " + menu[i][0] + '\n\n'
            elif similitudes(cafete_liste, mots_du_msg) != []:
                texte = "Menu de la cafet :" + '\n' + '\n' + \
                        menu[len(menu) - 6][1] + " : " + \
                        menu[len(menu) - 6][0] + '\n\n' + \
                        menu[len(menu) - 5][1] + " : " + \
                        menu[len(menu) - 5][0] + '\n\n' + \
                        menu[len(menu) - 4][1] + " : " + \
                        menu[len(menu) - 4][0] + '\n\n' + \
                        menu[len(menu) - 3][1] + " : " + \
                        menu[len(menu) - 3][0] + '\n\n' + \
                        menu[len(menu) - 2][1] + " : " + \
                        menu[len(menu) - 2][0] + '\n\n' + \
                        menu[len(menu) - 1][1] + " : " + \
                        menu[len(menu) - 1][0]
    else:
        if similitudes(horaire_liste, mots_du_msg) != []:
            texte = "RAK :\nLundi au vendredi \n" \
                    "11h30 - 13h15\n19h15 - 20h00\n\n" \
                    "Samedi - Dimanche - Jours feries \n" \
                    "12h15 - 13h\n19h15 - 20h00\n\n" \
                    "Vacances scolaires \n11h45 - 13h" \
                    "\n19h30 - 20h\n\n" \
                    "BAR :\nLundi au vendredi" \
                    " \n7h30 - 16h45"
        elif ("partager" in mots_du_msg):
            texte = "partager"
        elif ("menu" in mots_du_msg):
            texte = "Tu veux quel type de menu ? Appuie sur les boutons ci dessous"
        else:
            texte = "Je suis là que pour donner le menu ne m'en demandes pas trop! 😉"

    return texte


