
## Setup

- Create virtualenv and install django

- django-admin startproject exercise_proj

- python manage.py startapp workouts

- add 'workouts' to INSTALLED_APPS in settings.py


## Models

- Create model in workouts/models.py. Notice format string variables with {var=} to print the variable name plus it's value. This was introduced in Python 3.8 so remove the = if using Python 3.7 or earlier, or you'll get errors with this syntax. 

- Register model in workouts/admin.py.  Not required but makes it easier to see what's in your DB

- python manage.py makemigrations

- python manage.py migrate 


## URLs

- Create new workouts/urls.py

- Add line to exercise_proj/urls.py to include new workouts/urls.py routes

- Create new URL path in exercise_proj/urls.py to show workout list for '/'


## Views and templates 

- Create new function in exercise_proj/views.py to handle request 

- Create new template  workouts/templates/workout_list for list of all workouts 

- Go into admin console and add example workout(s)

    - "Push ups" focus "Arms" rating true video ID 0pkjOk0EiAk
    - "Jumping Jacks", focus "Cardio" rating: false, video ID c4DAnQ6DtF8
        - The ID is in the URL, the original URL is https://www.youtube.com/watch?v=c4DAnQ6DtF8

- Check page works, you see videos

## Create base template 

Using WaterCSS for styles, primarily for the forms and buttons.

https://kognise.github.io/water.css/

## Etc

todo 

# Forms - new search form 
