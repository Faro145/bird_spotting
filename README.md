# bird_spotting

# Description
This is a CRUD application which is designed to record bird sightings in various locations in the UK. This presents a basic idea of what birds are in their respective area.

# Dependencies
This is a Flask application that requires Python3 as well as pip3 and a virtual environment. Perform the following sudo commands:


sudo apt update
sudo apt install python3 python3-pip python3-venv python3-flask python3-flask-sqlalchemy


Then create and activate the virtual environment.


python3 -m venv venv
. venv/bin/activate


The pip3 installations are the next priority.


pip3 install flask flask_sqlalchemy flask-wtf wtforms


Finally create the database and run the application.


python3 create.py
python3 app.py
