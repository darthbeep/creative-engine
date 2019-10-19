import requests
if __name__ == '__main__':
    page = requests.get("https://www.instagram.com/creative_engine_project/")
    things = str(page.content).split("/30:\\\\n")
    things = things[1:]
    for i in range(len(things)):
         things[i] = things[i].split("\\\\n")[0]
    print(things)
