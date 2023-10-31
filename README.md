# PYTHON CONTENT AGGREGATOR APP

## This project aggregates your favorite Python podcasts in one website
### With the ever-increasing number of podcasts online, an aggregator provides value by saving you time scouring the internet for your favourite podcasts. This project entails building a podcast aggregator with Python using the Django framework

#### Step 1: Environment setup and installation of dependencies
#####        Django, feedparser, django-apscheduler

#### Step 2: Building Podcast Model and migrating it to the database
#####       	Built-in testing framework used for unit tests

#### Step 3: Creating Home Page View
#####    	Set up templates(html) and static files (css and images)
#####       Run unit tests to ensure the correct content is displayed

#### Step 4: Parsing Podcast RSS Feeds
#####       feedparser.parse() fetches and automatically parses the feed into a usable Python object
#####       All podcasts have RSS feeds.

#### Step 5: Creating a Django Custom Command
#####       The goal is to exexute scripts within the project to interact with it while the Django or production server is also running.
#####       Utilises manage.py command utility
#####       Create appropriate directories and a file for command storage


#### Step 6: Adding more feeds to the content aggregator
#####       Refactoring the pasrsing code for more general use.
#####       Adding functions for each individual podcast.

#### Step 7: Scheduling tasks with django-apscheduler
#####       Django implementation of the APScheduler library
#####       Schedule fetching
#####       Schedule deletion of old jobs weekly
#####       Include an interval trigger for both

#### Step 8: Sit back, Relax and Enjoy your Implementation
#### Learnt:
#####       Parsing RSS feeds into Python objects using Feedparser library
#####       Execution of custom commands in Django
#####       Apscheduler in Django to automate custom commands
#####       Inclusion of unit tests in Django
#####       Viewing admin side of platform in execution
#####       View custom job execution and storage
