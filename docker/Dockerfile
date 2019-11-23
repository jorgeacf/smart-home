FROM python:3.8.0-slim

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

ENTRYPOINT [ "python", "tasks" ]