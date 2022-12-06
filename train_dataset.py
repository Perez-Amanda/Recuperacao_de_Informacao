from pathlib import Path
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

df = pd.read_csv('./dataset.csv', sep=',')
lista_links = df['link'].tolist()

root = Path().absolute()
url_base = 'https://www.letras.mus.br'
txt_mus = open(root/"musicas_short.txt", "a", encoding='utf-8')

counter = 1  # para printar a quantidade de músicas já inserida no dataset
link_id = 0

for url in lista_links:
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    song_name = soup.findAll("a", {"class": "song-name"})
    for i in range(0, len(song_name)):
        title = str(song_name[i].findAll("span")[0]).replace("<span>", "").replace("</span>", "")
        txt_mus.write(title)
        txt_mus.write(f"\n>> {df.iloc[link_id]['genero']}")
        txt_mus.write("\n---\n")
        url_mus = url_base + song_name[i]['href']
        html_2 = urlopen(url_mus)
        soup2 = BeautifulSoup(html_2.read(), 'html.parser')
        song_lyrics = soup2.findAll("div", {"class": "cnt-letra"})
        letra = song_lyrics[0].findAll("p")
        for estrofe in letra:
            est = str(estrofe).replace("<p>", "").replace("</p>", "")
            est = est.replace("<br/>", "\n").replace("<br>", "\n").replace("</br>", "\n")
            estrofe_final = est + "\n\n"
            txt_mus.write(estrofe_final.replace("\n\n\n", "\n\n"))
        txt_mus.write("XXXXXXXXXX\n\n")
        print(counter)
        counter += 1
    link_id += 1
# DEU 9340 MÚSICAS!!!!!