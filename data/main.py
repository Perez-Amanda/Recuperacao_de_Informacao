from pathlib import Path
from bs4 import BeautifulSoup
from urllib.request import urlopen

lista_musicas = []

root = Path().absolute()
print(root/"url_artistas.txt")

url_base = 'https://www.letras.mus.br'

txt_mus = open(root/"musicas.txt", "a", encoding='utf-8')

counter = 1

with open(root/"url_artistas.txt", encoding='utf-8') as f:
    lista_links = f.readlines()
    for url in lista_links:
        html = urlopen(url)
        soup = BeautifulSoup(html.read(), 'html.parser')
        song_name = soup.findAll("a", {"class": "song-name"})
        for i in range(0, len(song_name)):
            title = str(song_name[i].findAll("span")[0]).replace("<span>", "").replace("</span>", "")
            txt_mus.write(title)
            txt_mus.write("\n---\n")
            url_mus = url_base + song_name[i]['href']
            html_2 = urlopen(url_mus)
            soup2 = BeautifulSoup(html_2.read(), 'html.parser')
            song_lyrics = soup2.findAll("div", {"class": "cnt-letra"})
            # aaa = song_lyrics[0].findAll("p")
            letra = song_lyrics[0].findAll("p")
            # print(len(letra))
            for estrofe in letra:
                est = str(estrofe).replace("<p>", "").replace("</p>", "")
                est = est.replace("<br/>", "\n").replace("<br>", "\n").replace("</br>", "\n")
                # print(a.replace("\n\n\n", "\n\n"), "\n")
                estrofe_final = est + "\n\n"
                txt_mus.write(estrofe_final.replace("\n\n\n", "\n\n"))
            txt_mus.write("XXXXXXXXXX\n\n")
            print(counter)
            counter += 1

            
print("Finish!")
# html = urlopen(url)
# soup = BeautifulSoup(html.read(), 'html.parser')
# song_name = soup.findAll("a", {"class": "song-name"})
# # print(song_name[0]['href'])
# # print(soup.prettify())

# print(title)
# txt_mus.write(title)
# txt_mus.write("\n---\n")
# # url_base = 'https://www.letras.mus.br'

# url_mus = url_base + song_name[10]['href']
# print(url_mus)



# anotar manualmente 656 artistas pra definir o genero das suas músicas e tals



