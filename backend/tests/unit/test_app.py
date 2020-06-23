import os
import xml.etree.ElementTree as ET

from rogue_sky import darksky

DARKSKY_API_KEY = os.environ["DARKSKY_SECRET_KEY"]


def test_ping(backend_api_client):
    response = backend_api_client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_get_blog_posts(backend_api_client):
    response = backend_api_client.get("/api/blog")
    assert response.status_code == 200

    actual = response.get_json()
    assert isinstance(actual, list)
    assert len(actual) > 0
    assert not set(actual[0]) - set(["title", "date", "summary", "url"])


def test_get_blog_post(backend_api_client):
    response = backend_api_client.get("/api/blog/something-worth-writing")
    assert response.status_code == 200

    actual = response.get_json()
    assert isinstance(actual, dict)
    assert not set(actual) - set(["title", "date", "summary", "content", "url"])


def test_get_rss(backend_api_client):
    response = backend_api_client.get("/api/rss")
    assert response.status_code == 200
    assert ET.fromstring(response.data.decode())


def test_get_astronomical_events(backend_api_client):
    response = backend_api_client.get("/api/astronomical_events")
    assert response.status_code == 200

    actual = response.get_json()
    assert isinstance(actual, list)
    assert len(actual) > 0

    actual = actual[0]
    assert isinstance(actual, dict)
    assert not set(actual) - set(["date", "event", "info", "type"])
