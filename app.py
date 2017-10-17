# coding: utf-8
import traceback
import json
from config import me, token, FB_VERIFY_TOKEN
from flask import request
from send import senderator, send_share, send_paquet
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
            menu, index = download_menu()
            text = construct_text(menu,mots_du_msg, index)
            if text == "partager":
                send_paquet(token, send_share(sender))
                return "nothing"
            senderator(token,sender, text, choix_dict)
        else:
            print(type_msg_recu)
    except Exception :
                print(traceback.format_exc())
    return "Nothing"
