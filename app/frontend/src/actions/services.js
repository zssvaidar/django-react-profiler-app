import axios from 'axios';
import { GET_SERVICES, DELETE_SERVICE } from './types';

export const getServices = () => dispatch => {
  axios.get("api-profiler/services")
    .then(res => {
      dispatch({
        type:GET_SERVICES,
        payload: res.data
      });
    })
    .catch(err=> console.log(err));
};

export const deleteService = id => dispatch => {
  axios.delete(`api-profiler/services/${id}`)
    .then(res => {
      dispatch({
        type:DELETE_SERVICE,
        payload: id
      });
    })
    .catch(err=> console.log(err));
};
