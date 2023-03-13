rm db.sqlite3
rm -rf ./craftyCrittersapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations craftyCrittersapi
python3 manage.py migrate 
python3 manage.py loaddata yarns
python3 manage.py loaddata photos
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata critters
python3 manage.py loaddata projects
python3 manage.py loaddata comments
python3 manage.py loaddata yarns_for_projects