# POLESTAR Python assignment

This project was developed using Python flask framework

## Installation

Activate python virtual environment from pole (base) directory using the command

command: source bin/activate

## Python libraries

All python libraries are available at

pole/lib/python3.7/site-packages 

## Import csv data and python test execution

Navigate to app folder


command: cd app


and run pytest to execute csv import and test case execution


command: pytest



## Running flask api and html page

run below commands from app folder

set environment variable flask_app


command: FLASK_APP=app.py


run flask application

command: flask run

UI can be viewed after running the application 

http://localhost:5000/

ships api

http://localhost:5000/api/ships/


get positions api

http://localhost:5000/api/positions/9247455/
