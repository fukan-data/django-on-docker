# django-on-docker

This is an sample of building a Django environment on Docker using Nginx, Gunicorn, and PostgreSQL.

# Usage

## Git clone  

```bash
$ git clone git@github.com:dsonoda/django-on-docker.git
```

## Building a development environment  

#### Goal  

Use docker-compose to set up a service-specific container on a single host to build a Django web application development environment. The host is assumed to be in a local environment.  

![](https://github.com/dsonoda/django-on-docker/blob/images/django_on_docker_development.png)  

#### 1. Edit ```.env.development``` and set the environment variables  

```.env
SECRET_KEY=[django secret key value]
DB_PASSWORD=[db password]
POSTGRES_PASSWORD=[db user password]
```

#### 2. Launch the containers  

```bash
$ cd django-on-docker
$ docker-compose -f docker-compose.development.yml up -d --build
...
Creating django-on-docker_db_1 ... done
Creating django-on-docker_app_1 ... done
Creating django-on-docker_nginx_1 ... done

$ docker-compose -f docker-compose.development.yml ps -a
        Name                        Command               State          Ports
----------------------------------------------------------------------------------------
django-on-docker_app_1     /usr/src/app/entrypoint.de ...   Up      8000/tcp
django-on-docker_db_1      docker-entrypoint.sh postgres    Up      5432/tcp
django-on-docker_nginx_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:1337->80/tcp
```

#### 3. Initialization  

All data deleted.  
Remove data from all tables except for some, such as migration management.  

```bash
$ docker-compose -f docker-compose.development.yml exec app python manage.py flush --no-input
```

Generating a migration files.  
If a model modification occurs in subsequent development, it must be run again.  

```bash
$ docker-compose -f docker-compose.development.yml exec app python manage.py makemigrations
```

Create DB tables from the generated migration files.  
If a model modification occurs in subsequent development, it must be run again.  

```bash
$ docker-compose -f docker-compose.development.yml exec app python manage.py migrate
```

Move the static files into the static directory.  

```bash
$ docker-compose -f docker-compose.development.yml exec app python manage.py collectstatic --no-input --clear
```

Registering an administrative user.  

```bash
$ docker-compose -f docker-compose.development.yml exec app python manage.py createsuperuser
Username (leave blank to use 'app'): [admin user name]
Email address: [admin user email]
Password: [admin user password]
Password (again):
Superuser created successfully.
```

#### 4. Access pages  

|page|url|note|
|:---|:---|:---|
|Frontend file upload page|http://localhost:1337/uploads/|Try file upload.|
|Admin login|http://localhost:1337/admin/login/|Enter the registered administrator's information.|

#### 5. Other commands  
Stop the container and suspend development.  

```bash
$ docker-compose -f docker-compose.development.yml stop
```

Start the container and resume development.  

```bash
$ docker-compose -f docker-compose.development.yml start
```

Restart the container.  

```bash
$ docker-compose -f docker-compose.development.yml restart
```

Destroy images, containers, volumes, and networks.  

```bash
$ docker-compose -f docker-compose.development.yml down
```

If you want to modify only the app code and check the result, restart the app container only.  

```bash
$ docker container restart django-on-docker_app_1
```

## Building a production environment  
Recently Announced.  

# Author  

- Daisuke Sonoda  
- mail@daisukesonoda.com  

# License  

This repository is under [MIT license](https://github.com/dsonoda/django-on-docker/blob/main/LICENSE).  


# 追記

側用人＜最新＞
https://github.com/dsonoda/django-on-docker
wsl
sudo service docker start
source venv/bin/activate
docker-compose -f docker-compose.development.yml up -d --build

DB確認
docker-compose -f docker-compose.development.yml exec app python manage.py dbshell

docker全削除
docker-compose -f docker-compose.development.yml down --rmi all --volumes --remove-orphans


http://localhost:1337/admin/login/
sato
sudo -> み?カ<user>
docker-compose -f docker-compose.development.yml exec app /bin/sh

venvの仮想環境構築
cd /var/app/django-on-docker
python3 -m venv venv
source venv/bin/activate
python -V

black app/
https://blog.hirokiky.org/entry/2019/06/03/202745

