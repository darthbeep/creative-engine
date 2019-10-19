import markovify
import requests
import json

class Markov:
    def __init__(self, text):
        self.text = open('testcaptions.txt', 'r').read()
        self.text_model = markovify.Text(self.text)
        data = {}
        r = requests.post(url = "https://www.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code", data = data)
        with open('auth.txt') as creds:
            credentials = json.load(creds)
    def generate(self):
        return self.text_model.make_sentence(tries = 100)

if __name__== "__main__":
    markov = Markov("ha")
    t = markov.generate()
    print(t)
