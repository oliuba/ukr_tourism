"""
Module to search information about place.
"""
from googlesearch import search


def info(start: str) -> str:
    """
    Return site-url, with information about given place.
    """
    query = f"{start}"
    res = search(query, lang='ua', stop=1)
    for i in res:
        return i


# print(info('хмельницький'))
