# bird_spotting

# Goal

The goal of this project was to create a application that could create, read, update and delete while showing all the resources and techniques that we had learned about during training.

This need to include:

* A Trello board 
* A relational database 
* Clear Documentation from a design phase 
* A functional CRUD application created in Python
* Fully designed test suites for the application
* A functioning front-end website and integrated API's, using Flask
* Code fully integrated into a Version Control System

# My Apporach
A CRUD application which was designed to record bird sightings in various locations in the UK. This would present a basic idea of what birds there are in their respective area. It would allow me to do the following:

* Create - generate a three table database which would display the bird species, locations visited and the sightings of birds in these locations.
* Create - allow users to add birds and locations that were previously not in the database as well as any new bird sightings
* Read - View the tables containing the bird, location and sighting information
* Update - Correct any entries that had any incorrect bird or location information as any sightings that were inaccurate upon review
* Delete - Delete any records in the tables

In addition, I also wanted validators to make sure that all the information was entered to avoid blank spaces in the tables and that any sightings were in one of Scotland, England, Northern Ireland or Wales. 

# Architecture

## Database Structure

Pictured below is an entity relationship diagram (ERD) showing the structure of the database.

![Schema](Project Draft.png)

As shown in the ERD, the app models a many-to-many relationship between Bird entities and Location entities using the Sightings table. This is due to the fact that that many bird species can be present in many locations. In addition, any bird sepcies or location can have many sightings. Conversely, one sighting can only have one bird species and one location.

# Author
Ross Farquhar

# Dependencies
This is a Flask application that requires Python3 as well as pip3 and a virtual environment. Perform the following sudo commands:


sudo apt update

sudo apt install python3 python3-pip python3-venv python3-flask python3-flask-sqlalchemy 


Then create and activate the virtual environment.


python3 -m venv venv

. venv/bin/activate


The pip3 installations are the next priority.


pip3 install flask flask_sqlalchemy pymysql flask-wtf wtforms 


Finally create the database and run the application.


python3 create.py

python3 app.py
