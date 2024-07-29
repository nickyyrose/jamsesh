// Friends.js

import React from 'react';
import { Link } from 'react-router-dom';

const Friends = () => (
  <div>
    {/* Display friends */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default Friends;
