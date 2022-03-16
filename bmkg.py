import os
import requests
from bs4 import BeautifulSoup as soup

#warna
g = "\033[1;32m"
w = "\033[1;97m"

banner = """
__________    _____   ____  __.________  
\______   \  /     \ |    |/ _/  _____/  
 |    |  _/ /  \ /  \|      </   \  ___  
 |    |   \/    Y    \    |  \    \_\  \ 
 |______  /\____|__  /____|__ \______  / 
        \/         \/        \/      \/  Author : Jhosua
--------- Gempa Terkini ---------
"""

def main():
     print(banner)
     data = soup(requests.get("https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg").text, "html.parser").find("tbody")
     for i in data.find_all("tr"):
          gempa = i.find_all("td")
          print("{}~ {}Nomor     : {}".format(g,w,gempa[0].text))
          print("{}~ {}Waktu     : {}".format(g,w,gempa[1].text))
          print("{}~ {}Lintang   : {}".format(g,w,gempa[2].text))
          print("{}~ {}Bujur     : {}".format(g,w,gempa[3].text))
          print("{}~ {}Magnitudo : {}".format(g,w,gempa[4].text))
          print("{}~ {}Kedalaman : {}".format(g,w,gempa[5].text))
          print("{}~ {}Wilayah   : {}".format(g,w,gempa[6].text))
          print("\n-----------------------------------------------------")


if __name__ == '__main__':
     os.system("clear")
     main()