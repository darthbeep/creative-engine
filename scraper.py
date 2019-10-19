import requests

class Scraper:
    def __init__(self, username, start = 'text":', stop = '"}'):
        print("test")
        url = 'https://www.instagram.com/' + username
        page = requests.get(url)
        things = str(page.text).split(start)
        things = things[1:]
        for i in range(len(things)):
             things[i] = things[i].split(stop)[0]
             if '.' not in things[i]:
                 things[i] += '. '
        text = "".join(things)
        text = text.split("\\n")
        text = "".join(text)
        self.text = text
