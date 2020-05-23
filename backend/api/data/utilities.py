"""Utilities for making PostgreSQL connections."""
from contextlib import contextmanager
import pkg_resources

import psycopg2

from api import logger

_logger = logger.setup(__name__)


@contextmanager
def pg_connect(pg_url):
    _logger.debug("Creating connection to %s...", pg_url)

    connection = psycopg2.connect(pg_url)
    try:
        yield connection

    finally:
        connection.commit()
        connection.close()


@contextmanager
def pg_cursor(pg_url, **cursor_kwargs):
    connection = psycopg2.connect(pg_url)

    _logger.debug("Creating cursor %s...", pg_url)
    cursor = connection.cursor(**cursor_kwargs)
    try:
        yield cursor

    finally:
        _logger.debug("Closing connection and cursor...")
        connection.commit()
        cursor.close()
        connection.close()


def read_sql_file(filename, module_path="api.data.table_definitions"):
    _logger.debug("Reading sql file %s from %s", filename, module_path)
    file_string = pkg_resources.resource_string(module_path, filename).decode()
    return [query.strip("\n") for query in file_string.strip("\n").split(";") if query]


def execute_sql_file(filename, cursor, module_path="api.data.table_definitions"):
    _logger.info("Executing sql file %s", filename)
    queries = read_sql_file(filename=filename, module_path=module_path)

    for query in queries:
        cursor.execute(query)
        _logger.info(cursor.statusmessage)
