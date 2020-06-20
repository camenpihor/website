"""Flask application for the backend API."""
import glob
import json
import os

from flask import Flask, Response
import mistune
from rogue_sky import darksky, stars

from api import logger

app = Flask(__name__)  # pylint: disable=invalid-name
_logger = logger.setup(__name__)

FRONTEND_ADDRESS = os.environ.get("FRONTEND_ADDRESS", None)
DARKSKY_SECRET_KEY = os.environ["DARKSKY_SECRET_KEY"]


@app.route("/api/health")
def ping_test():
    """Backend API ping test."""
    return _json_response(data={"status": "ok"})


@app.route("/api/coordinates/<query>")
def coordinates(query):
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


@app.route("/api/blog")
def blog_posts():
    """Get blog posts."""
    _logger.info("Getting blog posts...")
    filepaths = glob.glob(os.path.join("api", "blog", "final", "*.md"))
    data = [_parse_blog_post(filepath=filepath, content=False) for filepath in filepaths]
    return _json_response(data=data)


@app.route("/api/blog/<title>")
def blog_post(title):
    """Get blog post."""
    _logger.info("Getting blog post %s...", title)
    filepath = os.path.join("api", "blog", "final", f"{title}.md")
    data = _parse_blog_post(filepath=filepath) if os.path.exists(filepath) else None
    return _json_response(data=data)


def _parse_blog_post(filepath, content=True):
    class CustomRenderer(mistune.HTMLRenderer):
        """Custom markdown renderer."""

        def link(self, link, text=None, title=None):
            """Add target="_blank" to links."""
            return f"<a href={link} target='_blank'>{text}</a>"

    markdown = mistune.create_markdown(renderer=CustomRenderer())

    with open(filepath, "r") as buffer:
        data = buffer.read()

    _, metadata, post_markdown = data.split("---", 2)

    metadata = json.loads(metadata.replace("\n", "").replace("  ", " "))
    if content:
        metadata["content"] = markdown(post_markdown)
    return metadata


def _json_response(data):
    """Return a Flask response with the mimetype set to JSON."""
    resp = Response(json.dumps(data), mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = FRONTEND_ADDRESS
    return resp
