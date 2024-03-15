# Use the official PHP image
FROM php:7.4-apache

# Create a new user with UID/GID 1000
RUN useradd -u 1000 -ms /bin/bash appuser
RUN apt-get update && apt-get install socat -y
# Copy the PHP files to Apache's document root
COPY index.php /var/www/html/index.php

# Change ownership of the document root to the new user
RUN chown -R appuser:appuser /var/www/html

# Expose port 80 to the outside world
EXPOSE 80

COPY flag.txt /flag.txt
RUN chmod 444 /flag.txt

# Switch to the new user
USER appuser

# Start Apache
CMD ["apache2-foreground"]
