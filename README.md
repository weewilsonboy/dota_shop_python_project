# Dota2 Shop and Courier journey replication project


## Steps to run this project
- Make sure PostgreSQL is installed on your system
- Clone this repo into the desired folder on your system
- Change `postgresql://wilson:password@localhost:5432/dota_db` in app.py to reflect your postgresql access details
- use `flask seed` to seed the database with heroes, items, and the initial courier journey.
- use `flask run` to start the project running on your system
