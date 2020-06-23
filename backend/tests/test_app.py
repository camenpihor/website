import os
import xml.etree.ElementTree as ET

from rogue_sky import darksky

DARKSKY_API_KEY = os.environ["DARKSKY_SECRET_KEY"]


def test_ping(backend_api_client):
    response = backend_api_client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_get_star_visibility_forecast(
    requests_mock, backend_api_client, darksky_json_response
):
    latitude = 47.6038321
    longitude = -122.3300624
    api_key = DARKSKY_API_KEY

    requests_mock.get(
        darksky.DARKSKY_URL.format(
            api_key=api_key, latitude=latitude, longitude=longitude
        ),
        json=darksky_json_response,
    )
    response = backend_api_client.get(f"api/stars/{latitude}/{longitude}")
    assert response.status_code == 200

    actual = response.get_json()
    assert len(actual["daily_forecast"]) == 8
    assert set(actual.keys()) == set(
        [
            "latitude",
            "longitude",
            "queried_date_utc",
            "daily_forecast",
            "city",
            "state",
            "timezone",
        ]
    )
    assert set(actual["daily_forecast"][0].keys()) == set(
        [key.replace("utc", "local") for key in darksky.DAILY_WEATHER_MAPPING]
        + ["star_visibility", "moon_illumination", "moonrise_time_local"]
    )
    assert actual["daily_forecast"][0]["sunset_time_local"] == "2019-11-10T16:29:00-05:00"


def test_get_coordinates(backend_api_client, requests_mock):
    requests_mock.get(
        "https://nominatim.openstreetmap.org/search?q=seattle&format=json&limit=1",
        json={"lat": 50, "lon": 50, "display_name": "Seattle, WA"},
    )
    response = backend_api_client.get("/api/coordinates/seattle")
    assert response.status_code == 200


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
