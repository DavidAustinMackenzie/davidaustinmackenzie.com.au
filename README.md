#enable virtual environment
source venv/bin/activate

#Run gunicorn server for web site
gunicorn --bind 0.0.0.0:8000 wsgi:app &
