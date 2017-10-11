import urllib.request
import json

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
                texte_notponct = extract_ponct(texte,ponct_liste) # On retire la ponctuation
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
def url_shorter(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = urllib.request(
        post_url,
        json.dumps(postdata),
        headers
    )
    ret = urllib2.urlopen(req).read()
    print(ret)
    return json.loads(ret)['id']
def recherche_similitude(chercher,liste):
    position=-1
    for i in range(len(chercher)):
        for j in range(len(liste)):
            if chercher[i]==liste[j]:
                return j
    
def similitudes (a,b):

    return list(set(a).intersection(b)) 
def extract_ponct(texte,ponct_liste):
    l=''
    for i in range(len(texte)):
        if texte[i] in ponct_liste: #supprime la ponctuation
            pass
        elif texte[i]=="'":
            l=l+' '
        else:
            if ord(texte[i]) in [232,233,234,235]: #remplacer les accents é par e
                l=l+'e'
            else:
                l=l+texte[i].lower() #met en minuscule
    return l 