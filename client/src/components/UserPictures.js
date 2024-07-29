// UserPictures.js

import React from 'react';
import { Link } from 'react-router-dom';

const UserPictures = () => (
  <div>
    {/* Display 4 pictures */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default UserPictures;
