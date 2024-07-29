// Messages.js

import React from 'react';
import { Link } from 'react-router-dom';

const Messages = () => (
  <div>
    {/* Display messages */}
    <Link to="/profile">Back to Profile</Link>
    <Link to="/">Home</Link>
  </div>
);

export default Messages;
