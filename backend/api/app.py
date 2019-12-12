"""Flask application for the backend API."""
import logging

import arrow
from flask import Flask
from flask_cors import CORS

from rogue_sky import darksky, stars

app = Flask(__name__)  # pylint: disable=invalid-name
CORS(app, resources={"/api/*": {"origins": "*"}})

app.config.from_object("api.config.DevelopmentConfig")
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)
logging.getLogger("flask_cors").level = logging.DEBUG


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


@app.route("/api/stars/<latitude>/<longitude>")
def star_visibility_forecast(latitude, longitude):
    """Get daily star visibility forecast for location."""
    _logger.info(
        "Getting star forecast for (%s, %s)", latitude, longitude,
    )
    forecast = stars.get_star_forecast(
        latitude=float(latitude),
        longitude=float(longitude),
        api_key=app.config["DARKSKY_API_KEY"],
    )
    return _format_times(forecast=forecast)


def _parse_datetime(datetime_string, is_date):
    value = arrow.get(datetime_string)
    if is_date:
        return value.format("MMM D")
    return value.format("h:mm a")


def _format_times(forecast):
    daily_forecast_parsed = [
        {
            key: value if "local" not in key else _parse_datetime(value, "date" in key)
            for key, value in day_prediction.items()
        }
        for day_prediction in forecast["daily_forecast"]
    ]

    return {
        key: value if key != "daily_forecast" else daily_forecast_parsed
        for key, value in forecast.items()
    }
