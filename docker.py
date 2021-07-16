import requests
from bs4 import BeautifulSoup
print("{Y}    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗      ██████╗  ██████╗ ███████╗ ")
print("{Y}    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗    ██╔═████╗██╔═████╗╚════██║ ")
print("{Y}    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝    ██║██╔██║██║██╔██║    ██╔╝")
print("{Y}    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗    ████╔╝██║████╔╝██║   ██╔╝")
print("{Y}    ██║  ██╗██║███████╗███████╗███████╗██║  ██║    ╚██████╔╝╚██████╔╝   ██║ ")
print ("=" * 80)

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
	}
tabUrl="https://www.google.com/search?client=firefox-b-d&q="
dork =  input("Enter your dorks ::")
url = tabUrl+dork
filter = input("Enter filter world :: ")
print("Total sites found from that url")
print ("=" * 80)
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text , "html.parser")
lista=[]
for link in soup.find_all('a', href=True):
    lista.append(link.get('href'))

for text in lista:
    if filter in text:
        print (text) 


