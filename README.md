#APP for my tests

#чтоб был проброс порта и видно в докер сети
sudo docker run -p 5000:80 -d -P --net foodtrucks --name static-site4 prakhar1989/static-site

#mysql with root pass test
docker run  -d -p 8000:3306   -e MYSQL_ROOT_PASSWORD=test mysql

