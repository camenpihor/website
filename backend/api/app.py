"""Flask application for the backend API."""
import json
import os

from flask import Flask, Response
from rogue_sky import darksky, stars

from api import logger

app = Flask(__name__)  # pylint: disable=invalid-name
_logger = logger.setup(__name__)

FRONTEND_ADDRESS = os.environ.get("FRONTEND_ADDRESS", None)
DARKSKY_SECRET_KEY = os.environ["DARKSKY_SECRET_KEY"]


@app.route("/")
def ping_test():
    """Backend API ping test."""
    return _json_response(data={"status": "ok"})


@app.route("/api/coordinates/<query>")
def get_coordinates(query):
    """Get coordinates from query."""
    _logger.info("Getting coordinates for %s", query)
    latitude, longitude = darksky.parse_address(address=query)
    return _json_response(data={"latitude": latitude, "longitude": longitude})


@app.route("/api/stars/<latitude>/<longitude>")
def star_visibility_forecast(latitude, longitude):
    """Get daily star visibility forecast for location."""
    _logger.info(
        "Getting star forecast for (%s, %s)", latitude, longitude,
    )
    return _json_response(
        data=stars.get_star_forecast(
            latitude=float(latitude),
            longitude=float(longitude),
            api_key=DARKSKY_SECRET_KEY,
        )
    )


def _json_response(data):
    """Return a Flask response with the mimetype set to JSON."""
    resp = Response(json.dumps(data), mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = FRONTEND_ADDRESS
    return resp
