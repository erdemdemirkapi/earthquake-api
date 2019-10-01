from flask import Flask
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def earthquakes():
    URL = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
    COLUMNS = ["Tarih", "Saat", "Enlem(N)", "Boylam(E)", "Derinlik(km)", "MD", "ML", "Mw", "Yer", "Çözüm Niteliği"]
    html = urllib.request.urlopen(URL).read()

    pre = BeautifulSoup(html).find("pre")
    pre_array = str(pre).split("\n")
    data = []
    for i in range(7, len(pre_array) - 2):
        detail = pre_array[i].split()
        detail[8:-1] = [" ".join(detail[8:-1])]
        detail_json = dict(zip(COLUMNS, detail))
        data.append(detail_json)

    response = {"data" : data}
    return response

if __name__ == '__main__':
    app.run()