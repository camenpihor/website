import contextlib
import logging
import os
import json

import importlib.resources as pkg_resources

import pytest

from api.app import app
from api.data.utilities import pg_cursor, execute_sql_file
from tests import resources as test_resources

logging.disable(logging.CRITICAL)


@pytest.fixture(scope="function")
def darksky_json_response():
    """Response from DarkSky that was translated to JSON."""
    return json.load(
        pkg_resources.open_text(test_resources, "test_darksky_response.json")
    )


@pytest.fixture(scope="function")
def serialized_star_response():
    """JSON-Serialized star visibility forecast."""
    return json.load(
        pkg_resources.open_text(test_resources, "test_serialized_star_response.json")
    )


@pytest.fixture(scope="function")
def backend_api_client():
    app.config["TESTING"] = True
    os.environ["DARKSKY_SECRET_KEY"] = "testing"
    os.environ["DATABASE_URL"] = os.environ["TEST_DATABASE_URL"]

    with app.test_client() as client:
        yield client


@pytest.fixture(scope="function")
def database():
    url = os.environ["TEST_DATABASE_URL"]

    with pg_cursor(pg_url=url) as cursor:
        for filename in ["recommendations.sql"]:
            execute_sql_file(cursor=cursor, filename=filename)

    try:
        yield url

    finally:
        with pg_cursor(pg_url=url) as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")


@pytest.fixture()
def recommendations_data():
    return pkg_resources.open_text(test_resources, "test_recommendations.csv")
