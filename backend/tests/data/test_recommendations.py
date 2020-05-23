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


def test_get_by_kind(database, recommendations_data):
    kind = "blog"

    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    actual = recommendations.get_by_kind(kind=kind, pg_url=database)
    assert len(actual) == 4
    for row in actual:
        assert row["kind"] == kind


def test_get_by_tag(database, recommendations_data):
    tag = "nature"

    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    actual = recommendations.get_by_tag(tag=tag, pg_url=database)
    assert len(actual) == 5
    for row in actual:
        assert tag in row["tags"]


def test_get_unique_tags(database, recommendations_data):
    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    actual = recommendations.get_unique_tags(pg_url=database)
    assert len(actual["tags"]) == 20


def test_get_unique_kinds(database, recommendations_data):
    with utilities.pg_cursor(pg_url=database) as cursor:
        recommendations.insert_csv(cursor=cursor, csv=recommendations_data)

    actual = recommendations.get_unique_kinds(pg_url=database)
    assert len(actual["kinds"]) == 5
