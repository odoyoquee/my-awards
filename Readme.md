# Awards

>[odoyoquee](https://github.com/odoyoquee) 

# Description 

This project allows users to post their projects for other users to rate according to design, usability and content.

## Live Link

## User Story  
  
* A user can view posted projects and their details. 
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects. 
* Search for projects. 
* View projects overall score. 
* A user can view their profile page.

## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
 https://github.com/odoyoquee/my-awards
```
##### Navigate into the folder
 ```bash 
cd project-my-awards
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual
- source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```
##### Setup Database  
SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
  Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

