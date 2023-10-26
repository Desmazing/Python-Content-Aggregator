from django.test import TestCase
from django.utils import timezone
from .models import Episode
from django.urls.base import reverse


class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="My Probably Amazing Podcast Episode",
            description="Mind on millions!",
            pub_date=timezone.now(),
            link="https://probablyamazing.com",
            image="https://image.probablyamazing.com",
            podcast_name="Most Must-See Podcast",
            guid="de194720-7b4c-49e2-a05f-433436d3fetr",
        )
    
    
    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Mind on millions!")
        self.assertEqual(self.episode.link, "https://probablyamazing.com")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-433436d3fetr"
        )


    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "Most Must-See Podcast: My Probably Amazing Podcast Episode"
        )
    

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    

    def teste_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")
    

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "My Probably Amazing Podcast Episode")
