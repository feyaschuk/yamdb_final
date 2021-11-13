# Yamdb_final d
### Workflow status
![yamdb_final workflow](https://github.com/feyaschuk/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)
<p dir="auto"><a href="https://www.python.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/56f517b8a6a9ae6c1e67721d05ecfb6f6e23da70303349909fc049b44348087e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d6666646535373f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e" alt="Python" data-canonical-src="https://img.shields.io/badge/-Python-ffde57?style=flat-square&amp;logo=Python" style="max-width: 100%;"></a>
<a href="https://www.djangoproject.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/e9c106ec5d7b3f59ec614b2fea30b56341a4569e72c9b6147259feaf94a759ff/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f2d3039326532303f7374796c653d666c61742d737175617265266c6f676f3d446a616e676f" alt="Django" data-canonical-src="https://img.shields.io/badge/-Django-092e20?style=flat-square&amp;logo=Django" style="max-width: 100%;"></a>
<a href="https://www.django-rest-framework.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/923b97514c38493e8e996d8a4f2f5f47ebe17cfa7f87f01188b228d3489e3a20/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f253230524553542532304672616d65776f726b2d6339353130633f7374796c653d666c61742d737175617265266c6f676f3d647266" alt="Django REST Framework" data-canonical-src="https://img.shields.io/badge/-Django%20REST%20Framework-c9510c?style=flat-square&amp;logo=drf" style="max-width: 100%;"></a>
<a href="https://www.postgresql.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/a30cd887333f3d98e4ea39fbc2baef6169fd91c97993cc8e9e349ac80e970b9e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d506f737467726553514c2d6262656564643f7374796c653d666c61742d737175617265266c6f676f3d506f737467726553514c" alt="PostgreSQL" data-canonical-src="https://img.shields.io/badge/-PostgreSQL-bbeedd?style=flat-square&amp;logo=PostgreSQL" style="max-width: 100%;"></a>
<a href="https://gunicorn.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/ba1dea441993e4724bfdac547509aa07310f76f941263fb13fc9a2c8f587ad75/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d67756e69636f726e2d3030383237323f7374796c653d666c61742d737175617265266c6f676f3d67756e69636f726e" alt="gunicorn" data-canonical-src="https://img.shields.io/badge/-gunicorn-008272?style=flat-square&amp;logo=gunicorn" style="max-width: 100%;"></a>
<a href="https://github.com/features/actions"><img src="https://camo.githubusercontent.com/ba2a3b5f07c69283fef98a4baa8f15b2343ce911a321163ee670d3976f76cb87/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d476974487562253230416374696f6e732d6635663566353f7374796c653d666c61742d737175617265266c6f676f3d476974487562253230616374696f6e73" alt="GitHub%20Actions" data-canonical-src="https://img.shields.io/badge/-GitHub%20Actions-f5f5f5?style=flat-square&amp;logo=GitHub%20actions" style="max-width: 100%;"></a>

#### Link to running project 
```
http://130.193.53.130/redoc/
```

#### About
The YaMDb project collects user feedback on various works. The works are divided into categories: "Books", "Films", "Music". The list of categories can be expanded by the administrator.
The works themselves are not stored in Review, you can not watch a movie or listen to music here.
In each category there are works: books, movies or music.
A work can be assigned a genre from the list of preset ones. Only the administrator can create new genres.
Grateful or outraged users leave text reviews for the works and give the work a rating in the range from one to ten (an integer); an average rating of the work is formed from user ratings — a rating (an integer). The user can leave only one review for one work.

#### Functionality
Getting confirmation code using email and then Auth with JWT-token.
Permission system for different roles: admin/moderator/user.
Create, Read, Update, Delete title, category, genre, review, comment.

## Continuous Integration and Continuous Deployment with testing by GithubActions

### How to use:

#### 1. Install Docker and Docker-compose on your server.
```
https://docs.docker.com/get-docker/
https://docs.docker.com/compose/install/
```
#### 2. Clone the repository and go to it on the command line:
```
git clone https://github.com/feyaschuk/yamdb_final.git
```

#### 3. Copy docker-compose.yaml and nginx/default.conf to your server
```
scp docker-compose.yaml server_username@server:/home/<your_username>/docker-compose.yaml
scp -r nginx/default.conf server_username@server:/home/<your_username>/nginx/default.conf
```
#### 4. Prepare your repository in GitHub:
In settings of repo find secrets and set in them:
```
DOCKER_PASSWORD, DOCKER_USERNAME - for pull and download image from DockerHub
```
```
SECRET_KEY, ALLOWED_HOSTS - for django app
```
```
DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT - to connect to default database
```

#### 5. After "push" to github, the main application will pass the tests, update the image on DockerHub, and deploy to the server.

#### 6. Connect to the server
In terminal put command:
```
ssh <USER>@<HOST>
```
#### 7. Run comands afterwards in local deploy, but with 'sudo':

* Run migrations:
```
sudo docker-compose exec web python manage.py migrate --noinput
```
* Create superuser:
```
sudo docker-compose exec web python manage.py createsuperuser
```
* Load statics - project design:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
* Load dump object:
```
sudo docker-compose exec web python manage.py loaddata fixtures.json
```
#### 8. If you want to stop the process and remove containers:
```
sudo docker-compose down
```

#### Documentation and requests examples
://yourhost/redoc/ - Task and full documentation

#### Using technologies:

* Django==3.0.5
* django-filter==21.1
* djangorestframework==3.11.0
* djangorestframework-simplejwt==5.0.0
* gunicorn==20.1.0
* psycopg2-binary==2.8.6
* pytest==6.2.4
* python-dotenv==0.13.0
* requests==2.26.0

#### Author: Mariya Yaschuk
