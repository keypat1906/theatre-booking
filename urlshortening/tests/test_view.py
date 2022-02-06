import json

from django.conf import settings
from django.test import TestCase, override_settings

from urlshortening.models import Url


@override_settings(
    ROOT_URLCONF='urlshortening.urls',
    SHORT_URL_PATH='http://tinyurl.com/short-prefix/',
    REDIRECT_PREFIX='r'
)
class ViewTestCase(TestCase):
    fixtures = ['urlshortening-test-data']

    def test_get_full_link(self):
        short_id = "000001"
        should_response = {"error": "", "data": {"full_url": "http://tinyurl.com/to-000001"}}

        response = self.client.get('/expand/{}/'.format(short_id))
        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["data"], should_response["data"])
        self.assertEqual(response_data["error"], should_response["error"])

    def test_get_full_link_expired(self):
        short_id = "000002"
        should_response = {"data": "", "error": "Link is expired"}

        response = self.client.get('/expand/{}/'.format(short_id))
        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["data"], should_response["data"])
        self.assertEqual(response_data["error"], should_response["error"])

    def test_get_full_link_not_found(self):
        short_id = "000003"
        should_response = {"data": "", "error": "Url doesn\'t exist"}

        response = self.client.get('/expand/{}/'.format(short_id))
        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["data"], should_response["data"])
        self.assertEqual(response_data["error"], should_response["error"])


