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
                            "default_action": {"type": "web_url","url": 'https://m.me/pyrak'},
                            "buttons": [{
                                  "type": "web_url",
                                  "url": 'http://m.me/pyrak', 
                                  "title": 'Se lancer !'
                                }]
                            }]
                        }
                    }
                }
            }]
        }
    }}}
def send_msg_button1(sender,texte,nom_button,reponse_rapide):
  return {
  "recipient":{
    "id":sender
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":texte,
        "buttons":[
          {
            "type":"postback",
            "title":nom_button,
            "payload":reponse_rapide
          }
        ]
      }
    }
  }
 } 
def send_msg_button1_web(sender,title,subtitle,link,image_url,nom_button):
  return {
    "recipient": {
      "id": sender
    },
    "message": {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "elements": [{
            "title": title,
            "subtitle": subtitle,
            "item_url": link,               
            "image_url": image_url,
            "buttons": [{
              "type":"web_url",
              "title":nom_button,
              "url":link
            },
            {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title,
                            "subtitle": subtitle,
                            "item_url": link,               
                            "image_url": image_url,
                            "buttons": [{
                                  "type": "web_url",
                                  "url": 'http://m.me/halcomputer', 
                                  "title": 'Discuter avec Hal !'
                                }]
                            }]
                        }
                    }
                }
            }],
          }]
        }
      }
    }
    }
def send_button2_postback_url(sender,texte,nom_button1,reponse_rapide1,nom_lien,link):
  return {"recipient":{"id":sender },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":texte,
        "buttons":[{
            "type":"web_url",
            "url": link,
            "title": nom_lien
            },
            {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": "Actualité",
                            "subtitle": texte,
                            "default_action": {"type": "web_url","url": link},
                            "buttons": [{
                                  "type": "web_url",
                                  "url": link, 
                                  "title": nom_lien
                                }]
                            }]
                        }
                    }
                }
            },
            {
            "type":"postback",
            "title":nom_button1,
            "payload":reponse_rapide1
            }]
        }
    }}}
def location_quick_answer(sender):
  return {
        "recipient": {
            "id": sender
        },
        "message": {
            "text": "Share your location:",
            "quick_replies": [
                {
                    "content_type": "location",
                },
                {
                "content_type":"text",
                "title":'Météo Paris',
                "payload":"Météo Paris"
      }
            ]
        }
    }

