# ==================================
# nodejs-deserialization dockerfile
# ==================================
FROM node:argon
MAINTAINER Mikael Kall <kall.micke@gmail.com>

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

# Expore port
EXPOSE 3000

# Start application.
CMD [ "npm", "start" ]
