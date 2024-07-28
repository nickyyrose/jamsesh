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

    # Relationships
    instruments = db.relationship('UserInstrument', back_populates='user', cascade='all, delete-orphan')
    genres = db.relationship('UserGenre', back_populates='user', cascade='all, delete-orphan')
    pictures = db.relationship('Picture', back_populates='user', cascade='all, delete-orphan')
    songs = db.relationship('Song', back_populates='user', cascade='all, delete-orphan')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', back_populates='sender', cascade='all, delete-orphan')
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', back_populates='receiver', cascade='all, delete-orphan')
    friends_friender = db.relationship('Friend', foreign_keys='Friend.friender', back_populates='friender_user', cascade='all, delete-orphan')
    friends_friended = db.relationship('Friend', foreign_keys='Friend.friended', back_populates='friended_user', cascade='all, delete-orphan')

    # Validations
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
    
    # Hybrid Property for Password Hash
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self,password):
        self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    # Authentication Method
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    # Representation Method
    def __repr__(self):
        return f'<User {self.name}>'

#######################################################################

class Instrument(db.Model, SerializerMixin):
    __tablename__ = "instruments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationships
    users = db.relationship('UserInstrument', back_populates='instrument', cascade='all, delete-orphan')

    # Validations
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

    # Relationships
    users = db.relationship('UserGenre', back_populates='genre', cascade='all, delete-orphan')

    # Validations
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

    # Relationships
    user = db.relationship('User', back_populates='instruments')
    instrument = db.relationship('Instrument', back_populates='users')

#######################################################################

class UserGenre(db.Model, SerializerMixin):
    __tablename__ = "user_genres"

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='genres')
    genre = db.relationship('Genre', back_populates='users')

#######################################################################

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    song_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='songs')

    # Validations
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

    # Relationships
    user = db.relationship('User', back_populates='pictures')

#######################################################################

class Friend(db.Model, SerializerMixin):
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True)
    friender = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friended = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    friender_user = db.relationship('User', foreign_keys=[friender], back_populates='friends_friender')
    friended_user = db.relationship('User', foreign_keys=[friended], back_populates='friends_friended')

#######################################################################

class Message(db.Model, SerializerMixin):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String)

    # Relationships
    sender = db.relationship('User', back_populates='sent_messages', foreign_keys=[sender_id])
    receiver = db.relationship('User', back_populates='received_messages', foreign_keys=[receiver_id])

#######################################################################
