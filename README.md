<!-- logo -->
<a href="https://github.io/fantaso">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Ghibli Studio API
</h1>

> Web app caching test case with Django and Memcached. It consists of caching a single web page for 60 seconds, in which the Django view makes a request to a third party API service for the data (All movies and cast of Ghibli Studio available in that API) that will be rendered as a web page and cached.

<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->




Test case allows the user to visit website to view a list of all movies ever produced by Ghibli Studio (or available on the API database) and for each movie it will list the all the people (human (animated) characters, because their are animals or species available too.) that was part of the movie.

It is partly tested as only and was developed as showcase only.




How Ghiblie Studio API Works:
- You can open the browser with the url http://localhost:8000/movies to view the list of movies and people on it.
- You can refresh the web page and it will be cached for 60 seconds so between that time, the response time of the web browser should be responding faster as page have been cached.        

<br><br>

## Index:
- #### Installation
    1. Installing Ghibli Studio Api App

- #### Usage:
    1. Available Endpoints
    2. Tests INFO

- #### What's Next:
    1. thoughts on improving it.
        - Testing
        - App
        - Ghibli Api
        - DevOps

- #### Information:
- #### Maintainer


<br><br>


## Installation:
#### 1.Installing Ghibli Studio API App

1. Clone repository and go inside the repository folder "ghibli-studio-api"
```sh
git clone https://github.com/Fantaso/ghibli-studio-api.git
```

2. Create you virtualenv and install the packages (You might need to install memcached in your system as python-memcached)
```sh
pip install -r requirements.txt
```

3. (Optional: we are not using the db) Apply database's default mapping to the database; migrate the database.
```sh
python manage.py migrate
```

5. Run the application.
```sh
python manage.py runserver
```


<br>

## USAGE
#### 1. Endpoint List
URI Example: `http://localhost:8000/movies`


<br>


#### 2. Tests INFO

1. Run the Ghibli Studio app tests locally with:
```sh
python manage.py test
```

<br>


## WHATS NEXT
#### 1. Thoughts on improving it.

###### Testing
- Add unittest, integration and system tests within Django app "movies/" folder "tests" with the folder architecture in place.  
- Set up pytest and design fixtures architecture for flexible and rapid testing
- Set up test coverage for reporting and monitoring
- Set up linting flake8 to check for styling and code consistency with specifics requirements

###### App
- Set up error handling and pages
- Set up error tracking (Sentry)
- Do we want to handle to some data for more than 60 in case the erd-party ghibli api fails.
 
###### Ghibli Api
- Test and do profiling on the relationship (movies/ and people/) and refactor to a better and fastest approach.
- Add error handling

###### DevOps
- Set up automated testing pipeline


## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Django                    | ![django][django]                     | Web Framework |
| Selenium                  | ![selenium][selenium]                  | Web browser automation |
| Requests                  | ![requests][requests]                 | HTTP Library |

<br><br>


## Maintainer
Get in touch -–> [Github][github-profile]



<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://www.fantaso.de/
<!-- Extra -->


<!-- Repos -->
[github-repo]: https://github.com/Fantaso/ghibli-studio-api

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[django]: readme/django.png
[selenium]: readme/selenium.png
[requests]: readme/requests.jpg