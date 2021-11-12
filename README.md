# Yamdb_final
### Workflow status
![yamdb_final workflow](https://github.com/feyaschuk/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

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

### How to use Continuous Integration and Continuous Deployment with testing by GithubActions:

#### 1.Install Docker and Docker-compose on your server.
```
https://docs.docker.com/get-docker/
https://docs.docker.com/compose/install/
```
#### 2.Clone the repository and go to it on the command line:
```
git clone https://github.com/feyaschuk/yamdb_final.git
```

#### 3.Copy docker-compose.yaml and nginx/default.conf to your server
```
scp docker-compose.yaml server_username@server:/home/<your_username>/docker-compose.yaml
scp -r nginx/default.conf server_username@server:/home/<your_username>/nginx/default.conf
```
#### 4.Prepare your repository in GitHub:
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

#### 5.After "push" to github, the main application will pass the tests, update the image on DockerHub, and deploy to the server.

#### 6.Connect to the server
In terminal put command:
```
ssh <USER>@<HOST>
```
#### 7.Run comands afterwards in local deploy, but with 'sudo':

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

#### Documentation and requests examples
://yourhost/redoc/ - Task and full documentation

#### Using technologies:

Django==3.0.5
django-filter==21.1
djangorestframework==3.11.0
djangorestframework-simplejwt==5.0.0
gunicorn==20.1.0
psycopg2-binary==2.8.6
pytest==6.2.4
python-dotenv==0.13.0
requests==2.26.0

#### Author: Mariya Yaschuk
