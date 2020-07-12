"""Flask application for the backend API."""
import datetime
import glob
import json
import os
import xml.etree.ElementTree as ET

from flask import Flask, Response
import mistune
from rogue_sky import darksky, stars

from api import logger

app = Flask(__name__)  # pylint: disable=invalid-name
_logger = logger.setup(__name__)

FRONTEND_ADDRESS = os.environ.get("FRONTEND_ADDRESS", None)
DARKSKY_SECRET_KEY = os.environ["DARKSKY_SECRET_KEY"]
XML_DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S PT"


@app.route("/api/health")
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
def get_star_visibility_forecast(latitude, longitude):
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


@app.route("/api/astronomical_events")
def get_astronomical_events():
    """Get astronomical events."""
    _logger.info("Getting astronomical events...")
    return _json_response(data=_read_astronomical_events())


@app.route("/api/blog")
def get_blog_posts():
    """Get blog posts."""
    _logger.info("Getting blog posts...")
    print("here")
    data = _read_blog_posts(include_content=False)
    return _json_response(data=data)


@app.route("/api/blog/<title>")
def get_blog_post(title):
    """Get blog post."""
    _logger.info("Getting blog post %s...", title)
    filepath = os.path.join("api", "resources", "blog", "final", f"{title}.md")
    data = _parse_blog_post(filepath=filepath) if os.path.exists(filepath) else None
    return _json_response(data=data)


@app.route("/api/rss")
def get_rss():
    """Get the RSS feed."""
    _logger.info("Serving RSS...")

    posts = _read_blog_posts()

    astronomical_events = [
        event
        for event in _read_astronomical_events()
        if event["date"] == str(datetime.date.today())
    ]

    def add_subelement(parent, child_name, child_text=None):
        """Add subelement to XML element."""
        child = ET.SubElement(parent, child_name)
        if child_text:
            child.text = child_text
        return child

    rss = ET.Element("rss", version="2.0")

    channel = add_subelement(rss, "channel")
    add_subelement(channel, "title", "Camen Piho")
    add_subelement(channel, "link", "https://www.camenpiho.com/blog")
    add_subelement(channel, "description", "Blog and Astronomical Events by Camen Piho")
    add_subelement(channel, "language", "en-us")
    add_subelement(
        channel, "pubDate", datetime.datetime.utcnow().strftime(XML_DATETIME_FORMAT)
    )
    add_subelement(channel, "category", "Blog")

    image = add_subelement(channel, "image")
    add_subelement(image, "url", "https://www.camenpiho.com/site-icon.png")
    add_subelement(image, "title", "Camen Piho")
    add_subelement(image, "link", "https://www.camenpiho.com/blog")

    for post in posts:
        post_url = f"https://www.camenpiho.com/blog/{post['url']}"

        item = add_subelement(channel, "item")
        add_subelement(item, "title", post["title"].title())
        add_subelement(item, "link", post_url)
        add_subelement(item, "guid", post_url)
        add_subelement(item, "author", "camen.rogue@gmail.com (Camen Piho)")
        add_subelement(
            item,
            "pubDate",
            datetime.datetime.strptime(post["date"], "%d %B %Y").strftime(
                XML_DATETIME_FORMAT
            ),
        )

        description = add_subelement(item, "description")
        add_subelement(description, f"![CDATA[{post['content']}]]")

    for event in astronomical_events:
        item = add_subelement(channel, "item")
        add_subelement(item, "title", event["event"])
        add_subelement(item, "link", "https://www.camenpiho.com/roguesky")
        add_subelement(item, "guid", "https://www.camenpiho.com/roguesky")
        add_subelement(item, "author", "camen.rogue@gmail.com (Camen Piho)")
        add_subelement(
            item, "pubDate", datetime.datetime.utcnow().strftime(XML_DATETIME_FORMAT),
        )
        add_subelement(item, "description", event["info"] if event["info"] else "")

    rss_string = ET.tostring(rss, xml_declaration=True, encoding="UTF-8").decode()
    rss_string = rss_string.replace(" /></description>", "></description>")

    resp = Response(rss_string, mimetype="text/xml",)
    return resp


def _read_astronomical_events():
    filepath = os.path.join("api", "resources", "astronomy", "astronomical_events.json")
    with open(filepath, "r") as buffer:
        events = json.load(buffer)
    return events


def _read_blog_posts(include_content=True):
    posts = [
        _parse_blog_post(filepath=filepath, include_content=include_content)
        for filepath in glob.glob(
            os.path.join("api", "resources", "blog", "final", "*.md")
        )
    ]
    posts = sorted(
        posts,
        key=lambda post: datetime.datetime.strptime(post["date"], "%d %B %Y"),
        reverse=True,
    )
    return posts


def _parse_blog_post(filepath, include_content=True):
    """Parse blog post markdown into HTML.

    Parameters
    ----------
    filepath : str
    include_content : bool, optional
        Whether to include blog content, or just summary, by default True

    Returns
    -------
    dict
        {
            "title": str,
            "url": str,
            "date": str,
            "summary": str,
            "content": str
        }
    """

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
    if include_content:
        metadata["content"] = markdown(post_markdown)
    return metadata


def _json_response(data):
    """Return a Flask response with the mimetype set to JSON."""
    resp = Response(json.dumps(data), mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = FRONTEND_ADDRESS
    return resp
