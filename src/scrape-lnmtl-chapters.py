# import string
import requests
from bs4 import BeautifulSoup


page = requests.get("https://lnmtl.com/novel/martial-god-asura")

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

title = soup.find("span", class_="novel-name").get_text()
print(title)

# document.querySelector("#app > main > div.jumbotron.novel > div > div > div.media-body.media-middle > h2 > span")

# /html/body/main/div[1]/div/div/div[2]/h2/span

# //*[@id="app"]/main/div[1]/div/div/div[2]/h2/span
