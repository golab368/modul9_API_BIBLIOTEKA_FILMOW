from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


movie_library = [
    {
        'title': 'Matrix',
        'movie_id': '0',
        'genres': "action"
    },
    {
        'title': 'Godfather',
        'movie_id': '1',
        'genres': "drama"
    },
    {
        'title': 'Rambo',
        'movie_id': '2',
        'genres': "action"
    },
]


@app.route("/", methods=["GET"])
def index():
    return "Hello in my movies library"


@app.route("/movies", methods=["GET"])
def get_movie():
    return jsonify({"Movies": movie_library})


@app.route("/movies/<string:title>", methods=["GET"])
def get_movie_by_movie_title(title):
    for movie in movie_library:
        if title == movie["title"]:
            return jsonify({"Movies": movie})
    return "There is not such a movie in my library"


@app.route("/movies", methods=["POST"])
def add_new_movie_to_library():

    movie = {'title': request.json["title"],
             'movie_id': request.json["movie_id"],
             'genres': request.json["genres"], }
    movie_library.append(movie)
    return jsonify({"Created": movie_library})


@app.route("/movies/<int:movie_id>", methods=["PUT"])
def movie_update_add_some_description_to_movie(movie_id):
    movie_library[movie_id]["description"] = "this is my favorite movie"

    return jsonify({"movie_id": movie_library[movie_id]})


@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def movie_delete_by_movie_id(movie_id):

    movie_library.remove(movie_library[movie_id])

    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)
