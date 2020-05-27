"""Methods for interacting with the recommendations PostgreSQL table."""
from psycopg2.extras import RealDictCursor

from api import logger
from .utilities import pg_cursor, execute_sql_file

_logger = logger.setup(__name__)


def get(pg_url):
    with pg_cursor(pg_url=pg_url, cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM recommendations ORDER BY kind, label ASC;")
        _logger.info(cursor.statusmessage)
        return cursor.fetchall()


def create_table(cursor):
    execute_sql_file(filename="recommendations.sql", cursor=cursor)
    return cursor.statusmessage


def insert_csv(cursor, csv):
    query = "COPY recommendations FROM stdin WITH DELIMITER as ',' CSV HEADER"
    cursor.copy_expert(sql=query, file=csv)
    _logger.info(cursor.statusmessage)
    return cursor.statusmessage
