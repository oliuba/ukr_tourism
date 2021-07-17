"""This module reads file and gives a random place for traveling."""

from random import choice


def read_file(path: str) -> list:
    """Reads file and returns a list of places."""
    places = []
    with open(path, encoding='utf-8') as places_f:
        for place in places_f:
            places.append(place.strip())
    return places


def get_random_place(places: set) -> str:
    """Gives a random place from a list of places."""
    return choice(places)


def main_travel() -> str:
    """The main fumction that serves for giving a random place."""
    places = read_file('places.txt')
    return get_random_place(places)


if __name__ == "__main__":
    print(main_travel())
