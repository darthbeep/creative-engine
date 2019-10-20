import requests
import instaloader

class Scraper:
    def __init__(self, username, start = '', stop = ''):
        if len(start) < 1:
            start = ''
        if len(stop) < 1:
            stop = ''
        self.username = username
        L = instaloader.Instaloader()

        try:
            profile = instaloader.Profile.from_username(L.context, username)
            posts = profile.get_posts()
        except:
            posts = []
        text = ""
        for p in posts:
            post = p.caption
            if(start not in post or stop not in post):
                continue
            if(len(start) > 1):
             post = post.split(start)[1]
            if(len(stop) > 1):
             post = post.split(stop)[0]
            post = post[:-2]
            post += '.'
            text +=  post
        self.text = text
