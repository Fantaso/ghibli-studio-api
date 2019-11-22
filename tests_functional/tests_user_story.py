from django.test import TestCase

from selenium import webdriver


class MoviesPageVisitorTest(TestCase):

    @classmethod
    def setUpClass(cls):
        ## USER STORY
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
        self.assertIn('Ghibli Studio | Movies',
                      self.browser.title,
                      msg='Can not load /movies page')

    def test_user_can_see_movie_list(self):
        # user checks the list of all movies from Ghibli Studio
        self.assertEqual('Ghibli Studio Movie List',
                         self.browser.find_element_by_id('movie-list-title').text,
                         msg='Can not render movie list')
        self.assertIn('MY NEIGHBOR TOTORO',
                      [
                          title.text.replace('\n', '')
                          for title in self.browser.find_elements_by_class_name('movie-title')
                      ],
                      msg=f'Can not render movie {"MY NEIGHBOR TOTORO"}')

    def test_user_can_see_list_of_people_from_each_movie(self):
        # user also checks list of people (cast) for each movie
        self.assertIn('Jiji',
                      [
                          people.text.replace('* ', '')
                          for people in self.browser.find_elements_by_class_name('movie-cast')
                      ],
                      msg='Can not render cast of people from movie')
