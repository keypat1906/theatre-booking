# theatre booking

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


API Endpoints


1. List all the theaters that are owned by the company

GET http://localhost:8080/theatre/theatre
GET http://localhost:8080/theatre/theatre/{theatre_id}/


2. Display the schedule for a given day for a theatre of user's choice

GET http://localhost:8080/theatre/slot/?theatre_id=2


3. Allow the performer to choose a theater and get the best available show slot. For example, in a given theater X I should be able to 
select the best possible slot for a given date.

GET http://localhost:8080/theatre/theatre/2/available_slots?day=2022-02-01

4. Allow the performer to get a slot in any of the theatres for a given time slot. For example, I should be able to look for a Sunday 6 to 7 
p.m slot in any of the available theaters

GET http://localhost:8080/theatre/slotlist?start_time=14-00-00&end_time=17-00-00&slot_date=2022-02-1


5. Allow the performer to choose both the time and venue. For example, reserve a 3.15 to 4.45 p.m slot on 4th Feb in Theatre Y

POST http://localhost:8080/theatre/slot/
payload {"slot_date":  "2022-02-28", "start_time”:”11:00:00”,”end_time":"16:00:00”, "theatre": 4 }

User can only choose slot from 8 AM to 8 PM, otherwise 400 Bad request ["showtime should be between 8 AM and 8 PM"]


