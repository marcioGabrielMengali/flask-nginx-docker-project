# Fullcycle Project Nginx with Flask

> This project I made an adaption to use flask, because i work mostly with python.

# Running the Project

> docker-compose -f docker-compose.prod.yml up -d --build

## Run the project First time create table on the db container.

> docker exec app python manage.py create_db

# Acces:

> http://localhost:8080