from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt, db
import re

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    #######add relationships for User########
    instruments = db.relationship('UserInstrument', backref='user', cascade='all, delete-orphan')
    genres = db.relationship('UserGenre', backref='user', cascade='all, delete-orphan')
    pictures = db.relationship('Picture', backref='user', cascade='all, delete-orphan')
    songs = db.relationship('Song', backref='user', cascade='all, delete-orphan')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', cascade='all, delete-orphan')
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', cascade='all, delete-orphan')
    friends = db.relationship('Friend', foreign_keys='Friend.friender', backref='friender_user', cascade='all, delete-orphan')
    friended = db.relationship('Friend', foreign_keys='Friend.friended', backref='friended_user', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('must have name')
        return name 
    
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self,password):
        self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'<User {self.name}>'
    
    #######################################################################

class Instrument(db.Model, SerializerMixin):
    __tablename__ = "instruments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


#####add relationship for Instrument#########
    users = db.relationship('UserInstrument', backref='instrument', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('must have name')
        return name 


#######################################################################

class Genre(db.Model, SerializerMixin):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


#####add relationship for Genre#########
    users = db.relationship('UserGenre', backref='genre', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('must have name')
        return name

#######################################################################

class UserInstrument(db.Model, SerializerMixin):
    __tablename__ = "user_instruments"

    id = db.Column(db.Integer, primary_key=True)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instruments.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
#####add validations

#######################################################################

class UserGenre(db.Model, SerializerMixin):
    __tablename__ = "user_genres"

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

#####add relationship
#####add validations

#######################################################################

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    song_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
    user = db.relationship('User', backref=db.backref('songs', cascade='all, delete-orphan'))

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('must have name')
        return name

#######################################################################

class Picture(db.Model, SerializerMixin):
    __tablename__ = "pictures"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
    user = db.relationship('User', backref=db.backref('pictures', cascade='all, delete-orphan'))

#####add validations

#######################################################################

class Friend(db.Model, SerializerMixin):
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True)
    friender = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friended = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
    friender_user = db.relationship('User', foreign_keys=[friender], backref=db.backref('friends_friender', cascade='all, delete-orphan'))
    friended_user = db.relationship('User', foreign_keys=[friended], backref=db.backref('friends_friended', cascade='all, delete-orphan'))

#####add validations

#######################################################################

class Message(db.Model, SerializerMixin):
    __tablename__ = "Messages"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message =db.Column(db.String)


#####add relationship
    sender = db.relationship('User', foreign_keys=[sender_id], backref=db.backref('sent_messages', cascade='all, delete-orphan'))
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref=db.backref('received_messages', cascade='all, delete-orphan'))

#####add validations

#######################################################################
