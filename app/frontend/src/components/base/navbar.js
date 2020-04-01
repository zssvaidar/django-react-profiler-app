import React, { Component } from 'react';
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { logout } from "../../actions/auth";

class Navbar extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };



  render() {
    const { isAuthenticated, user } = this.props.auth;

    const authLinks = (
      <ul>
        <li className="nav-item">
          <span className="navbar-text mr-3">
            <strong>{user ? `Welcome ${user.login}` : ""}</strong>
          </span>
          <button
            onClick={this.props.logout}
            className="nav-link btn btn-info btn-sm text-light"
          >
            Logout
          </button>
        </li>
      </ul>
    );
    const guestLinks = (
      <ul>
        <li>
          <Link to="/login">Login</Link>
        </li>
        <li>
          <Link to="/register">Register</Link>
        </li>
      </ul>
    );

    return (
      <nav>
        {isAuthenticated ? authLinks : guestLinks}
      </nav>
    );
  }
}


const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { logout }
)(Navbar);
