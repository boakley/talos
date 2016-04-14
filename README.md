Welcome to Talos!
=================

Talos is a re-implementation of the [robot framework
hub](https://github.com/boakley/robotframework-hub) using django
(note: the original hub uses flask).

Talos is very much a work in progress. Don't expect anything to work
(though you might get lucky!)

Getting Started
---------------

Talos provides a RESTFUL api to a repository of robot framework keywords. 
To test this out you'll need a repository of tests and resource files (library
files are temporarily unsupported). You'll pass the name of a folder to a 
special django admin command which will find all keywords in resource files 
and test suites within that folder and all child folders. 

If you've used django before this will be very familiar. Clone this repository, cd to the repository, then run the following commands:

    $ python manage.py migrate
    $ python manage.py addproject /path/to/folder/with/resource/files
    $ python manage.py runserver
 
Then, open a browser to http://localhost:8000/api/
