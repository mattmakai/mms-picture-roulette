import json
import random
import requests

from flask import request
from twilio.rest import TwilioRestClient

from . import app
from config import FLICKR_API_KEY

client = TwilioRestClient()


@app.route('/', methods=['GET', 'POST'])
def send_image():
    if request.method == 'GET':
        return 'The deployment worked! Now copy your browser URL into the' + \
               ' Twilio message text box for your phone number.'
    sender_number = request.form.get('From', '')
    twilio_number = request.form.get('To', '')
    tag = request.form.get('Body', '')
    image_url, msg = _get_flickr_image(tag)
    _send_mms_twiml(image_url, msg, sender_number, twilio_number)
    return 'ok'


def _get_flickr_image(tag):
    flickr_api_call = "https://api.flickr.com/services/rest/" + \
        "?method=flickr.photos.search&api_key=%s&tags=%s&per_page=25&" + \
        "format=json&nojsoncallback=1"
    try:
        response = requests.get(flickr_api_call % (FLICKR_API_KEY, tag))
        json_response = json.loads(response.content)
        random_photo_number = random.randint(0, 25)
        photo_json = json_response['photos']['photo'][random_photo_number]
        msg = "Here's a picture of %s. Maybe." % tag
        image_url = "https://farm" + str(photo_json['farm']) + \
            ".staticflickr.com/" + str(photo_json['server']) + "/" + \
            str(photo_json['id']) + "_" + photo_json['secret'] + ".jpg"
    except:
        msg = "Sorry, we couldn't pull an image for that word, " + \
              "here's a dinosaur instead!"
        image_url = "https://farm1.staticflickr.com/46/" + \
                    "154877897_a299d80baa_b_d.jpg"
    return image_url, msg


def _send_mms_twiml(image_url, msg, sender_number, twilio_number):
    client.messages.create(to=sender_number, from_=twilio_number,
        body=msg, media_url=image_url)
