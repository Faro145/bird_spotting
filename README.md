# bird_spotting

# Goal

The goal of this project was to create a application that could create, read, update and delete while showing all the resources and techniques that we had learned about during training.

This need to include:

* A Trello board (or equivalent Kanban board)
* A relational database 
* Clear Documentation from a design phase 
* A functional CRUD application created in Python
* Fully designed test suites for the application
* A functioning front-end website and integrated API's, using Flask
* Code fully integrated into a Version Control System

# My Approach
A CRUD application which was designed to record bird sightings in various locations in the UK. This would present a basic idea of what birds there are in their respective area. It would allow me to do the following:

* Create - generate a three table database which would display the bird species, locations visited and the sightings of birds in these locations.
* Create - allow users to add birds and locations that were previously not in the database as well as any new bird sightings
* Read - View the tables containing the bird, location and sighting information
* Update - Correct any entries that had any incorrect bird or location information as any sightings that were inaccurate upon review
* Delete - Delete any records in the tables

In addition, I also wanted validators to make sure that all the information was entered to avoid blank spaces in the tables and that any sightings were in one of Scotland, England, Northern Ireland or Wales. 

# Architecture

## Database Structure

The link below is to an entity relationship diagram (ERD) showing the structure of the database.

https://docs.google.com/presentation/d/1I5Vgah-aS1d6ehUzF_mbHez4hiHRadjdXI2DxiJPrJs/edit

As shown in the ERD, the app models a many-to-many relationship between Bird entities and Location entities using the Sightings table. This is due to the fact that that many bird species can be present in many locations. In addition, any bird sepcies or location can have many sightings. Conversely, one sighting can only have one bird species and one location.

## CI Pipeline Structure

The CI pipeline (which is pictured in the link below) displays how the code written in Python is transport to GitHub via Git. GitHub provides the repository and the means to track the progress of the project. The repository is then pulled to a Jenkins server which provides a platform to build the application and run tests. The application has been developed using a virtual machine provided by Google Cloud Platform and a Flask framework.

https://docs.google.com/presentation/d/1uWjxWMigDzbH3BCqg1A-Ra0ytrCeNCggHmaci-6yE20/edit#slide=id.p

# Progress Tracking

The Projects feature in GitHub has been utilised to assist with keeping track of the progress of the development of the application. This can be found by clicking the Projects tab in this repository or by clicking the link below 

https://github.com/Faro145/bird_spotting/projects/1 

The board was split into three sections: "To do", "In Progress" and "Done". The "To do" section contains the elements that were planned but not initiated. The "In Progress" section contains the entries that were being worked on. Elements were generally worked on two at a time. However, the element(s) in the "To do" section would stay there if the element that was situated in the "In Progress" section was required to be completed for that to occur. Any elements that were finalised were placed in the "Done" section. Each element contained the user story described the need of the user for that element and the tasks required to accomplish it.   

# Risk Assessment

The risk assessment for this project is available in the link below. 

https://docs.google.com/spreadsheets/d/19eloi729DitI9hjlmfEKlpPphg7PyE3d/edit#gid=1091987158

It contains the risks determined for this project as well as the impact, probability and overall level of each risk. Mitigations have also been provided for these risks. In addition, the risks are adjusted after the mitigations and further reviewed in later updates.

# Testing

pytest is used to perform Unit Testing and Integration Testing. A testing coverage report is also produced to illustrate the percentage of the application code that has been tested. An example of the results and coverage report can be viewed in the link below. 

https://docs.google.com/presentation/d/1E0sHe8bjlIzBIoYHBq1LzY8LcAYeNWuhP8pP69sJCM4/edit?usp=sharing

# Front-End Design

The front-end design can be observed using the link below.

https://docs.google.com/presentation/d/1VjHSpiTrU60FMd6aJUEFnvKqXvlnchij1nJ-xaGVvis/edit?usp=sharing

Slides one and two display what happens when the application is run on Jenkins and the recorded actions that can occur when using the application. This is present on an assigned url. Slide three displays the home page which contains the three tables. Slide four demonstrates what happens when you click the "Add Location" button in the navbar. This is where you enter a new location to the database. Slide five illustrates the home page after you have added a location. Each entry has an update and a delete button below it. If you click the update button: you will be redirected to the update url which will contain a similar layout as slide four. If you click the delete button the entry will be removed from the database. Slides six and seven demonstrate what happens if click on the "Add Bird" and "Add Sighting" buttons respectively. They also have a similar user journey as described from slides three to five. However, the data entry would be added to a different table (Birds if slide 6 or Sightings if slide 7). The addition of a new sighting would require the bird and location entries for that sighting. This is due to each sighting containing both a location ID number and a Bird ID number. 

# Known Issues
* The sighting table does not currently display data on the application (despite it arriving in the database)
* Update function does not function properly in the Locations table


# Future Improvements

* CSS could be used to make the application more visually pleasing 
* Adding a Search Bar to locate specific locations, birds or sightings
* 

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


pip3 install -r requirements.txt


Finally create the database and run the application.


python3 create.py

python3 app.py
