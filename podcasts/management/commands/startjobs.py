"""This stores the commands that utilise the feedparse library to execute the parsing 
of the RSS feed into a usable Python object.
Jobs to be added to this file with django-apscheduler

Code to be refactored and be used for multiple feeds
"""

# import the base class from which all management commands derive
from django.core.management.base import BaseCommand


import feedparser
from dateutil import parser


from podcasts.models import Episode
class Command(BaseCommand):
    def handle(self, *args, **options):
        feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image["href"]

        for item in feed.entries:
            if not Episode.objects.filter(guid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    image=podcast_image,
                    podcast_name=podcast_title,
                    guid=item.guid,
                )
                episode.save()
