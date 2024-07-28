// Messages.js

import React from 'react';
import { Link } from 'react-router-dom';

const Messages = () => (
  <div>
    {/* Display message threads */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default Messages;
