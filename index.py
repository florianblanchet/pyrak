# coding: utf-8
from flask import Flask, render_template, request
from config import FB_VERIFY_TOKEN
from app import webhook_get

app = Flask("app")  #instance de la classe FLask. premier argument est le nom


print('     /$$$$$$$$\                  /$$   $$    ')
print('    | $$    |$$                 | $$  $$     ')
print('    | $$    | $$    /$$$$$$$    | $$ $$      ')
print('    | $$$$$$$$$$   |_______$$   | $$$$       ')
print('    | $$    \ $$    /$$$$$$$$   | $$ $$      ')
print('    | $$     \ $$  |$$__   $$   | $$  $$     ')
print('    | $$      \ $$ | $$$$$$$$   | $$ \ $$    ')
print('    |__/       \_/  \_______/   |__/  |_/    ')

@app.route('/', methods=['POST']) #A decorator that is used to register a view function for a given URL
# rule.Ici rule = / et en option les methodes assignées à ce rule
def start_post():
    return webhook_get()

@app.route('/', methods=['GET']) #A decorator that is used to register a view function for a given URL
def start_get():
    print(request.args.get('hub.verify_token'))
    print(FB_VERIFY_TOKEN)
    if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return "Wrong Verify Token"

@app.route('/confidentialite',methods=['GET'])
def confident():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) #Runs the application on a local development server. / If the debug flag is set the server will
    # automatically reload for code changes