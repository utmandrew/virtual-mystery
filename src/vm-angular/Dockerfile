# Installs the current application on a Node Image.
FROM node:10.5

# what is this for here??? 
# "qq is for silent output in the console"
RUN mkdir /usr/src/app 
WORKDIR /usr/src/app

RUN npm install -g @angular/cli
COPY . /usr/src/app

CMD ng serve --host 0.0.0.0 --port 4200
 

#RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim


# Copies all the content
#COPY . .

#run installing the requirements file 
#RUN pip install -r Requirements.txt


# Install all the packages
#RUN npm install -g @angular/cli
#RUN yarn install


# Uncomment this if you went with Option #2 in Step #2 (Windows Only)
# RUN npm rebuild node-sass --force
# The default port from ng serve (4200)
# and 49153 for Webpack Hot Module Reload
# what is the purpose of this
#EXPOSE 4200 49153