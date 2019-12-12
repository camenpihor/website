import json

import arrow
from rogue_sky import darksky

from api import app


def test_ping(backend_api_client):
    response = backend_api_client.get("/")
    assert response.status_code == 200


def test_star_forecast(requests_mock, backend_api_client, darksky_json_response):
    latitude = 47.6038321
    longitude = -122.3300624
    api_key = backend_api_client.application.config["DARKSKY_API_KEY"]

    requests_mock.get(
        darksky.DARKSKY_URL.format(
            api_key=api_key, latitude=latitude, longitude=longitude
        ),
        json=darksky_json_response,
    )
    response = backend_api_client.get(f"api/stars/{latitude}/{longitude}")
    assert response.status_code == 200

    actual = json.loads(response.data)
    assert len(actual["daily_forecast"]) == 8
    assert set(actual.keys()) == set(
        ["latitude", "longitude", "queried_date_utc", "daily_forecast", "city", "state"]
    )
    assert set(actual["daily_forecast"][0].keys()) == set(
        [key.replace("utc", "local") for key in darksky.DAILY_WEATHER_MAPPING.keys()]
        + ["star_visibility"]
    )
    assert actual["daily_forecast"][0]["sunset_time_local"] == "4:29 pm"
