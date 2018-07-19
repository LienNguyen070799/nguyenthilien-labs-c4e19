# 1.download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://dantri.com.vn"
#  1.1. open a connection
# conn = urlopen(url)
# 1.2 read data
# data = conn.read()
# 1.3. decode
# html = data.decode("utf-8")
html_file = urlopen(url).read()
# print(html)
# conn = urlopen(url)
# data = conn.read()
# html = urlopen(url).read().decode("uft-8")



# save to file
# f= open("dantri.html","wb") 
# f.write(html_file)
# f.close()




#2. extact ROI(region of interest)
soup = BeautifulSoup(html_file,"html.parser")
ul = soup.find("ul","ul1 ulnew")
# print(ul.prettify())



# # 3. Extract info
li_list = ul.find_all("li")

list_1 = []

for li in li_list:
    list_2 = {}
# li = li_list[0]
    a = li.h4.a
    title = a.string
    href = url + a['href']
    print(href)
    
    list_2["title"] = title
    list_2["link"] = href
    list_1.append(list_2)
print(list_1)
import pyexcel
pyexcel.save_as(records = list_1,dest_file_name = "ex011.xlsx")
# # a = h4.a
# print(title)

# print(li.prettify())



# 4. save to data excel
