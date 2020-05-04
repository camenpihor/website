import contextlib
import logging
import os
import json

import pkg_resources
import pytest

from api.app import app

logging.disable(logging.CRITICAL)


@pytest.fixture(scope="function")
def darksky_json_response():
    """Response from DarkSky that was translated to JSON."""
    return json.loads(
        pkg_resources.resource_string("tests.resources", "test_darksky_response.json")
    )


@pytest.fixture(scope="function")
def serialized_star_response():
    """JSON-Serialized star visibility forecast."""
    return json.loads(
        pkg_resources.resource_string(
            "tests.resources", "test_serialized_star_response.json"
        )
    )


@pytest.fixture
def backend_api_client(scope="method"):
    app.config["TESTING"] = True
    os.environ["DARKSKY_SECRET_KEY"] = "testing"

    with app.test_client() as client:
        yield client
