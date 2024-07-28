import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Home from './Home';
import SignUp from './SignUp';
import Login from './Login';


const App = () => (
  <Router>
    <div>
      <h1>JamSesh</h1>
      <nav>
        <ul>
          <li><Link to="/signup">Sign Up</Link></li>
          <li><Link to="/login">Login</Link></li>
        </ul>
      </nav>
      <Switch>
        <Route path="/signup" component={SignUp} />
        <Route path="/login" component={Login} />
        <Route path="/" component={Home} />
      </Switch>
    </div>
  </Router>
);

export default App;