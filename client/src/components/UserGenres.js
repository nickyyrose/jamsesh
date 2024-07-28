// UserGenres.js

import React from 'react';
import { Link } from 'react-router-dom';

const UserGenres = () => (
  <div>
    {/* Display list of user's genres */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default UserGenres;
