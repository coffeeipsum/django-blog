# Walk Through Project "Blog"
[![Build Status](https://travis-ci.org/coffeeipsum/django-blog.svg?branch=master)](https://travis-ci.org/coffeeipsum/django-blog)


# First
wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh

Hi coffeeipsum, welcome to your Code Institute Python workspace in c9, remember to use the mkvirtualenv and workon commands for your projects

# Create a new virtual environment (called foo)
mkvirtualenv foo

# Install Djano
sudo pip3 install django==1.11

# Add requirements.txt
pip freeze > requirements.txt

# Start a new project called Blog
django-admin startproject blog .
(don't forget the 'dot', this will add the project in the root directory)


# Make manage.py executable by changing to mode to:
chmod +x manage.py

# Lastly, migrate it!
./manage.py migrate

# Run the server
./manage.py runserver $IP:$PORT

# add ALLOWED_HOSTS
copy the url of your project,
go to blog > settings.py and add the url to ALLOWED_HOSTS = [ ]


# Create a .gitignore
echo -e "*.sqlite3\n*.pyc\n.~c9\n__pycache__/" > .gitignore

# Travis
https://travis-ci.org/
sync w/ Github Account

[![Build Status](https://travis-ci.org/coffeeipsum/django-blog.svg?branch=master)](https://travis-ci.org/coffeeipsum/django-blog)

create a ` .travis.yml ` file