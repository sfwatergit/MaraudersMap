#!/usr/local/bin/python
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "MaraudersMap.settings"

print "Mischief managed!"

# dump the data to fixtures
os.system('python manage.py dumpdata collector --indent=2 > semantic_mapping/models/fixtures/data.json')
# drop and recreate the db (this is for postgres)
os.system('dropdb maraudersmap')
#authentic is the name of putative custom authentication
os.system('createdb -T geo_template maraudersmap')
# sync the db
os.system('python manage.py syncdb --noinput')

# create a super user
from django.contrib.auth.models import User
u = User.objects.create(
    username='harry',
    first_name='Sid',
    last_name='Feygin',
    email='sid.feygin@berkeley.edu',
    is_superuser=True,
    is_staff=True,
    is_active=True
)

u.set_password('dissendium')
u.save()

print "Messrs. Moony, Wormtail, Padfoot and Prongs, purveyors " \
      "of aids to magical mischief-makers, are proud to " \
      "present the Marauder's Map."

# load the fixtures back in
os.system('python manage.py loaddata data.json')
# run the server
os.system('python manage.py runserver')

#rf. http://en.wikipedia.org/wiki
# /Magical_objects_in_Harry_Potter#The_Marauder.27s_Map