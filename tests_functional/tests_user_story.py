from django.test import TestCase

from selenium import webdriver
from tests_functional.messages_en import msg


class MoviesPageVisitorTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # USER STORY
        # user opens browser and
        # visits website /movies endpoint on localhost:8000
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        cls.browser.get('http://localhost:8000/movies')

    @classmethod
    def tearDownClass(cls):
        # user closes browser
        cls.browser.quit()

    def test_user_can_access_movie_page(self):
        self.assertIn(
            msg['GHIBLI_MOVIES_TITLE'],
            self.browser.title,
            msg=msg['GHIBLI_MOVIES_TITLE_MSG']
        )

    def test_user_can_see_movie_list(self):
        # user checks the list of all movies from Ghibli Studio
        self.assertEqual(
            msg['GHIBLI_MOVIE_LIST_TITLE'],
            self.browser.find_element_by_id(msg['GHIBLI_MOVIE_LIST_TITLE_TAG']).text,  # noqa
            msg=msg['GHIBLI_MOVIE_LIST_TITLE_MSG']
        )

        self.assertIn(
            msg['GHIBLI_MOVIE_NAME'],
            [title.text.replace('\n', '')
             for title in self.browser.find_elements_by_class_name(msg['GHIBLI_MOVIE_NAME_TAG'])],  # noqa
            msg=msg['GHIBLI_MOVIE_NAME_MSG']
        )

    def test_user_can_see_list_of_people_from_each_movie(self):
        # user also checks list of people (cast) for each movie
        self.assertIn(
            msg['GHIBLI_PERSON_NAME'],
            [people.text.replace('* ', '')
             for people in self.browser.find_elements_by_class_name(msg['GHIBLI_PERSON_NAME_TAG'])],  # noqa
            msg=msg['GHIBLI_PERSON_NAME_MSG']
        )
