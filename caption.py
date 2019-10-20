from markov import Markov
from scraper import Scraper

def caption(username, start, end):
    scraper = Scraper(username, start, end)
    text = scraper.text
    try:
        markov = Markov(text)
    except:
        return None
    text = markov.generate()
    if text == None:
        text = "Needs more input"
    return text
