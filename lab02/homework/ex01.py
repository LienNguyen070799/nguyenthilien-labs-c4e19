# 1dowload webpage 
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs"
html = urlopen(url).read()
# 2.extact ROI
soup = BeautifulSoup(html,"html.parser")
section = soup.find("section","section chart-grid")
div = section.find("div","section-content")	
li_list = div.ul.find_all("li")
# 3. extract info
list_music = []
list_music_2 = []
for li in li_list:
    dic_music = {}
    a1 = li.find("h3").string
    a2 = li.find("h4").string
    dic_music["name"] = a1
    dic_music["artist"] = a2
    list_music.append(dic_music)
    list_music_2.append(a1 + a2)
# print(list_music_2)
# 4.save to excel
import pyexcel
pyexcel.save_as(records = list_music ,dest_file_name = "excel01.xlsx")

# part 2
# a3 = li.find('h3')
# a4 = li.find('h4')

from youtube_dl import YoutubeDL
options = {'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1} # Tell downloader to download only the first entry (video)
    # 'format' : 'bestaudio/audio'} (thêm nếu muốn download audio)
dl = YoutubeDL(options)
dl.download(list_music_2)

