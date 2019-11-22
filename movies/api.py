from os.path import join
from typing import Dict, List, Union

import requests


class GhibliApi:
    _base_url = 'https://ghibliapi.herokuapp.com'

    _films_url = join(_base_url, 'films')
    _people_url = join(_base_url, 'people')

    films_with_people = []

    def __str__(self):
        return 'Ghibli API'

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    @classmethod
    def get_film_list_with_cast(cls) -> List[Dict[str, Union[str, List[str]]]]:
        """[{'id':'45336', 'title':'Totoro', 'people':['Renaldo',]}]"""

        cls.films_with_people = cls.query_films().copy()

        # for every person get all film's id
        for person in cls.query_people():
            for person_film_id in person['films_id']:

                # and compare film id with person's film id
                for film in cls.films_with_people:
                    if person_film_id == film['id']:

                        # people key don't exist. create it.
                        if not isinstance(film.get('people'), list):
                            film['people'] = []

                        film['people'].append(person['name'])

        return cls.films_with_people

    @classmethod
    def query_films(cls) -> List[Dict[str, Union[str, List[str]]]]:
        films_data = requests.get(cls._films_url).json()
        films = [cls.parse_film_title_and_id(film) for film in films_data]

        return films

    @classmethod
    def query_people(cls) -> List[Dict[str, Union[str, List[str]]]]:
        people_data = requests.get(cls._people_url).json()
        people = [
            cls.parse_name_and_films_id(person)
            for person in people_data
        ]

        return people

    @classmethod
    def parse_film_title_and_id(cls, film: Dict[str, Union[str, List[str]]]) -> Dict[str, str]:

        return {
            'id': film.get('id'),
            'title': film.get('title'),
        }

    @classmethod
    def parse_name_and_films_id(cls, person: Dict[str, Union[str, List[str]]]) -> Dict[str, List[str]]:

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
