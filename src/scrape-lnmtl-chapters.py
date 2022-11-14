import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from strip_html_tags import remove_html_tags, strip_tags


novel_name_list = ["martial-god-asura", "chaotic-sword-god"]

scraping_site = "https://lnmtl.com/novel/"

novel_list = []


for site in novel_name_list:
    page = requests.get(scraping_site + site)
    soup = BeautifulSoup(page.content, "html.parser")

    novel_title_list = soup.find_all("span", class_="novel-name")
    novel_title_list = [strip_tags(str(item)) for item in novel_title_list]

    novel_author = soup.find(href=re.compile("author")).get_text()

    novel_description_list = soup.find_all("div", class_="description")
    novel_description_list = [strip_tags(str(item)) for item in novel_description_list]
    # novel_tags
    novel_tags_list = soup.find_all(href=re.compile("tag"))
    novel_tags_list = [strip_tags(str(item)) for item in novel_tags_list]

    # print(novel_description_list)

    data_dict = {
        "novel_name": novel_title_list[0],
        "novel_description": novel_description_list[0],
        "novel_author": novel_author,
        "novel_tags": novel_tags_list[0],
    }
    novel_list.append(data_dict)
    # print(f"{novel_title}", novel_description)

novel_data_df = pd.DataFrame(novel_list)

# novel_data_df.to_excel(r"ex.xlsx")

print(novel_data_df)

# print(soup.prettify())

# print(title)


# print(novel_data)

# document.querySelector("#app > main > div.jumbotron.novel > div > div > div.media-body.media-middle > h2 > span")

# /html/body/main/div[1]/div/div/div[2]/h2/span

# //*[@id="app"]/main/div[1]/div/div/div[2]/h2/span
