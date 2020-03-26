import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Navbar from "./navbar/Navbar";
import Dashboard from "./services/Dashboard";
import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {

  render() {
    return (
      <Provider store={store}>

        <Fragment>
            <Dashboard/>
        </Fragment>
        
      </Provider>
    );
  }
};
ReactDOM.render(<App />, document.getElementById("root"));
