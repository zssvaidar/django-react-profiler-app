import { combineReducers } from 'redux';
import services from "./services";
import auth from "./auth";

export default combineReducers({
  services, auth
});
