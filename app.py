# coding: utf-8
import os
import requests
import traceback
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from toolkit import *
from send import *
import urllib.request
from bs4 import BeautifulSoup

#token = os.environ.get('FB_ACCESS_TOKEN')
token = 'EAAFo1IiXrQwBABjWTFk7ZA4XL2kmhFt6M0t0pTjJWSGRppsTWQOYI7Lylcub4899ZBpZBOHz3N4CfvABclqw7ZA5CNZB1JtfhtFEVShC8KP3ZB3GLqmc5RLtnBX3WGl1aMM0zYvm6DAxIvCeOXem1YsFqpcVsrp1pZAzpkeF0QeCAZDZD'
#FB_VERIFY_TOKEN =os.environ.get('FB_VERIFY_TOKEN')
FB_VERIFY_TOKEN = 'test_token'
me = '1437816462930392' #ID de l'app

app = Flask("app")  #instance de la classe FLask. premier argument est le nom


print('     /$$$$$$$$\                  /$$   $$    ')
print('    | $$    |$$                 | $$  $$     ')
print('    | $$    | $$    /$$$$$$$    | $$ $$      ')
print('    | $$$$$$$$$$   |_______$$   | $$$$       ')
print('    | $$    \ $$    /$$$$$$$$   | $$ $$      ')
print('    | $$     \ $$  |$$__   $$   | $$  $$     ')
print('    | $$      \ $$ | $$$$$$$$   | $$ \ $$    ')
print('    |__/       \_/  \_______/   |__/  |_/    ')

@app.route('/', methods=['GET', 'POST']) #A decorator that is used to register a view function for a given URL rule.Ici rule = / et en option les methodes assignées à ce rule
def webhook():
    global start_time
    if request.method == 'POST':  # Toutes les requetes post passent par la ; dans les deux sens
        try:
            data = json.loads(request.data.decode())  #recupere le message envoye a notre chatbot
            sender = data['entry'][0]['messaging'][0]['sender']['id']   # Qui nous l a envoye
            depaquet = depaquetage(sender,data,me,ponct_liste)
            print(depaquet)
            type_msg_recu = depaquet[0]
            if type_msg_recu == 'text_msg' :
                type_msg_recu, texte, mots_du_msg=depaquet
                menu=download_menu()
                print(menu)
                if ("menu" in mots_du_msg) and ("midi" in mots_du_msg):
                    texte ="Menu du midi :"+'\n'+'\n' "Entrée chaude : " +menu[0]+'\n' +"Plat 1 : "+ menu[1]+'\n'+"Accompagnement 1 : " + menu[2]+'\n'+"Plat 2 : " + menu[3]+'\n'+"Accompagnement 2 : "  + menu[4]+'\n'+"Plat 3 "+ menu[5]+'\n'+"Accompagnement 3 : " + menu[6]+'\n'+"Dessert chaud : "+menu[7]
                    payload = send_text(sender,texte)
                    send_paquet(token,payload)
                    print('Repas midi envoyé')
                    return 'nothing'
                elif ("menu" in mots_du_msg) and ("soir" in mots_du_msg):
                    texte ="Menu du soir :"+'\n'+'\n' "Plat 1 : "+ menu[8]+'\n'+"Accompagnement 1 : " + menu[9]+'\n'+"Plat 2 : "+menu[10]
                    payload = send_text(sender,texte)
                    send_paquet(token,payload)
                    print('Repas soir envoyé')
                    return 'nothing'
                elif ("cafet" in mots_du_msg) or ("cafete" in mots_du_msg):
                    texte ="Menu de la cafete :"+'\n'+'\n' +"salade 1 : "+ menu[11]+'\n'+"salade 2 : " + menu[12]+'\n'+"salade 3 : "+menu[13]+'\n' +"sandwich 1 : "+ menu[14]+'\n'+"sandwich 2 : " + menu[15]+'\n'+"sandwich 3 : "+menu[16]
                    payload = send_text(sender,texte)
                    send_paquet(token,payload)
                    print('Repas soir envoyé')
                    return 'nothing'

        except Exception as e:
                    print(traceback.format_exc())
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return "Nothing"

