import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import Informatik from './Informatik';
import OurNavbar from './OurNavbar';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component {
    render() {
      return (
          <Router>
            <div className="App container">
                <OurNavbar/>
                <div className="content">
                    <Switch>
                        <Route exact path="/">
                            <Home/>
                        </Route>
                        <Route path="/informatik">
                            <Informatik/>
                        </Route>
                    </Switch>
                </div>
            </div>
          </Router>
      );
    }
}

export default App;