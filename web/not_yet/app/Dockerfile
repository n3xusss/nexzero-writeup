FROM php:8.2.12-apache
WORKDIR /var/www/html
COPY index.php s3cR33Ttt.php sitemap.xml /var/www/html/
COPY flag.txt encryption.txt /home/
RUN useradd -ms /bin/bash ctf
RUN chown -R ctf:ctf /var/www/html/
RUN chown -R ctf:ctf /home
EXPOSE 80
USER ctf
CMD ["apache2-foreground"]
