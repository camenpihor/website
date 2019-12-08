"""Flask application for the backend API."""
import logging

from flask import Flask
from flask_cors import CORS

from rogue_sky import darksky, stars

app = Flask(__name__)  # pylint: disable=invalid-name
CORS(app, resources={"/api/*": {"origins": "http://localhost:8080"},})

app.config.from_object("api.config.DevelopmentConfig")
logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)


@app.route("/")
def ping_test():
    """Backend API ping test."""
    return "Success"


@app.route("/api/coordinates/<query>")
def get_coordinates(query):
    """Get coordinates from query."""
    _logger.info("Getting coordinates for %s", query)
    latitude, longitude = darksky.parse_address(address=query)
    return {"latitude": latitude, "longitude": longitude}


@app.route("/api/weather/<latitude>,<longitude>")
def weather_forecast(latitude, longitude):
    """Get daily weather forecast for location."""
    return darksky.get_weather_forecast(
        latitude=float(latitude),
        longitude=float(longitude),
        api_key=app.config["DARKSKY_API_KEY"],
        database_url=app.config["DATABASE_URL"],
    )


@app.route("/api/stars/<latitude>/<longitude>")
def star_visibility_forecast(latitude, longitude):
    """Get daily star visibility forecast for location."""
    _logger.info("Getting star forecast for (%s, %s)", latitude, longitude)
    return stars.get_star_forecast(
        latitude=float(latitude),
        longitude=float(longitude),
        api_key=app.config["DARKSKY_API_KEY"],
        database_url=app.config["DATABASE_URL"],
    )
