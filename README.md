# web
A simple Python web-service that always returns 'Ok'

## How to run?
Use the following command to run this container:

    docker run --name web -d -p 80:6000 dadvisor/web:latest
    
Or build from source:

    docker build -t web .
    docker run --name web -d -p 80:6000 web