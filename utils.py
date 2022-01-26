import random

import requests

url = "https://jsonkeeper.com/b/ZD7I"


def load_random_word():

    json = requests.get(url)
    data = json.json()
    random_word = random.choice(data)
    return random_word["word"], random_word["subwords"]



