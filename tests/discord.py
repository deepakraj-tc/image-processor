import unittest
from io import BytesIO

import requests

from PIL import Image


class BannerTest(unittest.TestCase):

    URL = "http://127.0.0.1:5000/discord/banners/welcome/"

    A_BANNER_URL = "https://i.imgur.com/6aieR4Y.gif"
    BANNER_URL = "https://i.imgur.com/I8fNRV8.jpg"
    AVATAR_URL = "https://i.imgur.com/zsfY16f.jpg"

    NAME = "The Cosmos#9806"
    TEXT = "Welcome to B-20! Enjoy your stay!"

    def test_welcome_banner(self):
        _bytes = requests.post(self.URL, json={
            "banner_url": self.A_BANNER_URL,
            "avatar_url": self.AVATAR_URL,
            "name": self.NAME,
            "text": self.TEXT,
        }).content
        with open("results/test.gif", "wb") as file:
            file.write(_bytes)
        self.assertIsInstance(_bytes, bytes)
