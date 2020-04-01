import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { register } from "../../actions/auth";


export class Register extends Component {
  state = {
    login: "",
    phonenumber: "",
    country: "",
    city: "",
    password: "",
    password2: "",
    user_type: "1"
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };


    onSubmit = e => {
      e.preventDefault();
      const { login, phonenumber, country, city, password, password2, user_type } = this.state;
      if (password !== password2) {
        console.log("didnot match");
        // this.props.createMessage({ passwordNotMatch: "Passwords do not match" });
      } else {
        const newUser = {
          login, password, phonenumber, country, city, user_type
        };
        this.props.register(newUser);
      }
    };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }
    const { login, phonenumber, country, city, password, password2 } = this.state;
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
<br/>

          <label>Phonenumber</label>
          <input
            type="text"
            className="form-control"
            name="phonenumber"
            onChange={this.onChange}
            value={phonenumber}
          />
<br/>
          <label>Country</label>
          <input
            type="text"
            className="form-control"
            name="country"
            onChange={this.onChange}
            value={country}
          />
<br/>
          <label>City</label>
          <input
            type="text"
            className="form-control"
            name="city"
            onChange={this.onChange}
            value={city}
          />
          <br/>

          <label>Password</label>
          <input
            type="password"
            className="form-control"
            name="password"
            onChange={this.onChange}
            value={password}
          />
<br/>
          <label>Controll password</label>
          <input
            type="password"
            className="form-control"
            name="password2"
            onChange={this.onChange}
            value={password2}
          />

          <button type="submit" className="btn btn-primary">
            Register
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
  { register }
)(Register);
