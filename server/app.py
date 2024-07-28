#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Api, Resource
from sqlalchemy.orm.exc import NoResultFound

# Local imports
from config import app, db, api
from models import User, Instrument, Genre, Song, Picture, Friend, Message

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)

    def post(self):
        req_json = request.get_json()
        try:
            new_user = User(
                name=req_json["name"],
                email=req_json["email"],
                password_hash=req_json["password"]
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except ValueError as e:
            return make_response({'error': str(e)}, 400)


class Users_by_id(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).one()
            return make_response(user.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'User not found'}, 404)

    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).one()
            db.session.delete(user)
            db.session.commit()
            return make_response({'message': 'User deleted'}, 204)
        except NoResultFound:
            return make_response({'error': 'User not found'}, 404)

    def patch(self, id):
        try:
            user = User.query.filter_by(id=id).one()
            req_json = request.get_json()
            for key, value in req_json.items():
                setattr(user, key, value)
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'User not found'}, 404)


class Instruments(Resource):
    def get(self):
        instruments = [instrument.to_dict() for instrument in Instrument.query.all()]
        return make_response(instruments, 200)

    def post(self):
        req_json = request.get_json()
        try:
            new_instrument = Instrument(
                name=req_json["name"]
            )
            db.session.add(new_instrument)
            db.session.commit()
            return make_response(new_instrument.to_dict(), 201)
        except ValueError as e:
            return make_response({'error': str(e)}, 400)


class Instruments_by_id(Resource):
    def get(self, id):
        try:
            instrument = Instrument.query.filter_by(id=id).one()
            return make_response(instrument.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Instrument not found'}, 404)

    def delete(self, id):
        try:
            instrument = Instrument.query.filter_by(id=id).one()
            db.session.delete(instrument)
            db.session.commit()
            return make_response({'message': 'Instrument deleted'}, 204)
        except NoResultFound:
            return make_response({'error': 'Instrument not found'}, 404)

    def patch(self, id):
        try:
            instrument = Instrument.query.filter_by(id=id).one()
            req_json = request.get_json()
            for key, value in req_json.items():
                setattr(instrument, key, value)
            db.session.add(instrument)
            db.session.commit()
            return make_response(instrument.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Instrument not found'}, 404)


class Genres(Resource):
    def get(self):
        genres = [genre.to_dict() for genre in Genre.query.all()]
        return make_response(genres, 200)

    def post(self):
        req_json = request.get_json()
        try:
            new_genre = Genre(
                name=req_json["name"]
            )
            db.session.add(new_genre)
            db.session.commit()
            return make_response(new_genre.to_dict(), 201)
        except ValueError as e:
            return make_response({'error': str(e)}, 400)


class Genres_by_id(Resource):
    def get(self, id):
        try:
            genre = Genre.query.filter_by(id=id).one()
            return make_response(genre.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Genre not found'}, 404)

    def delete(self, id):
        try:
            genre = Genre.query.filter_by(id=id).one()
            db.session.delete(genre)
            db.session.commit()
            return make_response({'message': 'Genre deleted'}, 204)
        except NoResultFound:
            return make_response({'error': 'Genre not found'}, 404)

    def patch(self, id):
        try:
            genre = Genre.query.filter_by(id=id).one()
            req_json = request.get_json()
            for key, value in req_json.items():
                setattr(genre, key, value)
            db.session.add(genre)
            db.session.commit()
            return make_response(genre.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Genre not found'}, 404)


class Songs(Resource):
    def get(self):
        songs = [song.to_dict() for song in Song.query.all()]
        return make_response(songs, 200)

    def post(self):
        req_json = request.get_json()
        try:
            new_song = Song(
                song_url=req_json["song_url"],
                name=req_json.get("name"),
                genre=req_json.get("genre"),
                user_id=req_json["user_id"]
            )
            db.session.add(new_song)
            db.session.commit()
            return make_response(new_song.to_dict(), 201)
        except ValueError as e:
            return make_response({'error': str(e)}, 400)


class Songs_by_id(Resource):
    def get(self, id):
        try:
            song = Song.query.filter_by(id=id).one()
            return make_response(song.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Song not found'}, 404)

    def delete(self, id):
        try:
            song = Song.query.filter_by(id=id).one()
            db.session.delete(song)
            db.session.commit()
            return make_response({'message': 'Song deleted'}, 204)
        except NoResultFound:
            return make_response({'error': 'Song not found'}, 404)

    def patch(self, id):
        try:
            song = Song.query.filter_by(id=id).one()
            req_json = request.get_json()
            for key, value in req_json.items():
                setattr(song, key, value)
            db.session.add(song)
            db.session.commit()
            return make_response(song.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Song not found'}, 404)


class Pictures(Resource):
    def get(self):
        pictures = [picture.to_dict() for picture in Picture.query.all()]
        return make_response(pictures, 200)

    def post(self):
        req_json = request.get_json()
        try:
            new_picture = Picture(
                caption=req_json.get("caption"),
                user_id=req_json["user_id"]
            )
            db.session.add(new_picture)
            db.session.commit()
            return make_response(new_picture.to_dict(), 201)
        except ValueError as e:
            return make_response({'error': str(e)}, 400)


class Pictures_by_id(Resource):
    def get(self, id):
        try:
            picture = Picture.query.filter_by(id=id).one()
            return make_response(picture.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Picture not found'}, 404)

    def delete(self, id):
        try:
            picture = Picture.query.filter_by(id=id).one()
            db.session.delete(picture)
            db.session.commit()
            return make_response({'message': 'Picture deleted'}, 204)
        except NoResultFound:
            return make_response({'error': 'Picture not found'}, 404)

    def patch(self, id):
        try:
            picture = Picture.query.filter_by(id=id).one()
            req_json = request.get_json()
            for key, value in req_json.items():
                setattr(picture, key, value)
            db.session.add(picture)
            db.session.commit()
            return make_response(picture.to_dict(), 200)
        except NoResultFound:
            return make_response({'error': 'Picture not found'}, 404)


# Adding resources to API
api.add_resource(Users, '/users')
api.add_resource(Users_by_id, '/users/<int:id>')
api.add_resource(Instruments, '/instruments')
api.add_resource(Instruments_by_id, '/instruments/<int:id>')
api.add_resource(Genres, '/genres')
api.add_resource(Genres_by_id, '/genres/<int:id>')
api.add_resource(Songs, '/songs')
api.add_resource(Songs_by_id, '/songs/<int:id>')
api.add_resource(Pictures, '/pictures')
api.add_resource(Pictures_by_id, '/pictures/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
