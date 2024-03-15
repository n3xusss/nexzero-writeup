FROM php:7.4-apache

WORKDIR /var/www/html

COPY challenge/*.php ./

COPY challenge/flag.txt /flag.txt

EXPOSE 80

CMD ["apache2-foreground"]
