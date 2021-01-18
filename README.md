<!-- logo -->
<a href="https://github.io/fantaso">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Ghibli Studio
</h1>


**Badges**

[![pipeline status](https://gitlab.com/fantaso/ghibli-studio/badges/master/pipeline.svg)](https://gitlab.com/fantaso/ghibli-studio/-/commits/master)
[![coverage report](https://gitlab.com/fantaso/ghibli-studio/badges/master/coverage.svg)](https://gitlab.com/fantaso/ghibli-studio/-/commits/master)



> Web app caching test case with Django and Memcached. It consists of caching a single web page for 60 seconds, in which the Django view makes a request to a third party API service for the data (All movies and cast of Ghibli Studio available in that API) that will be rendered as a web page and cached.





Test case allows the user to visit website to view a list of all movies ever produced by Ghibli Studio (or available on the API database) and for each movie it will list the all the people (human (animated) characters, because their are animals or species available too.) that was part of the movie.

It is partly tested as only and was developed as showcase only.




How Ghiblie Studio API Works:
- You can open the browser with the url http://localhost:8000 to view the list of movies and people on it.
- You can refresh the web page and it will be cached for 60 seconds so between that time, the response time of the web browser should be responding faster as page have been cached.        

<br><br>

## Index:
- #### Installation
    1. Installing Ghibli Studio App

- #### Usage:
    1. Available Endpoints
    2. Tests INFO
    3. Code quality and security
    4. Quick command list for Docker
    
- #### Basic Deployment:
    1. Gitlab
       - create repository
       - add CI/CD environment variables
    2. Heroku
       - create app-
       - get a heroku api to use in gitlab CI/CD for automated deployments
       - add dyno & get dns for custom domain
       - add server environment variables
    3. AWS
       - get a aws programmatic user key and 
       - create S3 bucket
       - Route53 to create  
    
- #### Manual and Emergency Deployments:
    1. One line command

- #### What's Next:
    1. thoughts on improving it.
        - Testing
        - App
        - Ghibli Api

- #### Information:
- #### Maintainer


<br><br>


## Installation:
#### 1.Installing Ghibli Studio API App

1. Clone repository and go inside the repository folder "ghibli-studio"
```sh
git clone https://gitlab.com/fantaso/ghibli-studio.git
```

2. Create you virtualenv and install the packages (You might need to install memcached in your system as python-memcached)
```sh
pip install -r requirements-dev.txt
```

3. Apply database's default mapping to the database; migrate the database.
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
URI Example: `http://localhost:8000`


<br>


#### 2. Tests & code quality INFO

1. Run the Ghibli Studio app tests locally with:
```sh
py.test core/
```



#### 3. Code quality and security

1. One liner to run the `black` `flake8` `bandit` `safety` and `isort` (make sure you are on the repository root directory)
(Some of the additional arguments used for example in flake8 are taken automatically from the setup.cfg file)

```sh
black -l 120 --diff --exclude \migrations/ core/ && isort core/ && flake8 && safety check && bandit -r core/
```
(remove the `--diff` from after `black -l 120` in order to allow black to format your files. `--diff` just shows you what would be formatted but doesn't write on the files.)


#### 4. Quick command list for Docker

**Production Image**

- build image, run it, get in running container if you want. 

```bash
docker build --pull -f Dockerfile -t ghibli-prod .
docker run --rm -p 80:5000 --env-file .env.sample --name ghibli-prod -t ghibli-prod

docker exec -it ghibli-prod bash
```

**Testing Image**

Performing the test with docker
```bash
docker build --pull -f DockerfileCI -t ghibli-test .
docker run -t ghibli-test
```

**Bulk erasing all and every docker image or container in your computer**
```bash
docker container rm -f $(docker container ls -aq)
docker image rm -f $(docker image ls -aq)
```

<br>


## Basic Deployment


#### 1 Gitlab Setup


- Go to gitlab.com and create your repository and follow the instruction there to push you local repo into gitlab.

- Once there go the repo you just created and into the project's settings go to the CI/CD settings and add 2 environment variables
needed in the environment when the automated test and automated deployment runs with the gitlab runners to push the new updates to Heroku.
The gitlab runners will run everytime you push new code into the master branch.
This environment variables are used in the gitlab-ci.yml file where is configured the CI/CD pipelines.

This environment variables are:

- `HEROKU_API_KEY` : api key you get it from heroku in order to allow you to push the docker images into the server that will host the web app
- `HEROKU_APP` : the name of the app you will create in the next section where I explain the Heroku process.


#### 2 Heroku Setup


- Create the app that will host the dockerized web app in heroku.com and choose the region you want (we chose EUROPE). 
No configuration yet about the docker as that will happen automatically when you push a docker image
here is important to notice that the name of heroku app you create is the same name you need to fill in 
GITLAB setup in the previous section where we added to CI/CD gitlab runner environment variable `HEROKU_APP`.
  
- Once you created the app go to the heroku account section and the very end of the web page you will see a section to get the api key.
This api key is the one that you will use in the CI/CD gitlab runner environment variable `HEROKU_API_KEY` 
  
- Now in you app project there go to "settings" section and here is where we will add the environment variables that will use the server that will host our web app.
These are the variables:
  

AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`: Used to give programmatic access to the aws from our web app to do manage S3 buckets and whatever resources you are using in AWS.
`AWS_REGION`: the aws region you are using.

`AWS_STORAGE_BUCKET_NAME`: the name of the bucket you will host your data used by the web app.

`DATABASE_URL`: This will be commissioned by Heroku automatically since we will configure a Heroku postgresql later on this section. You don't need to create. it will appear automatically.

`DB_CON_MAX_AGE`: max connection time for the database.

`DJANGO_SETTINGS_MODULE`: this is how we will tell our web app which settings to used in production "core.settings.production"

`SECRET_KEY`: the very secret key.

`STATIC_URL`: where our static (html templates and so on) data will leave under our web app.

`MEDIA_URL`: where our media (uploaded data) data will leave under our web app.

  
- Now go to the "overview" section in the heroku app and you will see a "Dyno formation" section and then click in "configure dyno" to use a non-hobby tier server.
This give us the feature to be able to use our own custom domain name. in this case we will use `https://ghibli.fantaso.de`.
Now go to the "settings" section in the heroku app and add a custom domain and it will give you and commission a dns url. This url we will use later on to route the traf from AWS ROUTE53 where we have our main domain `fantaso.de`.
  
- Go to to the "resources" section in the heroku app and create an "add-on" which will be our "Heroku Postgres" database and submit the order for the current app.
This will set up automatically the environment variable we spoke of before `DATABASE_URL`.
  

#### 3 AWS Setup


- Go into the IAM resource of aws in the aws console and get a IAM programmatic user accesskeyid and secretkey that will be used entirely for the web app.
  
- Go to the S3 resource and create the S# bucket with the proper permission and with a name that you need to fill in heroku environment variables previously spoken `AWS_STORAGE_BUCKET_NAME`
  
- Go to Route53 resource and in the hosted zone (fantaso.de) create a dns simple CNAME record to use `https://ghibli.fantaso.de` and reroutes the trafic to the dns url we got from heroku when we commissioned the domain.


**You are good to go for a basic deployment instructions.


## Manual and Emergency Deployments

#### Release a new docker image and update manually our web app for emergencies

**Deploy manually**

make sure you are standing on the repo root directory where the Dockerfile is or use -f Dockerfile-custom-filename.

login, build image, tag the image, push image to heroku registry, release the new image into production.

```bash
heroku container:login
```

then run this:

`<heroku-app-name>`: the heroku app name we used in the section of Heroku whenc reating the app. this env variable `HEROKU_APP`

```bash
docker build --pull -t ghibli-heroku .
docker tag ghibli-heroku registry.heroku.com/<heroku-app-name>/web
docker push registry.heroku.com/<heroku-app-name>/web
heroku container:release web -a <heroku-app-name>
```

  
## WHATS NEXT
#### 1. Thoughts on improving it.

###### Testing
- Add unittest, integration and system tests within Django app "movies/" folder "tests" with the folder architecture in place.

###### App
- Set up error handling and pages
- Set up error tracking (Sentry). it's already configured in the web app, but need to create the app and get the dns url sentry gives you and added to the environment variables in the settings of the heroku server.
- we want to handle to some data for more than 60 in case the erd-party ghibli api fails.
- We want to handle once the server is commissioned for the first time to retrieve the data from the ghibli api, so the user must not wait the first time he goes into our site.
 
###### Ghibli Api
- Test and do profiling on the relationship (movies/ and people/) and refactor to a better and fastest approach.



## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Django                    | ![django][django]                     | Web Framework |
| Requests                  | ![requests][requests]                 | HTTP Library |
| Requests HTML             | ![requests-html][requests-html]       | Parsing HTML |
| SQLite (dev)              | ![sqlite][sqlite]                     | Database |
| PostgreSQL (prod)         | ![postgres][postgres]                 | Database |
| Uwsgi                     | ![uwsgi][uwsgi]                       | Web Server Gateway Interface |
| Nginx                     | ![nginx][nginx]                       | Web server |
| Debug Tool Bar            | ![django-debug-toolbar][django-debug-toolbar] | Analyze SQL queries |
| Docker                    | ![docker][docker]                     | Containers |
| Heroku                    | ![heroku][heroku]                     | Cloud provider |
| Pytest                    | ![pytest][pytest]                     | Test framework |
| Flake8                    | ![flake8][flake8]                     | Code style |
| Black                     | ![black][black]                       | Code style |
| Isort                     | ![isort][isort]                       | Code style |
| Mypy                      | ![mypy][mypy]                         | Code quality |
| Snyk                      | ![snyk][snyk]                         | Security tool |
| Bandit                    | ![bandit][bandit]                     | Security tool |
| Safety                    | ![safety][safety]                     | Secutiry tool |
| Python Security           | ![python-security][python-security]   | Guess what? |
| Sentry                    | ![sentry][sentry]                     | Monitoring |
| UpTime Robot              | ![uptimerobot][uptimerobot]           | Monitoring |

<br><br>


## Maintainer
Get in touch -–> [Website][fantaso]



<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://www.fantaso.de/
<!-- Extra -->


<!-- Repos -->
[github-repo]: https://gitlab.com/fantaso/ghibli-studio

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[django]: readme/django.png
[requests]: readme/requests.jpg
[requests-html]: readme/requests-html.png

[postgres]: readme/postgresql40x40.png
[sqlite]: readme/sqlite40x40.png
[uwsgi]: readme/uwsgi40x40.png
[nginx]: readme/nginx40x40.png

[django-debug-toolbar]: readme/django-debug-toolbar.png

[docker]: readme/docker40x40.png
[heroku]: readme/heroku40x40.png

[pytest]: readme/pytest40x40.png
[flake8]: readme/flake840x40.png
[black]: readme/black40x40.png
[isort]: readme/isort40x40.png
[mypy]: readme/mypy40x40.jpeg

[snyk]: readme/snyk40x40.png
[bandit]: readme/bandit40x40.png
[safety]: readme/safety40x40.jpg
[python-security]: readme/python-security40x40.png

[sentry]: readme/sentry40x40.png
[uptimerobot]: readme/uptimerobot-icon-nobg40x40.png