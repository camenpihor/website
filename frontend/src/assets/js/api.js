import axios from "axios";

// production 'https://www.camenpiho.com/api'
// development 'http://127.0.0.1:5000/api'
const backendUrl = process.env.VUE_APP_BACKEND_ENDPOINT;

function getStarForecast(latitude, longitude) {
  const url = `${backendUrl}/stars/${latitude}/${longitude}`;
  return axios.get(url);
}

function getCoordinates(query) {
  const url = `${backendUrl}/coordinates/${query}`;
  return axios.get(url);
}

function getBlogPosts() {
  const url = `${backendUrl}/blog`;
  return axios.get(url);
}

function getBlogPost(query) {
  const url = `${backendUrl}/blog/${query}`;
  return axios.get(url);
}

function getAstronomicalEvents() {
  const url = `${backendUrl}/astronomical_events`;
  return axios.get(url);
}

export {
  getStarForecast,
  getCoordinates,
  getBlogPosts,
  getBlogPost,
  getAstronomicalEvents,
};
