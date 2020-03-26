import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Navbar extends Component {
  render() {
    return (
      <ul>
        <li>Coming events</li>
        <li>Travel Locations</li>
        <li>Weather</li>
        <li>Style</li>
      </ul>
    );
  }
}

export default Navbar;
