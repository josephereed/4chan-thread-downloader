from bs4 import BeautifulSoup
import requests

user_input = input("what url?: ")

response = requests.get(user_input)

soup = BeautifulSoup(response.text, "html.parser")


def getFileType(string):
    return {"gif": "gif", "ebm": "webm", "jpg": "jpg", "epg": "jpeg", "png": "png"}[
        string
    ]


links = []
filenames = []
for link in soup.findAll("div", {"class": "fileText"}):
    filenames.append(link.text[6:-25])
    links.append("https:" + link.a.get("href"))

i = 0
for link in links:
    print(link)
    downloaded_img = requests.get(link)
    with open(filenames[i] + "." + getFileType(link[-3:]), "wb") as file:
        file.write(downloaded_img.content)
    i += 1
