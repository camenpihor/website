from api.data import utilities, recommendations


def test_create_table(database):
    table_discovery_query = """
    SELECT
        *
    FROM information_schema.tables

    WHERE table_name = 'recommendations'
    ;
    """

    with utilities.pg_cursor(pg_url=database) as cursor:
        cursor.execute("DROP TABLE recommendations CASCADE;")
        cursor.execute(table_discovery_query)
        assert cursor.rowcount == 0

        recommendations.create_table(cursor=cursor)
        cursor.execute(table_discovery_query)
        assert cursor.rowcount == 1


def test_insert_csv(database, recommendations_data):
    query = "SELECT * FROM recommendations;"

    with utilities.pg_cursor(pg_url=database) as cursor:
        cursor.execute(query)
        assert cursor.rowcount == 0

        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)
        cursor.execute(query)
        assert cursor.rowcount == 28


def test_get(database, recommendations_data):
    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    actual = recommendations.get(pg_url=database)
    assert len(actual) == 28
