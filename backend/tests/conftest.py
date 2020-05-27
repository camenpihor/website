import contextlib
import logging
import os
import json

import importlib.resources as pkg_resources
import pytest

from api.app import app
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
    """Flask API client for testing."""
    app.config["TESTING"] = True
    os.environ["DARKSKY_SECRET_KEY"] = "testing"

    with app.test_client() as client:
        yield client
