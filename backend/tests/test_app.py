import json
import os

from rogue_sky import darksky

from api.data import recommendations, utilities

DARKSKY_API_KEY = os.environ["DARKSKY_SECRET_KEY"]


def test_ping(backend_api_client):
    response = backend_api_client.get("/")
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


def test_get_recommendations_by_kind(backend_api_client, database, recommendations_data):
    kind = "book"

    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    response = backend_api_client.get(f"/api/recommendations/kind/{kind}")
    assert response.status_code == 200

    actual = response.get_json()
    assert len(actual) == 5

    for item in actual:
        assert not set(item.keys()) - set(["url", "group_label", "label", "kind", "tags"])
        assert item["kind"] == kind

    response = backend_api_client.get(f"/api/recommendations/kind/unique")
    assert response.status_code == 200

    actual = response.get_json()
    assert list(actual.keys()) == ["kinds"]
    assert len(actual["kinds"]) == 5


def test_get_recommendations_by_tag(backend_api_client, database, recommendations_data):
    tag = "fantasy"

    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    response = backend_api_client.get(f"/api/recommendations/tag/{tag}")
    assert response.status_code == 200

    actual = response.get_json()
    assert len(actual) == 9

    for item in actual:
        assert not set(item.keys()) - set(["url", "group_label", "label", "kind", "tags"])
        assert tag in item["tags"]

    response = backend_api_client.get(f"/api/recommendations/tag/unique")
    assert response.status_code == 200

    actual = response.get_json()
    assert list(actual.keys()) == ["tags"]
    assert len(actual["tags"]) == 20
