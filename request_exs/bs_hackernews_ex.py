import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/news"

def make_request(url):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".titleline > a")
    return links


def get_data(url):
    response_links = []
    links = make_request(url)
    for link in links:
        title = link.getText()
        href = link.get("href", None)
        votes = link.find_next(class_="score")
        points = int(votes.getText().replace(" points", ""))

        response_links.append(
            {
                "title": title,
                "href": href,
                "points": points
            }
        )
    return response_links


news = get_data(target_url)
print(news)