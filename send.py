# POUR GENERER DES PAYLOAD :
from toolkit import recherche_similitude

def send_share(sender):
  texte = "Pyrak est un chatbot permettant de demander le menu du RAK, restaurant de l'IMT Atlantique"
  return {"recipient":{"id":sender },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"Click pour permettre à tes potes de savoir ce qu'il y a au RAK!",
        "buttons":[
            {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": "Pyrak Chatbot",
                            "subtitle": texte,
                            "default_action": {"type": "web_url","url": 'https://m.me/menupyrak/'},
                            "buttons": [{
                                  "type": "web_url",
                                  "url": 'https://m.me/menupyrak/', 
                                  "title": 'Se lancer !'
                                }]
                            }]
                        }
                    }
                }
            }]
        }
    }}}
def send_text (sender,texte):

    return {'recipient': {'id': sender}, 'message': {'text': texte}}
def send_choix_multiple5(sender,texte,choix1,choix2,choix3,choix4,choix5):
  return {
  "recipient":{
    "id":sender
  },
  "message":{
    "text":texte,
    "quick_replies":[
      {
        "content_type":"text",
        "title":choix1,
        "payload":choix1,
      },
      {
        "content_type":"text",
        "title":choix2,
        "payload":choix2,
      },
      {
        "content_type":"text",
        "title":choix3,
        "payload":choix3,
      },
      {
        "content_type":"text",
        "title":choix4,
        "payload":choix4,
      },
      {
        "content_type":"text",
        "title":choix5,
        "payload":choix5,
      }
    ]
  }
 }