***
In this project we are going to provide a list of feeds that are available in 
database and make it possible for each user to give each feed a rating. 
User's should be logged-in before using the APIs.
<br>
Following are a list of available APIs that we need in order to work with the project:
- admin/
- feeds/list/ 
- feeds/list/{id}/
- feeds/rate/
- feeds/rate/{id}/
- auth/login/
- auth/logout/
- auth/registration/

Also, we are using browsable API from django-rest-framework which helps us to work with
APIs more convenient. 

*Note that this is a test project and secret keys in settings.py are public
