from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    #######add relationships for User########

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('must have name')
        return name 
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self,password):
        self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._paswword_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'<User {self.name}>'
    
#######################################################################

class Instrument(db.Model, SerializerMixin):
    __tablename__ = "instruments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


#####add relationship for Instrument#########
#####add validations for Instrument##########

#######################################################################

class Genre(db.Model, SerializerMixin):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


#####add relationship for Genre#########
#####add validations for Genre##########

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
#####add validations

#######################################################################

class Picture(db.Model, SerializerMixin):
    __tablename__ = "pictures"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
#####add validations

#######################################################################

class Friend(db.Model, SerializerMixin):
    __tablename__ = "friends"

    id = db.Column(id.Integer, primary_key=True)
    friender = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friended = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


#####add relationship
#####add validations

#######################################################################

class Message(db.Model, SerializerMixin):
    __tablename__ = "Messages"

    id = db.Column(id.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message =db.Column(db.String)


#####add relationship
#####add validations

#######################################################################
