import markovify
import requests
import json

class Markov:
    def __init__(self, text):
        self.text = text
        self.text_model = markovify.Text(text)

    def generate(self):
        return self.text_model.make_sentence(tries = 100, state_size = 0)

# if __name__== "__main__":
#     markov = Markov("ha")
#     t = markov.generate()
#     print(t)
