from os.path import join
from typing import Dict, List, Union

import requests

# Type hint
ComplexDict = Dict[str, Union[str, List[str]]]
StrDict = Dict[str, str]
StrListDict = Dict[str, List[str]]


class GhibliApi:
    _base_url = 'https://ghibliapi.herokuapp.com'

    _films_url = join(_base_url, 'films')
    _people_url = join(_base_url, 'people')

    @classmethod
    def get_film_list_with_cast(cls) -> List[ComplexDict]:
        """[{'id':'45336', 'title':'Totoro', 'people':['Renaldo',]}]"""

        films_with_people = cls.query_films().copy()

        # for every person get all film's id
        for person in cls.query_people():
            for person_film_id in person['films_id']:

                # and compare film id with person's film id
                for film in films_with_people:
                    if person_film_id == film['id']:

                        # people key don't exist. create it.
                        if not isinstance(film.get('people'), list):
                            film['people'] = []

                        film['people'].append(person['name'])

        return films_with_people

    @classmethod
    def query_films(cls) -> List[ComplexDict]:
        films_data = requests.get(cls._films_url).json()
        films = [cls.parse_film_title_and_id(film) for film in films_data]

        return films

    @classmethod
    def query_people(cls) -> List[ComplexDict]:
        people_data = requests.get(cls._people_url).json()
        people = [
            cls.parse_name_and_films_id(person)
            for person in people_data
        ]

        return people

    @classmethod
    def parse_film_title_and_id(cls, film: ComplexDict) -> StrDict:

        return {
            'id': film.get('id'),
            'title': film.get('title'),
        }

    @classmethod
    def parse_name_and_films_id(cls, person: ComplexDict) -> StrListDict:

        return {
            'name': person.get('name'),
            'films_id': [
                cls.parse_film_id(film)
                for film in person.get('films')
            ],
        }

    @classmethod
    def parse_film_id(cls, film: str) -> str:
        return film.split('/')[-1]
