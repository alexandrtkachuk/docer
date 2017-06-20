# Version: 0.0.1


FROM php:7.0-apache
#COPY ./public-html/ /usr/local/apache2/htdocs/

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y mysql-client
WORKDIR /tmp/

USER daemon
RUN mkdir wp 
WORKDIR /tmp/wp/
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN php wp-cli.phar core download --locale=ru_RU
RUN php wp-cli.phar core config --dbname=wpclidemo --dbuser=root --dbpass=test --dbhost=localhost:8000
RUN php wp-cli.phar db create
RUN php wp-cli.phar core install --url=wpclidemo.dev --title="WP-CLI" --admin_user=wpcli --admin_password=wpcli --admin_email=info@wp-cli.org
USER root
WORKDIR /var/www/html/
RUN cp /tmp/wp . -r
EXPOSE 80

