import React from 'react';
import { Link } from 'react-router-dom';

class Navbar extends React.Component {
    render() {
      return (
          <nav className="navbar">
              <h1>NotenOptimierer®</h1>
              <div className="links">
                <Link to="/">Home</Link>
                <Link to="/informatik">Informatik</Link>
              </div>
          </nav>
      );
    }
}

export default Navbar;