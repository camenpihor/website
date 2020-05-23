from api.data import utilities


def test_read_sql_file():
    actual = utilities.read_sql_file(
        filename="test_sql_query.sql", module_path="tests.resources"
    )
    assert len(actual) == 2


def test_execute_sql_file(database):
    with utilities.pg_cursor(pg_url=database) as cursor:
        utilities.execute_sql_file(
            filename="test_sql_query.sql", module_path="tests.resources", cursor=cursor
        )
        cursor.execute("SELECT * FROM test;")
        response = cursor.fetchall()

    assert len(response) == 1
    assert response[0][0] == 10
