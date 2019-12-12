import axios from "axios";

const backendUrl = 'https://www.camenpiho.com/api'

function getStarForecast(latitude, longitude) {
  const url = `${backendUrl}/stars/${latitude}/${longitude}`
  return axios.get(url)
}

function getCoordinates(query) {
  const url = `${backendUrl}/coordinates/${query}`
  return axios.get(url)
}

export { getStarForecast, getCoordinates }
