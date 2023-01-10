import requests
from bs4 import BeautifulSoup
import sqlite3

# so what i tried to to do here was just to tale every link in the homepage of lnmtl
# to see the strategies of routing in the site


def scrape():
    # site: str = "https://lnmtl.com/novel/"
    site: str = "https://lnmtl.com"

    page = requests.get(site)
    soup = BeautifulSoup(page.content, "html.parser")

    page_links = soup.find_all("a")

    for link in page_links:
        print(check_for_images(link))


# Format node for links
def check_for_images(link_raw: BeautifulSoup):
    href = link_raw["href"]
    text = link_raw.get_text()
    image = link_raw.find("img")
    image_src = ""
    image_alt_text = ""
    if image:
        image_src = image["src"]
        # imageAltText = image["alt"]

    return {
        "text": text.strip(),
        "href": href,
        "image_src": image_src,
        "image_alt_text": image_alt_text,
    }


if __name__ == "__main__":
    scrape()
