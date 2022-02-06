# url-shortning

Install virtualenv

pip install virtualenv
On the project directory,

Create virtual environment

virtualenv venv
Activate

source venv/bin/activate
Install requirements including dependencies

pip install -r requirements.txt
Do Database migrations

./manage.py makemigrations
./manage.py makemigrations chat
./manage.py migrate
Try creating a superuser for user management

./manage.py createsuperuser
Give necessary inputs

Run development server

./manage.py runserver 0.0.0.0:8000

APIs

Get all the recent messages
GET /api/recent-messages ( Get all the recent messages in last 30 days. Max 100 records)
GET /api/recent-messages?page_size=1 (If more than 100 record, use page_size)
Get all the messages for sender and receiver
GET /api/messages/1/2 ( Get all the messages for reciever id 1 from sender id 2)
GET /api/messages/1/2?page_size=1 (If more than 100 record, use page_size)


