// UserInstruments.js

import React from 'react';
import { Link } from 'react-router-dom';

const UserInstruments = () => (
  <div>
    {/* Display list of user's instruments */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default UserInstruments;
