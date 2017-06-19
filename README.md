#APP for my tests

#чтоб был проброс порта и видно в докер сети
sudo docker run -p 5000:80 -d -P --net foodtrucks --name static-site4 prakhar1989/static-site

