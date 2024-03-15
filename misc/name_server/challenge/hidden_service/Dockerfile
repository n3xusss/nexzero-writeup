FROM php:7.4-apache AS builder

WORKDIR /app

# Copy PHP application files
COPY . /app

# Stage 2: Create the final image
FROM php:7.4-apache

# Install Tor and other necessary packages
RUN apt-get update && \
    apt-get install -y tor && \
    rm -rf /var/lib/apt/lists/*


# Copy the built PHP application from the builder stage
COPY --from=builder /app /var/www/html

# Expose the port your Apache server will run on
EXPOSE 80

COPY . /hidden-service

RUN chmod -R 400 /hidden-service/*
RUN chmod 400 /hidden-service

CMD ["sh","-c","tor -f /hidden-service/torrc & apache2-foreground"]




