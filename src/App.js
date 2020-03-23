import React from 'react';

import './App.css';

import Home from './components/home/Home';
import Newstape from './components/news-tape/Newstape';
import Navbar from './components/navbar/Navbar';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
    return (
      <Router>
        <div className="App">
          <Navbar/>
          <Switch>
            <Route path="/" exact component={ Home }/>
            <Route path="/newsletter" component={ Newstape }/>
            <p> Learn React </p>
          </Switch>
        </div>
      </Router>

    );
}

export default App;
