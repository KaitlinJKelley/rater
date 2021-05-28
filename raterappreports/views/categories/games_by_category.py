from raterappreports.views import Connection
import sqlite3
from django.shortcuts import render

def games_by_category(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(""" 
            Select 
                c.id as cat_id,
                c.label,
                g.id as game_id,
                g.title
            From raterapp_category c
            Join raterapp_categorygame cg On cg.category_id = c.id
            Join raterapp_game g On g.id = cg.game_id
            """)

            dataset = db_cursor.fetchall()

            category_games = {}

            for row in dataset:
                cat_id = row["cat_id"]

                game = {
                    "id": row["game_id"],
                    "title": row["title"]
                }
                if cat_id in category_games:
                    category_games[cat_id]["games"].append(game)
                else:
                    category_games[cat_id] = {
                        "id": row["cat_id"],
                        "label": row["label"],
                        "games": [game]
                    }
            return category_games.values()

            # template = "games_by_category.html"

            # context = {
            #     "category_games_list": category_games_list
            # }

            # return render(request, template, context)
            