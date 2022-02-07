# url-shortning

Install virtualenv
```
pip install virtualenv
```
On the project directory,

Create virtual environment
```
virtualenv venv
```
Activate
```
source venv/bin/activate
```

Install requirements including dependencies
```
pip install -r requirements.txt
```

Do Database migrations
```
./manage.py makemigrations
./manage.py makemigrations chat
./manage.py migrate
```

Try creating a superuser for user management
```
./manage.py createsuperuser
```

Give necessary inputs

Run development server

```
./manage.py runserver 0.0.0.0:8080
```


Services

1.  Short the URL 

http://localhost:8080/linkshortening/fullurl/


2. Retrieve the Long URL

http://localhost:8080/linkshortening/shorturl/


