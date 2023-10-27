"""This stores the commands that utilise the feedparse library to execute the parsing 
of the RSS feed into a usable Python object.
Jobs to be added to this file with django-apscheduler

Code to be refactored and be used for multiple feeds
"""

# import the base class from which all management commands derive
from typing import Any
from django.core.management.base import BaseCommand


import feedparser
from dateutil import parser


from podcasts.models import Episode

def save_new_episodes(feed):
    """Saves new episodes to the database.
    Checks episode GUID against the episodes in the database.
    If not found, then a new episode is added to the database.
    
    Args:
        feed: requires a feedparser object
    """
    
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


def fetch_realpython_episodes():
    """fetches new episodes from RSS for The Real Python Podcast"""
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(_feed)


def fetch_talkpython_episodes():
    """fetches new episodes from RSS for the Talk Python to Me Podcast"""
    _feed = feedparser.parse("https://talkpython.fm/episodes/rss")
    save_new_episodes(_feed)


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        fetch_realpython_episodes()
        fetch_talkpython_episodes()
