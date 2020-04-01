import React, { Component } from "react";
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";

import PropTypes from "prop-types";
import { login } from "../../actions/auth";

export class Login extends Component {
  state = {
    login: "",
    password: ""
  };


  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onSubmit = e => {
    e.preventDefault();
    this.props.login(this.state.login, this.state.password);
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }
    const { login, password } = this.state;
    return (
      <form onSubmit={this.onSubmit}>
          <label>Login</label>
          <input
            type="text"
            className="form-control"
            name="login"
            onChange={this.onChange}
            value={login}
          />

          <label>Password</label>
          <input
            type="password"
            className="form-control"
            name="password"
            onChange={this.onChange}
            value={password}
          />

          <button type="submit" className="btn btn-primary">
            Login
          </button>

      </form>
    );
  }

}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default connect(
  mapStateToProps,
  { login }
)(Login);
