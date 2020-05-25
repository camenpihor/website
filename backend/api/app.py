"""Flask application for the backend API."""
import json
import os

from flask import Flask, Response, request
from rogue_sky import darksky, stars

from api import logger
from api.data import recommendations

app = Flask(__name__)  # pylint: disable=invalid-name
_logger = logger.setup(__name__)

FRONTEND_ADDRESS = os.environ.get("FRONTEND_ADDRESS", None)
DARKSKY_SECRET_KEY = os.environ["DARKSKY_SECRET_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]


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


@app.route("/api/recommendations")
def get_recommendations():
    query = request.args
    if not query:
        data = recommendations.get(pg_url=DATABASE_URL)

    elif "tag" in query:
        tag = query.get("tag")
        if tag == "unique":
            data = recommendations.get_unique_tags(pg_url=DATABASE_URL)
        else:
            data = recommendations.get_by_tag(tag=tag, pg_url=DATABASE_URL)

    elif "kind" in query:
        kind = query.get("kind")
        if kind == "unique":
            data = recommendations.get_unique_kinds(pg_url=DATABASE_URL)
        else:
            data = recommendations.get_by_kind(kind=kind, pg_url=DATABASE_URL)
    else:
        raise ValueError(f"Cannot handle query. Got {query}")

    return _json_response(data=data)


def _json_response(data):
    """Return a Flask response with the mimetype set to JSON."""
    resp = Response(json.dumps(data), mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = FRONTEND_ADDRESS
    return resp
