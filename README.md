# Yamdb_final
### Workflow status
![yamdb_final workflow](https://github.com/feyaschuk/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

### link to running project 
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

### How to use:
* Install docker 
```
https://docs.docker.com/get-docker/
```




Deploy
Local:
Delete whole dir .github/workflows
Uncomment .env in .gitignore and set secrets in .env like:
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=TRUE # if you want to work in dev
ALLOWED_HOSTS=host1, host2, etc 
CORS_ALLOWED_ORIGINS=host1, host2, etc. # uncomment CORS_ALLOWED_ORIGINS and comment CORS_ALLOW_ALL_ORIGINS in settings.py, if you want  special hosts for CORS
DJANGO_SUPERUSER_USERNAME=admin # set instead admin, username of superuser
DJANGO_SUPERUSER_EMAIL=admin@gmail.com # set instead admin@gmail.com, email of superuser
DJANGO_SUPERUSER_PASSWORD=admin # set instead admin, password of superuser
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # set instead postgres, name of db
POSTGRES_USER=postgres # set instead postgres, nikname of superuser of db
POSTGRES_PASSWORD=postgres # set instead postgres, password of db
DB_HOST=db # you can rename it or set a needed host, but before make changes to docker-compose.yaml
DB_PORT=5432


Install docker https://docs.docker.com/get-docker/

If you don't need any files or dirs in container, you can set them in .dockerignore
In dir with project run:
$ docker-compose up
Open a new window of terminal and from dir of project run:
$ docker-compose exec web ./manage.py migrate --noinput
$ docker-compose exec web ./manage.py database
$ docker-compose exec web ./manage.py create_admin
$ docker-compose exec web ./manage.py collectstatic --no-input 
You can get admin panel in http://localhost/admin/ with username and password, that you set in .env (DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_PASSWORD)
Continuous Integration and Continuous Deployment with testing by GithubActions:
Install Docker and Docker-compose on your server.
Copy docker-compose.yaml and nginx/default.conf to your server
Prepare your repository in GitHub:
In settings of repo find secrets and set in them:
DOCKER_PASSWORD, DOCKER_USERNAME - for pull and download image from DockerHub
SECRET_KEY, ALLOWED_HOSTS - for django app
DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT - to connect to default database
DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD - for creating superuser
After push to github, the main application will pass the tests, update the image on DockerHub, and deploy to the server. Next, you need to connect to the server.
$ ssh <USER>@<HOST>
Run comands like after 'docker-compose up' in local deploy, but with 'sudo', like:
$ sudo docker-compose exec web ./manage.py migrate --noinput
$ etc.
Documentation and requests examples
If you local deployed project, you can see that here:
Task and full documentation (Redoc)
Documentation and requests - Swagger
Documentation and requests - Redoc
If not local:
://yourhost/redoc/ - Task and full documentation
://yourhost/swagger/ - Swagger
://yourhost/redoc_main/ - Redoc
