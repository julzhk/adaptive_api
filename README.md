adaptive_api
============

UI for a REST twitter-like feed

How to install
==============

This is a standard Python / Django project, so should be simple.
But here are some further notes:

- It has some dependencies (requirements.txt), (using pip install -r requirements.txt)
these are best installed in a virtual environment ( pip install virtualenv)
- the project uses a local-settings.py file. Hence a local_settings.py.template file is checked in.
-- You can amend this and rename it to 'local_settings.py' for your local machine.
-- in particular, you'll need to set the path to the sqlite database
- The project uses django-south for database migrations so you can do:
-- python migrate --all
-- or python migrate.py syncdb.
to initialize the database.
- You'll also need to run manage.py collectstatic too:
this moves resources into their correct location

This should be enough to get you up and running. Any problems please contact me.


