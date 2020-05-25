"""Methods for interacting with the recommendations PostgreSQL table."""
from psycopg2.extras import RealDictCursor

from api import logger
from .utilities import pg_cursor, execute_sql_file

_logger = logger.setup(__name__)


def get(pg_url):
    with pg_cursor(pg_url=pg_url, cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM recommendations ORDER BY label DESC;")
        _logger.info(cursor.statusmessage)
        return cursor.fetchall()


def get_by_kind(kind, pg_url):
    with pg_cursor(pg_url=pg_url, cursor_factory=RealDictCursor) as cursor:
        query = "SELECT * FROM recommendations WHERE kind = %s ORDER BY label DESC;"
        cursor.execute(query, (kind,))
        _logger.info(cursor.statusmessage)
        return cursor.fetchall()


def get_by_tag(tag, pg_url):
    with pg_cursor(pg_url=pg_url, cursor_factory=RealDictCursor) as cursor:
        query = "SELECT * FROM recommendations WHERE %s = ANY(tags) ORDER BY label DESC;"
        cursor.execute(query, (tag,))
        _logger.info(cursor.statusmessage)
        return cursor.fetchall()


def get_unique_tags(pg_url):
    with pg_cursor(pg_url=pg_url) as cursor:
        query = """
        SELECT
            *
        FROM (
            SELECT
            DISTINCT(UNNEST(tags))
            FROM recommendations
        ) as uniq_tags
        ORDER by uniq_tags DESC
        ;
        """
        cursor.execute(query)
        _logger.info(cursor.statusmessage)
        tags = cursor.fetchall()
    return [tag for tag, in tags]


def get_unique_kinds(pg_url):
    with pg_cursor(pg_url=pg_url) as cursor:
        query = "SELECT DISTINCT(kind) from recommendations ORDER BY kind DESC;"
        cursor.execute(query)
        _logger.info(cursor.statusmessage)
        kinds = cursor.fetchall()
    return [kind for kind, in kinds]


def create_table(cursor):
    execute_sql_file(filename="recommendations.sql", cursor=cursor)
    return cursor.statusmessage


def insert_csv(cursor, csv):
    query = "COPY recommendations FROM stdin WITH DELIMITER as ',' CSV HEADER"
    cursor.copy_expert(sql=query, file=csv)
    _logger.info(cursor.statusmessage)
    return cursor.statusmessage
