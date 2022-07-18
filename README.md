# AAwards Clone

## Description

This Application is a clone of AWWWARDS site.Users to rate projects on the site and post their own for review.The User can signup and create a profile,update their profile and upload a project for review.Users also can use my API. 


## Author

Sandra 

You can view the site at:[AAwards]()


## User Stories
As a user I would like to:
* See various projects and their details  
* Copy link of the projects 
* Allowed to search for projects
* Allowed to search create an account and profile
* Allowed to post projects and rate other projects


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display of projects | **On page load** | List of various projects on site displayed on a page|
| Search for projects| **On search bar click submit** | see projects details searched for |
| Rate projects | **On signin** | allowed to rate projects|
| Create profile | **on signup and login** | update profile with details|
| Upload projects | **On log in** |  upload,save,delete and update projects|
|Rate projects | **on sign in** | rate projects


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pipenv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/Awards-project.git
        $ cd Awards

## Running the Application
* Creating the virtual environment

        $ pip3 install pipenv 
        $ pipenv shell
        
       


* To run the application, in your terminal:

        $ python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python3.8  manage.py tests 

## Technologies Used
* Python3.8
* Django 4.0.4
* Heroku

## Known Bugs
Rating on projects not diplayed
Users Can't update or delete uploaded projects

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/Awards-project.git)**

