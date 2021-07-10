# Polling Application
A Django based project to allow users to create polling questions with four options. Users can also cast votes for different polls created by all other users. 

## Technologies Used:
* Django = 3.2.3
  
## How to use:
  
#### Clone this project:
```
$ https://github.com/atharvamishra123/PollingApplication.git
``` 

#### Install dependencies:
```
$ pip install -r requirements.txt
```

#### Go to the directory in which you have manage.py:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create superuser:
```
$ python manage.py createsuperuser
```

#### Run the server on local:
```
$ python manage.py runserver
```
 
#### On a browser, open:
```
$ http://127.0.0.1:8000/signup/
```

###### Now you can signup, login, create polling question and vote in other questions
###### You can go to django admin at http://127.0.0.1:8000/admin/ to view the models registered.
