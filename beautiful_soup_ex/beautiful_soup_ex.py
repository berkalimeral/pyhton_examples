import requests
from bs4 import BeautifulSoup

target_url = "https://atilsamancioglu.com"
response_links = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_links(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        #print(found_link)
        if found_link:
            if '#' in found_link:
                found_link = found_link.split('#')[0]
            if target_url in found_link and found_link not in response_links: #target_url found_link in içinde geçiyorsa if bloğu çalışacak
                response_links.append(found_link)
                print(found_link)
                make_request(found_link)

get_links(target_url)