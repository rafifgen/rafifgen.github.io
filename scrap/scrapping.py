import datetime as dt
import json
import requests as rq
from bs4 import BeautifulSoup

page = rq.get("https://www.republika.co.id/")
aBSobj = BeautifulSoup(page.text, 'html.parser')
file = open("C:\\Users\\rafif\\OneDrive - Politeknik Negeri Bandung\\sem 2\\Semester 2\\Proyek 1\\Pertemuan 8\\Source Code\\kupip.github.io\\scrap\\data.json", 'w')

data = []
for obj in aBSobj.find_all("div", class_="caption"):
    temp_date_cat = obj.find("div", class_='date')
    temp_judul = obj.find("h3")

    # pengecekan apakah objek yang diambil ada isinya
    if temp_judul != None and temp_date_cat != None:
        # ambil judul
        judul = temp_judul.find("span")
        judul = judul.text

        # mengambil teks yang berisi kategori dan waktu
        temp_date_cat = temp_date_cat.text
        
        # ambil kategori
        kategori = temp_date_cat[0:temp_date_cat.find(' -')]
        kategori = kategori.strip()
        
        # ambil tanggal
        date = temp_date_cat[temp_date_cat.find('- ')+2:]
        date = date.strip()

        # nulis ke array dictionary
        data.append({"judul": judul, "kategori": kategori, "waktu_publish": date, "waktu_pengambilan": dt.datetime.now().strftime("%d %b %Y, %H:%M")})
file.writelines(json.dumps(data))
file.close()
print(json.dumps(data))