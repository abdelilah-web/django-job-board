 - frontend template
 - virtualenv : 
    - create 
    - activate [windowds : source ./scripts/activate]
    - pip install 
    - deactivate 

- upload project on github

- url : path 
- view : logic 
- models : db
- templates : frontend





Relations : 
    - One to many    [ user - posts ]   Foreginkey
    - Many to many   [ user - groups ]  
    - One to one  [ user - profile ]




static files : [frontend] images , css , javascript 
                we modify in settings
                and we creat a folder by the name of static we add to it (css, js, img, fonts)
                and we modify in the template : - {% load static %}
                                                - and we modify in href ex : href="{% static 'css/bootstrap.min.css' %}"
media files : [upload] images