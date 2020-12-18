from flask import Flask, jsonify
import requests

# INSTRUCTION
# If you want to use Methods = DELETE, or POST the instruction is below
# DELETE copy to terminal : curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/movies/0  <---- The number represents id number of the movie you want to DELETE
# POST: curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/movies <---- ADD a new movie to library
# PUT: curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/movies/0 <---- The number represents id number of the movie you want to PUT new "description"


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


@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie_by_movie_id(movie_id):
    return jsonify({"Movie Id": movie_library[movie_id]})


@app.route("/movies", methods=["POST"])
def add_new_movie_to_library():
    movie = {
        'title': 'The Holiday',
        'movie_id': '3',
        'genres': "romance, comedy"
    },

    movie_library.append(movie)
    return jsonify({"Created": movie})


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
# INSTRUCTION
# If you want to use Methods = DELETE, or POST the instruction is below
# DELETE copy to terminal : curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/movies/0  <---- The number represents id number of the movie you want to DELETE
# POST: curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/movies <---- ADD a new movie to library
# PUT: curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/movies/0 <---- The number represents id number of the movie you want to PUT new "description"
