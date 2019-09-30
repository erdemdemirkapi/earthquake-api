from flask import Flask
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def earthquakes():
    URL = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
    COLUMNS = ["Tarih", "Saat", "Enlem", "Boylam", "Derinlik", "MD", "ML", "Mw", "Yer", "Çözüm Niteliği"]
    html = urllib.request.urlopen(URL).read()

    data = BeautifulSoup(html)
    pre = data.find("pre")
    data = str(pre).split("\n")

    return data

if __name__ == '__main__':
    app.run()
