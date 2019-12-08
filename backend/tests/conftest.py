import contextlib
import os
import json

import pkg_resources
import psycopg2
from psycopg2 import sql
import pytest

from api.app import app

PG_URL = os.environ["TEST_DATABASE_URL"]


class TestDatabase:
    pg_url = PG_URL

    def __init__(self):
        self.tear_down()

    @contextlib.contextmanager
    def get_cursor(self):
        connection = psycopg2.connect(self.pg_url)
        cursor = connection.cursor()
        try:
            yield cursor
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    def tear_down(self):
        with self.get_cursor() as cursor:
            cursor.execute(
                """
            SELECT schemaname, tablename FROM pg_catalog.pg_tables
            WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
            ;
            """
            )
            tables = cursor.fetchall()
            print("Cleaning test database")
            for (schema, table) in tables:
                cursor.execute(
                    sql.SQL("DROP TABLE {}").format(sql.Identifier(schema, table))
                )


@pytest.fixture(scope="function")
def test_database():
    database = TestDatabase()
    yield database
    database.tear_down()


@pytest.fixture(scope="function")
def darksky_json_response():
    """Response from DarkSky that was translated to JSON."""
    return json.loads(
        pkg_resources.resource_string("tests.resources", "test_darksky_response.json")
    )


@pytest.fixture
def backend_api_client(scope="method"):
    app.config.from_object("api.config.TestingConfig")

    with app.test_client() as client:
        yield client
