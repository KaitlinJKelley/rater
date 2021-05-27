import json
from raterapp.models.category import Category
from raterapp.models import Game
from rest_framework import status
from rest_framework.test import APITestCase

class GameTests(APITestCase):
    def setUp(self):
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)

        self.token = json_response["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        cat1 = Category()
        cat1.label = "Card Game"
        cat1.save()
        cat1 = Category()
        cat1.label = "Fun"
        cat1.save()

        self.data = {
            "title": "Uno",
            "description": "A card game",
            "designer": "Uno, Inc.",
            "releaseYear": 2001,
            "numberOfPlayers": "2 or more",
            "timeToPlay": 20,
            "minAge": 6,
            "categories": [1, 2],
            "owner": 1
        }

    def test_create_game(self):
        response = self.client.post("/games", self.data, format="json")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["title"], self.data["title"])
        self.assertEqual(json_response["description"], self.data["description"])
        self.assertEqual(json_response["designer"], self.data["designer"])
        self.assertEqual(json_response["release_year"], self.data["releaseYear"])
        self.assertEqual(json_response["num_of_players"], self.data["numberOfPlayers"])
        self.assertEqual(json_response["time_to_play"], self.data["timeToPlay"])
        self.assertEqual(json_response["min_age"], self.data["minAge"])