def send_link6 (sender,title1,subtitle1,image_url1,link1,title2,subtitle2,image_url2,link2,title3,subtitle3,image_url3,link3,title4,subtitle4,image_url4,link4,title5,subtitle5,image_url5,link5,title6,subtitle6,image_url6,link6):
    return {
    "recipient": {
      "id": sender
    },
    "message": {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "image_aspect_ratio":'square',
          "elements": [{
            "title": title1,
            "subtitle": subtitle1,              
            "image_url": image_url1,
            "default_action":{"type":"web_url","url":link1},
            "buttons": [{
              "type": "web_url",
              "url": link1,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
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
                              "title": "Accéder à l'article",
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title2,
            "subtitle": subtitle2,              
            "image_url": image_url2,
            "default_action":{"type":"web_url","url":link2},
            "buttons": [{
              "type": "web_url",
              "url": link2,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title2,
                            "subtitle": subtitle2,
                            "item_url": link2,               
                            "image_url": image_url2,
                            "buttons": [{
                              "type": "web_url",
                              "url": link2,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title3,
            "subtitle": subtitle3,         
            "image_url": image_url3,
            "default_action":{"type":"web_url","url":link3},
            "buttons": [{
              "type": "web_url",
              "url": link3,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title3,
                            "subtitle": subtitle3,
                            "item_url": link3,               
                            "image_url": image_url3,
                            "buttons": [{
                              "type": "web_url",
                              "url": link3,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title4,
            "subtitle": subtitle4,         
            "image_url": image_url4,
            "default_action":{"type":"web_url","url":link4},
            "buttons": [{
              "type": "web_url",
              "url": link4,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title4,
                            "subtitle": subtitle4,
                            "item_url": link4,               
                            "image_url": image_url4,
                            "buttons": [{
                              "type": "web_url",
                              "url": link4,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title5,
            "subtitle": subtitle5,          
            "image_url": image_url5,
            "default_action":{"type":"web_url","url":link5},
            "buttons": [{
              "type": "web_url",
              "url": link5,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title5,
                            "subtitle": subtitle5,
                            "item_url": link5,               
                            "image_url": image_url5,
                            "buttons": [{
                              "type": "web_url",
                              "url": link5,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title6,
            "subtitle": subtitle6,        
            "image_url": image_url6,
            "default_action":{"type":"web_url","url":link6},
            "buttons": [{
              "type": "web_url",
              "url": link6,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title6,
                            "subtitle": subtitle6,
                            "item_url": link6,               
                            "image_url": image_url6,
                            "buttons": [{
                              "type": "web_url",
                              "url": link6,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }]
        }
      }
    }
    } 
def send_link4 (sender,title1,subtitle1,image_url1,link1,title2,subtitle2,image_url2,link2,title3,subtitle3,image_url3,link3,title4,subtitle4,image_url4,link4):
    return {
    "recipient": {
      "id": sender
    },
    "message": {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "image_aspect_ratio":'square',
          "elements": [{
            "title": title1,
            "subtitle": subtitle1,             
            "image_url": image_url1,
            "default_action":{"type":"web_url","url":link1},
            "buttons": [{
              "type": "web_url",
              "url": link1,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
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
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title2,
            "subtitle": subtitle2,            
            "image_url": image_url2,
            "default_action":{"type":"web_url","url":link2},
            "buttons": [{
              "type": "web_url",
              "url": link2,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title2,
                            "subtitle": subtitle2,
                            "item_url": link2,               
                            "image_url": image_url2,
                            "buttons": [{
                              "type": "web_url",
                              "url": link2,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title3,
            "subtitle": subtitle3,             
            "image_url": image_url3,
            "default_action":{"type":"web_url","url":link3},
            "buttons": [{
              "type": "web_url",
              "url": link3,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title3,
                            "subtitle": subtitle3,
                            "item_url": link3,               
                            "image_url": image_url3,
                            "buttons": [{
                              "type": "web_url",
                              "url": link3,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title4,
            "subtitle": subtitle4,          
            "image_url": image_url4,
            "default_action":{"type":"web_url","url":link4},
            "buttons": [{
              "type": "web_url",
              "url": link4,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title4,
                            "subtitle": subtitle4,
                            "item_url": link4,               
                            "image_url": image_url4,
                            "buttons": [{
                              "type": "web_url",
                              "url": link4,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }]
        }
      }
    }
    }
def send_link3 (sender,title1,subtitle1,image_url1,link1,title2,subtitle2,image_url2,link2,title3,subtitle3,image_url3,link3):
    return {
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
            "image_url": image_url1,
            "default_action":{"type":"web_url","url":link1},
            "buttons": [{
              "type": "web_url",
              "url": link1,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
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
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title2,
            "subtitle": subtitle2,             
            "image_url": image_url2,
            "default_action":{"type":"web_url","url":link2},
            "buttons": [{
              "type": "web_url",
              "url": link2,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title2,
                            "subtitle": subtitle2,
                            "item_url": link2,               
                            "image_url": image_url2,
                            "buttons": [{
                              "type": "web_url",
                              "url": link2,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title3,
            "subtitle": subtitle3,            
            "image_url": image_url3,
            "default_action":{"type":"web_url","url":link3},
            "buttons": [{
              "type": "web_url",
              "url": link3,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title3,
                            "subtitle": subtitle3,
                            "item_url": link3,               
                            "image_url": image_url3,
                            "buttons": [{
                              "type": "web_url",
                              "url": link3,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }]
        }
      }
    }
    }
def send_link (sender,title1,subtitle1,image_url1,link1,payload1,title2,subtitle2,image_url2,link2,payload2):
    return {
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
              "type": "postback",
              "title": "T'en veux plus ?",
              "payload": payload1,
            }],
          }, {
            "title": title2,
            "subtitle": subtitle2,
            "item_url": link2,               
            "image_url": image_url2,
            "buttons": [{
              "type": "web_url",
              "url": link2,
              "title": "Ouvre le lien"
            }, {
              "type": "postback",
              "title": "T'en veux plus ? ",
              "payload": payload2,
            }]
          }]
        }
      }
    }
    }

def send_text (sender,texte):

    return {'recipient': {'id': sender}, 'message': {'text': texte}}
def send_choix_multiple1(sender,texte,choix1):
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
        "payload":choix1
      }
    ]
  }
 } 
def send_choix_multiple2(sender,texte,choix1,choix2):
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
        "payload":choix1
      },
      {
        "content_type":"text",
        "title":choix2,
        "payload":choix2
      }
    ]
  }
 } 

def send_choix_multiple3(sender,texte,choix1,choix2,choix3):
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
        "payload":choix1
      },
      {
        "content_type":"text",
        "title":choix2,
        "payload":choix2
      },
      {
        "content_type":"text",
        "title":choix3,
        "payload":choix3
      }
    ]
  }
 } 
def send_choix_multiple4(sender,texte,choix1,choix2,choix3,choix4):
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
      }
    ]
  }
 }