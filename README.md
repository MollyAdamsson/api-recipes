# Elevated Eats API

* This is the backend service used by the Elevated Eats Application

## Development Goals

* The main goal for this API is to provide a good backend service that supports the Elevated Eats front end and makes sure it performs accordingly.

## Project Planning

This project was created via agile methods during two weeks.
I used the Kanban board to easily organize my work, you can find this via the github projects <here>. The developer creates cards to help them during the development, this is mainly to make it easier to keep track of the different user stories and make sure everything is completed.

- image here

## Epics

### Set up

### Posts

### Comments

### Profiles

### Followers

### Likes

### Contacts

### Recipes

### Reviews


# User Stories

* Set up

* Posts

* Comments

* Profiles

* Followers

* Likes

* Contacts

* Recipes

* Reviews

# API Endpoints

# Security

* The permission class that handles who gets to delete and edit the content based on owner was added, its called IsOwnerOrReadOnly. 

# Technologies
* Django
Main framework used for application creation
* Django REST Framework
Framework used for creating API
* Cloudinary Platform
Used for static image hosting
* Heroku
Used for hosting the application
* Git
Used for version control
* Github
Repository for storing code base and docs

# Python Packages

* .....

* Installed as package dependcies with above installations:

# Testing


### Bugs and their fixes

## Deployment

### [Elephantsql](https://www.elephantsql.com/) 

* Heroku needs sql's to work
* ElephantSQL will manage administrative tasks of PostgreSQL, such as installation, upgrades to latest stable version and backup handling.
* It automates every part of setup and running of PostgreSQL clusters.

1. Log into Heroku 
The first step to creating a free PostgreSQL database is to log in to Heroku. To create a new database on Heroku, an app must first be created within the personal dashboard. 

2. Create a new Heroku app 
Once logged in to Heroku, navigate to the personal app dashboard to create a new Heroku app. Simply click the Create new app button, which should be located on the top-right corner of the dashboard. 

3. Add a PostgreSQL database 
After creating the new app, it's time to attach a PostgreSQL database to it. Simply navigate to the Resources tab located in the header of the app's dashboard. Add the ElephantSql and a free PostgreSQL database has now been successfully created. 

### [Github](https://github.com/) 

* When logging into github, navigate to the settings tab
* Here you can find pages down on the left side
* A new page will load which will present the branch to master or main, and then the save option
* Once the save button has been clicked and the page is reloaded there will be a link to the deployed site.

### [Heroku](https://www.heroku.com/) Deployment:

* Ensure your requirements.txt file has the required dependencies. To do this you can use the following
code in your IDE: pip3 freeze > requirements.txt
* Create or login to you Heroku account
* Navigate to Dashboard
* Click and select "Create app" in the middle of the page
* Enter a unique name for you app
* Select region and the "create app"

### App deployment
* Navgiate to the deploy section
* Scroll down to the "deployment method" and select "Github"
* Authorise the connection
* Also important to make sure you have the right config variables applied, these change the way the app behaves. 
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
* * SECRET_KEY: (Your secret key)
* * DATABASE_URL: (This should already exist with add on of postgres)
* * EMAIL_HOST_USER: (email address)
* * EMAIL_HOST_PASS: (email app password)
* * CLOUNDINARY_URL: (cloudinary api url)
* Search for the repository name you've chosen
* Make sure you have selected the correct branch (master/main), and select the method you desire.