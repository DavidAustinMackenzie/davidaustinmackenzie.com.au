Switch to 'user' account on Freebsd image

su user

#enable virtual environment

source venv/bin/activate

#Run gunicorn server for web site

gunicorn --bind 0.0.0.0:8000 wsgi:app &

The following commands need to be run as su

#switch to root user

su

#Restart nginx service

service nginx restart

#Check nginx service

service nginx status

#Test nginx configuration

nginx -t
