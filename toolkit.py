# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup
import unidecode
from send import *

ponct_liste = ['.',',','!','?',';',':','-']
midi_liste = ["midi","dejeuner","déjeuner","dejeune"]
cafete_liste = ["cafet","cafeteriat","cafetariat","bar","cafete"]
horaire_liste = ["horaire","horaires"]
thanks_liste = ["merci","thanks"]
bonjour_liste = ["salut","bonjour","hi","hello","coucou"]
vulgarite_liste = ['tg','moche','nul','fdp','gueule','tagueule','connard','pd','idiot','encule','salop','ntm','nique','fuck','tocar','tocard'] 
info_liste = ['langage','language','version','info','information','code','createur','proprietaire','concepteur']
recharge_liste = ['recharge','recharger']

#DOWNLOAD MENU
def download_menu():
    req = urllib.request.Request('http://services.telecom-bretagne.eu/rak/')
    the_page = urllib.request.urlopen(req)
    page = the_page.read()
    soup = BeautifulSoup(page, 'html.parser')
    plats = soup.find_all("td", attrs={"class" : "col-md-4"})
    nom_plats = soup.find_all("td", attrs={"align" : "left"})
    dejeuner = []
    diner = []
    cafete = []
    #print(plats)
    for i in range(len(plats)):
        if 'cafeteria' in plats[i].find_all('a',href=True)[0]['href']:
            a = str(plats[i].getText())
            b = str(nom_plats[i].getText())
            cafete.append([a[1:-1],b[2:-2]])
            pass
        elif 'dejeuner' in plats[i].find_all('a',href=True)[0]['href']:
            a = str(plats[i].getText())
            b = str(nom_plats[i].getText())
            dejeuner.append([a[1:-1],b[2:-2]])
            pass
        elif 'diner' in plats[i].find_all('a',href=True)[0]['href']:
            a = str(plats[i].getText())
            b = str(nom_plats[i].getText())
            diner.append([a[1:-1],b[2:-2]])
            pass
    return dejeuner,diner,cafete



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
    l=''
    for i in texte:
        if i in ponct_liste:
            l=l+" "
        else : 
            l=l+i
    return l

def build_choix():
    choix_dict = {}
    list_menu = ["Menu midi", "Menu soir", "Menu cafete", "Horaires", "Recharge","Partager"]
    i=0
    for item in list_menu:
        choix_dict[i] = item
        i+=1
    return choix_dict

def construct_text(dejeuner,diner,cafete,mots_du_msg):
    texte = ''
    #print('le dej : ',dejeuner)
    #print('le diner : ',diner)
    #print('la cafete : ',cafete)
    print(mots_du_msg)
    if ("menu" in mots_du_msg):
        if (similitudes(midi_liste, mots_du_msg) != []):
            #print(dejeuner)
            if len(dejeuner)==0:
                texte = "Menu du midi indisponible aujourd'hui. Le Rak ne l'a pas diffusé."
            else:
                texte = "Menu du midi :" + '\n\n'
                for i in range(len(dejeuner)):
                    texte = texte + dejeuner[i][1] + " : " + dejeuner[i][0] + '\n\n'
        elif ("soir" in mots_du_msg):
            if len(diner)==0:
                texte = "Menu du soir indisponible aujourd'hui. Le Rak ne l'a pas diffusé."
            else:    
                texte = "Menu du soir :" + '\n\n'
                for i in range(len(diner)):
                    texte = texte + diner[i][1] + " : " + diner[i][0] + '\n\n'
        elif similitudes(cafete_liste, mots_du_msg) != []:
            if len(cafete)==0:
                texte = "Menu de la cafetariat indisponible aujourd'hui. Le Rak ne l'a pas diffusé."
            else:    
                texte = "Menu de la cafete :" + '\n\n'
                for i in range(len(cafete)):
                    texte = texte + cafete[i][1] + " : " + cafete[i][0] + '\n\n'
        else:
            texte = "Tu veux quel type de menu ? Appuie sur les boutons ci dessous"
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
        elif ("partager" in mots_du_msg) or ("share" in mots_du_msg):
            texte = "partager"
        elif similitudes(recharge_liste,mots_du_msg) != []:
            texte = "recharge"
        elif similitudes(thanks_liste, mots_du_msg) != []:
            texte = "Pas besoin de me remercier je suis là pour te servir!"
        elif similitudes(bonjour_liste, mots_du_msg) != []:
            texte = "Salut, content de te voir ici!"
        elif similitudes(vulgarite_liste,mots_du_msg) !=[]:
            texte = "T'es pas cool avec moi, tu dois surement avoir faim :"
        elif ("pyrak" in mots_du_msg):
            texte = "Mon nom est Pyrak, mais sais tu pourquoi? C'est une contraction de PY pour python et RAK pour le nom de la cantine. "
        elif ("rak" in mots_du_msg):
            texte = "Tu veux peut être savoir ce que veut dire RAK ? Ceci signifie Restaurant Associatif de Kernevent."
        elif similitudes(info_liste,mots_du_msg) !=[] or (('qui' in mots_du_msg) and ('es' in mots_du_msg) and ('tu' in mots_du_msg)):
            texte = "Je suis un chatbot codé en langage python pour plus d'info s'adresser à mon créateur, Florian Blanchet."
        elif ("breizh" in mots_du_msg):
            texte = "breizh"
        elif ("ker" in mots_du_msg):
            texte = "ker"
        elif ("aucune" in mots_du_msg):
            texte = "aucune"
        else:
            texte = "Je suis là que pour donner le menu ne m'en demande pas trop! 😉"

    return texte
