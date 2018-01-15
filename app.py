# coding: utf-8
import traceback
import json
from config import me, token, FB_VERIFY_TOKEN
from flask import request
from send import *
from toolkit import depaquetage, build_choix, ponct_liste, construct_text, download_menu

def webhook_get():
    choix_dict = build_choix()
    try:
        data = json.loads(request.data.decode())  #recupere le message envoye a notre chatbot
        sender = data['entry'][0]['messaging'][0]['sender']['id']   # Qui nous l a envoye
        depaquet = depaquetage(sender,data,me,ponct_liste)
        type_msg_recu = depaquet[0]
        if type_msg_recu == 'text_msg':
            type_msg_recu, texte, mots_du_msg = depaquet
            dejeuner,diner,cafete = download_menu()
            text = construct_text(dejeuner,diner,cafete,mots_du_msg)
            if text == "partager":
                send_paquet(token, send_share(sender))
                return "nothing"
            elif text == "recharge":
                link = "https://services.ard.fr/fr/espaces-clients/etablissements/enst/accueil.html?logintype=logout"
                title = "Recharge de compte RAK"
                subtitle = "Cliquez pour accéder au site du RAK"
                image_url = "http://services.telecom-bretagne.eu/rak/images/rak_logo.jpg"
                nom_button = "Recharger"
                send_paquet(token, send_msg_button1_web(sender,title,subtitle,link,image_url,nom_button))
                return "nothing"
            elif text=='ker':
                text = "Ta réponse a été enregistrée! \n\nCitation du jour :\n 23 à 0 ! C'est la piquette Jack ! Tu sais pas jouer Jack ! T'es mauvais ! "
            elif text == 'breizh':
                text = 'Ta réponse a été enregistrée! \n\nCitation du jour :\n Est-ce que tout cela est légal ? PAS DU TOUT! '
            elif text =='aucune':
                text = 'Ta réponse a été enregistrée!'
            senderator(token,sender, text, choix_dict)
            if "midi" in text:
                texte1 = "⚠ SONDAGE ⚠ : Nous voilà à mis chemin de la campagne electorale, un sondage s'impose. Quelle est la meilleure liste selon toi ?"
                payload = send_choix_multiple(sender,texte1,campagne)
                send_paquet(token,payload)
        else:
            print(type_msg_recu)
    except Exception :
                print(traceback.format_exc())
    return "Nothing"

campagne = { 'item0': { "title":"Loup Breizh St","payload":"loup", "image_url":"https://pbs.twimg.com/profile_images/952183042562576384/71h_JsH-_400x400.jpg" },
             'item1': { "title":"Ker Nid d'espion","payload":"ker", "image_url":"https://s1.qwant.com/thumbr/0x0/b/9/1ec3c878834fda31c6f654c7172b56/b_1_q_0_p_0.jpg?u=http%3A%2F%2Fimages.movieplayer.it%2Ft%2Fimages%2F2003%2F12%2F24%2Fla-locandina-di-oss-117-le-caire-nid-d-espions-36396_jpg_221x221_crop_q85.jpg" },
             'item2': { "title":"Aucune","payload":"aucune", "image_url":"" }
            }
