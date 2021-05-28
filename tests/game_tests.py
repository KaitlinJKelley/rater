import json
from typing import Counter
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

        self.cat1 = Category()
        self.cat1.label = "Card Game"
        self.cat1.save()
        self.cat2 = Category()
        self.cat2.label = "Fun"
        self.cat2.save()

        self.game = Game()
        self.game.title = "Monopoly"
        self.game.description = "Win all the money"
        self.game.designer = "Monopoly, Inc."
        self.game.release_year = 1873
        self.game.num_of_players = "2 or more"
        self.game.time_to_play = 80
        self.game.min_age = 12
        self.game.owner_id = 1
        self.game.save()
        self.game.categories.set([1, 2])

        self.data = {
            "title": "Uno",
            "description": "A card game",
            "designer": "Uno, Inc.",
            "releaseYear": 2001,
            "numberOfPlayers": "2 or more",
            "timeToPlay": 20,
            "minAge": 6,
            "categories": [1],
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

    def test_game_category_set(self):
        game = self.game
        game.categories.set([self.cat1, self.cat2])

        self.assertEqual(game.categories.count(), 2)

    def test_get_all_games(self):
        game = Game()
        game.title = "Yahtzee"
        game.description = "Roll the dice"
        game.designer = "Yahtzee, Inc."
        game.release_year = 1984
        game.num_of_players = "2 or more?"
        game.time_to_play = 7
        game.min_age = 90
        game.owner_id = 1
        game.save()
        game.categories.set([2])

        response = self.client.get("/games")
        # print(response.content)
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_response), 2)


    def test_get_game(self):
        # Create a review for game and verify added to response game 
        response = self.client.get(f"/games/{self.game.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["title"], self.game.title)
        self.assertEqual(json_response["description"], self.game.description)
        self.assertEqual(json_response["designer"], self.game.designer)
        self.assertEqual(json_response["release_year"], self.game.release_year)
        self.assertEqual(json_response["num_of_players"], self.game.num_of_players)
        self.assertEqual(json_response["time_to_play"], self.game.time_to_play)
        self.assertEqual(json_response["min_age"], self.game.min_age)
    
    def test_update_game(self):
        response = self.client.put(f"/games/{self.game.id}", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/games/{self.game.id}")
        json_response = json.loads(response.content)

        self.assertEqual(json_response["title"], self.data["title"])
        self.assertEqual(json_response["description"], self.data["description"])
        self.assertEqual(json_response["designer"], self.data["designer"])
        self.assertEqual(json_response["release_year"], self.data["releaseYear"])
        self.assertEqual(json_response["num_of_players"], self.data["numberOfPlayers"])
        self.assertEqual(json_response["time_to_play"], self.data["timeToPlay"])
        self.assertEqual(json_response["min_age"], self.data["minAge"])