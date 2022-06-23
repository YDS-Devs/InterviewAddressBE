python manage.py makemigrations && ^
python manage.py migrate && ^
python manage.py loaddata countries.json && ^
python manage.py loaddata states.json && ^
python manage.py loaddata areas.json && ^
python manage.py runserver