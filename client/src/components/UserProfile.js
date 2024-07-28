// UserProfile.js

import React from 'react';
import { Link } from 'react-router-dom';
import UserPictures from './UserPictures';
import UserInstruments from './UserInstruments';
import UserGenres from './UserGenres';

const UserProfile = () => (
  <div>
    <h3>User Name</h3>
    <p>User Bio</p>
    <Link to="/pictures">Pictures</Link>
    <Link to="/add-friend">Add Friend</Link>
    <Link to="/messages">Message</Link>
    <Link to="/instruments">Instrument</Link>
    <Link to="/genres">Genre</Link>
  </div>
);

export default UserProfile;
