FROM php:7.4-apache

RUN adduser --disabled-password --no-create-home ctf

WORKDIR /var/www/html

COPY challenge/*.php ./

COPY challenge/*.sh ./

COPY challenge/flag.txt /opt/usr/s3cr3t/

EXPOSE 80

RUN chmod +x ./entrypoint.sh

CMD ["apache2-foreground"]
