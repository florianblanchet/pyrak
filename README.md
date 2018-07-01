# PyRAK

Give the RAK (IMT ATLANTIQUE Engineering School Canteen) through a Facebook Messenger Chatbot. The menu is collected at the URL: http://services.telecom-bretagne.eu/rak/.

## Create an Facebook Developer app

Set up a Messenger app on [developers.facebook.com](https://developers.facebook.com/). A TOKEN will be given. Add it to the config.py file.
Create the Facebook page you want to chat with linked to your personal profile on [facebook.com](https://facebook.com/).

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).
It works fine with Python 3.6.2.

```sh
$ cd pyRAK
$ pip install -r requirements.txt
$ python index.py
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

For tests it is useful to use [ngrok](https://ngrok.com/) to redirect your localhost:5000 stream to a temporary public domain. Give the domain to the facebook developer Webhook and you will be able to test the bot on a page.


## Deploying pyRAK to Heroku
Install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ heroku create
$ git push heroku master
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Make sure to add FB_ACCESS_TOKEN and FB_VERIFY_TOKEN to the Heroku environment variables and change the facebook developer Webhook with your new domain.