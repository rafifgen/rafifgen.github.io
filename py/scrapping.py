import requests as rq
import json
import datetime
from bs4 import BeautifulSoup


def del_new_line(value):
    return ''.join(value.splitlines())

page = rq.get("https://www.republika.co.id/")
aBSobj = BeautifulSoup(page.text, 'html.parser')

file = open(".\\json\\data.json", 'w')

data = []
temp = []
arr_judul = []
for obj in aBSobj.find_all("div", class_="caption"):
    temp_date = obj.find("div", class_='date')
    temp_judul = obj.find("h3")
    if temp_judul != None and temp_date != None:
        temp_date = temp_date.text
        
        # ambil kategori
        temp_kategori = temp_date[0:temp_date.find(' -')]
        temp_kategori = temp_kategori.strip()
        
        # ambil tanggal
        temp_date = temp_date[temp_date.find('- ')+2:]
        temp_date = temp_date.strip()
        # print(temp_date)
        
        # ambil judul
        temp_judul = temp_judul.find("span")
        temp_judul = temp_judul.text
        # print(temp_judul)

        # nulis ke json
        data.append({"judul": temp_judul, "kategori": temp_kategori, "waktu_publish": temp_date, "waktu_pengambilan": datetime.datetime.now().strftime("%a %d %b %Y, %H:%M")})
jdumps = json.dumps(data)
print(jdumps)
file.writelines(jdumps)