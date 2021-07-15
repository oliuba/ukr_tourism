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


def combine_places():
    """Combines all the results to a set."""
    lst_places_1 = places_veterdoit(parse_webpage('https://veterdoit.com/10-nezvychaynykh-sil-ukrainy-iaki-varto-vidvidaty/'))
    lst_places_2 = places_veterdoit(parse_webpage('https://veterdoit.com/tsikavi-mistsia-ukrainy-iaki-vas-vraziat/'))
    all_places = set(lst_places_1) | set(lst_places_2)
    return all_places


def write_file():
    """Writes a file with the places."""
    places = combine_places()
    with open('places.txt', 'a', encoding='utf-8') as file_t:
        for place in places:
            file_t.write(f'{place}\n')


# write_file()
