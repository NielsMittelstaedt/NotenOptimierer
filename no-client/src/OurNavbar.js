import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import './OurNavbar.css';

class OurNavbar extends React.Component {
    render() {
      return (
          <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="/" id="navbar-title">NotenOptimiere®</Navbar.Brand>
            <Nav className="mr-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="/Informatik">Informatik</Nav.Link>
              <Nav.Link href="/Mathematik">Mathematik</Nav.Link>
            </Nav>
          </Navbar>
      );
    }
}

/*

<nav className="navbar">
              <h1>NotenOptimierer®</h1>
              <div className="links">
                <Link to="/">Home</Link>
                <Link to="/informatik">Informatik</Link>
              </div>
          </nav>
*/

export default OurNavbar;