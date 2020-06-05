import os

from rogue_sky import darksky

DARKSKY_API_KEY = os.environ["DARKSKY_SECRET_KEY"]


def test_ping(backend_api_client):
    response = backend_api_client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_star_forecast(requests_mock, backend_api_client, darksky_json_response):
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
        ["latitude", "longitude", "queried_date_utc", "daily_forecast", "city", "state"]
    )
    assert set(actual["daily_forecast"][0].keys()) == set(
        [key.replace("utc", "local") for key in darksky.DAILY_WEATHER_MAPPING]
        + ["star_visibility"]
    )
    assert actual["daily_forecast"][0]["sunset_time_local"] == "2019-11-10T16:29:00-05:00"