ponct_liste = ['.',',','!','?',';',':']
meteo_img = 'http://ian.umces.edu/imagelibrary/albums/userpics/12865/normal_ian-symbol-weather-solar-radiation.png'
actu_img = 'http://icons.iconarchive.com/icons/zerode/plump/256/Network-Earth-icon.png'
wiki_img = 'http://www.icone-png.com/png/25/24983.png'
date_img = 'https://cdn2.iconfinder.com/data/icons/perfect-flat-icons-2/512/Date_calendar_event_month_time_day_vector.png'
pomme_img = 'https://s2.qwant.com/thumbr/0x0/5/8/3078a9585992fbea80e57c386326b7/b_1_q_0_p_0.jpg?u=http%3A%2F%2Fwww.free-icons-download.net%2Fimages%2Fred-apple-icon-54633.png&q=0&b=1&p=0&a=1' 
snake_img = 'http://www.indir.org/icon/classic_snake_2_icon.png'      

#DOWNLOAD MENU
def download_menu():
    req = urllib.request.Request('http://services.telecom-bretagne.eu/rak/')
    the_page = urllib.request.urlopen(req)
    page = the_page.read()
    soup = BeautifulSoup(page, 'html.parser')
    plats = soup.find_all("td", attrs={"class" : "col-md-4"})
    result = []
    for plat in plats:
        a = str(plat.getText())
        result.append(a[1:-1])
    return result


# ENVOYER UN PAYLOAD
def send_paquet(sender,payload):
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    print(r.text) # affiche la reponse à l'envoit; pratique si veut l'ID ou voir si bien envoyé
    pass

def send_webview(sender,title1,subtitle1,image_url1,link1,payload1):
    payload = {
    "recipient": {
      "id": sender
    },
    "message": {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "elements": [{
            "title": title1,
            "subtitle": subtitle1,
            "item_url": link1,               
            "image_url": image_url1,
            "buttons": [{
              "type": "web_url",
              "url": link1,
              "title": "Ouvre le lien"
            }, {
              "type": "web_url",
              "url":'https://m.me/mrjesaistout?ref=take_quiz',
              "title": "webview",
              "webview_height_ratio": "compact",
              "messenger_extensions": True
            }],
          }]
        }
      }
    }
    }
    return payload
def whitelist():
    payload = {
    "whitelisted_domains":[
    "https://m.me/mrjesaistout"
    ]
    }
    return payload 

# INTERACTION UTILISATEUR PAS ENCORE UTILISE
def msg_seen(sender):
    payload = {
        "recipient":{
            "id":sender
            },
        "sender_action":"mark_seen"
    }
    send_paquet(sender,payload)
def typing_on(sender):
    payload = {
        "recipient":{
            "id":sender
            },
        "sender_action":"typing_on"
    }
    send_paquet(sender,payload)
def typing_off(sender):
    payload = {
        "recipient":{
            "id":sender
            },
        "sender_action":"typing_off"
    }
    send_paquet(sender,payload)

# CONFIGURATION DE LA PAGE HAL
def reglage_menu():
    payload = {
  "persistent_menu":[
    {
      "locale":"default",
      "call_to_actions":[
        {
          "type":"postback",
          "title":"Menu",
          "payload":"menu"
        },
        {
          "title":"Actualités",
          "type":"nested",
          "call_to_actions":[
            {
              "title":"A la une",
              "type":"postback",
              "payload":"actuune"
            },
            {
              "title":"Actu Monde",
              "type":"postback",
              "payload":"actumonde"
            },
            {
              "title":"Actu Sport",
              "type":"postback",
              "payload":"actusport"
            }
          ]
        },
        {
          "type":"postback",
          "title":"Fais croquer !",
          "payload":"partage"
        }
      ]
    },
    {
      "locale":"zh_CN",
      "composer_input_disabled":"false"
    }
  ]
 }
    return payload
def get_started():
    payload = { 
  "get_started":{
    "payload":"salut"
  }
 }
    return payload
def description():
    payload = {
  "greeting":[
    {
      "locale":"default",
      "text":"Salut {{user_first_name}}, commençons à discuter !"
    }, {
      "locale":"en_US",
      "text":"Hi {{user_first_name}}, let's start!"
    }
  ] 
 }
    return payload

if __name__ == '__main__':
    app.run(debug=True) #Runs the application on a local development server. / If the debug flag is set the server will automatically reload for code changes 