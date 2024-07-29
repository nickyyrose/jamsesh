// UserGenres.js

import React from 'react';
import { Link } from 'react-router-dom';

const UserGenres = () => (
  <div>
    {/* Display user genres */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default UserGenres;
