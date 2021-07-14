"""This module serves for searching touristic places by parsing HTML documents."""

import requests
from bs4 import BeautifulSoup

def parse_webpage(url: str):
    """Parses webpage and and returns the text of webpage."""
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup


def places_veterdoit(soup):
    """Returns a list of places from a soup. of veterdoit"""
    places = soup.find_all('strong')
    places_lst = []
    for _, tag in enumerate(places):
        tag = str(tag)[8:-9].strip()
        try:
            remove_ind = tag.index(',')
            tag = tag[:remove_ind]
        except ValueError:
            pass
        if not 'област' in tag and not '<' in tag and not 'цьк' in tag and not 'Viber' in tag \
            and not 'Івано' in tag and not 'Тернопіль' in tag:
            places_lst.append(tag)
    return places_lst


def places_andy(soup):
    """Returns a list of places from a soup of andy."""
    print(soup.find_all('a'))

# print(places_andy(parse_webpage('https://andy-travel.com.ua/top-60-naycikavishyh-kutochkiv-ukrayiny')))
print(places_veterdoit(parse_webpage('https://veterdoit.com/10-nezvychaynykh-sil-ukrainy-iaki-varto-vidvidaty/')))
print(places_veterdoit(parse_webpage('https://veterdoit.com/tsikavi-mistsia-ukrainy-iaki-vas-vraziat/')))
