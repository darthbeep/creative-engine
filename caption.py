from markov import Markov
from scraper import Scraper

def caption(username, start, end):
    scraper = Scraper(username, start, end)
    text = scraper.text
    try:
        markov = Markov(text)
    except:
        if len(text) < 1:
            return "Username not found"
        return "Not enough captions found to generate new text"
    text = markov.generate()
    if len(text) < 1:
        text = "Not enough captions found to generate new text"
    return text
