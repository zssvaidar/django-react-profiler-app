import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch, Redurect }
from "react-router-dom";
import Login from "./accounts/Login"
// import Register from "./accounts/Register"

import Navbar from "./base/navbar";
import Dashboard from "./services/Dashboard";
import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {

  render() {
    return (
      <Provider store={store}>
        <Router>
          <Fragment>
            <Navbar/>

            <Switch>
              <Route exact path="/" component={Dashboard} />
              <Route exact path="/login" component={Login} />
            </Switch>
          </Fragment>
        </Router>
      </Provider>
    );
  }
};
ReactDOM.render(<App />, document.getElementById("root"));
