frisbillanas
============

Frisbillanas Website


Installing
----------

Clone project:

    $ git clone https://github.com/msaelices/frisbillanas.git

Create a virtualenv::

    $ cd frisbillanas
    $ virtualenv --no-site-packages --python=python2.7 venv
    $ source venv/bin/activate

Install dependencies::

    $ cd frisbillanas
    $ pip install -r requirements.txt

Init BD::

    $ python manage.py syncdb  --noinput --migrate
    $ python manage.py createsuperuser
    $ python manage.py collectstatic

Run webserver::

    $ python manage.py runserver
