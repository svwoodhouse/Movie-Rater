from app import app, db
from flask import request, jsonify
from models import Movie, Critic, User

#Gets all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    result = [movie.to_json() for movie in movies]
    return jsonify(result), 200

#Get all critics
@app.route("/api/critics", methods=["GET"])
def get_critics():
    critics = Critic.query.all()
    result = [critic.to_json() for critic in critics]
    return jsonify(result), 200

#Gets all people
@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = [user.to_json() for user in users]
    return jsonify(result), 200

# Add a new movie
@app.route("/api/movies", methods=["POST"])
def create_movie():
    try:
        data = request.json

        title = data.get("title")
        description = data.get("description")
        image_url = data.get("imageUrl")

        new_movie = Movie(title=title, description=description, image_url=image_url)
        db.session.add(new_movie)
        db.session.commit()

        return jsonify({"msg": "New Movie Added"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
# Add a new critic
@app.route("/api/critics", methods=["POST"])
def create_critic():
    try:
        data = request.json

        first_name = data.get("firstName")
        last_name = data.get("lastName")

        new_critic = Critic(first_name=first_name, last_name=last_name)
        db.session.add(new_critic)
        db.session.commit()

        return jsonify({"msg": "New Critic Added"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Add a new user
@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.json

        first_name = data.get("firstName")
        last_name = data.get("lastName")

        new_user = User(first_name=first_name, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "New User Added"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500