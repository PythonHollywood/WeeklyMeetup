import oauth2
import urllib

CONSUMER_SECRET = 'AhwROzia5YDDG14dSfuBF1DqnLVGjq6onlmKoBR69yb5HBm2Vf'
CONSUMER_KEY = 'aHEvWsmVQgXLkoOG7mXbTHH9e'

ACCESS_TOKEN = '39890579-oPwvAOrY95ayfVZRbgtXLDNfUYPVQNpzw9Pn4dQke'
ACCESS_TOKEN_SECRET = 'vPoNhZGd9pDSxkpQQPQEbDvdVEUZZyIAldKzOqmpyFqZT'


def update_profile_pic(mood):

    #update_profile_pic_url='https://api.twitter.com/1.1/account/update_profile_background_image.json'
    if mood=='Happy':
        path_to_image='/Users/gemclaw/Downloads/tamagotchi_dribbble.jpg'
    elif mood=='Mad':
        path_to_image='otherPath'
    elif mood=='Depressed':
        path_to_image='otherPath'
    elif mood=='Hungry':
        path_to_image='otherPath'
    with open(path_to_image, "rb") as f:
        data = f.read()
        image = data.encode("base64")
    update_data = {'image':image}
    encoded_update_data = urllib.urlencode(update_data)
    return encoded_update_data


def post(url, data):
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)

        client = oauth2.Client(consumer, token)
        resp, content = client.request(url, "POST", data, None)
        print resp
        if resp['status'] != '200':
            return 'POST Request Failed! with Code: '+resp['status']+"and Content :"+content



encoded_image = update_profile_pic('Happy')
post('https://api.twitter.com/1.1/account/update_profile_image.json', encoded_image)
