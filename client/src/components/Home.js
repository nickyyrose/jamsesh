// Home.js

import React from 'react';
import { Link } from 'react-router-dom';
import UserProfile from './UserProfile';
import BrowseUsers from './BrowseUsers';
import Friends from './Friends';
import Messages from './Messages';

const Home = () => (
  <div>
    <h2>Welcome to JamSesh!</h2>
    <Link to="/profile">View Your Profile</Link>
    <Link to="/browse">Browse Users</Link>
    <Link to="/friends">View Friends</Link>
    <Link to="/messages">Messages</Link>
    {/* Display main user picture here */}
    <UserProfile /> {/* This component should display the main user picture */}
  </div>
);

export default Home;
