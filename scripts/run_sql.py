import sqlite3


DATABASE = "processed/ecommerce.db"


def run_query(query):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    connection.close()

    return results


if __name__ == "__main__":
    query = """
        SELECT
            status,
            COUNT(*) AS order_count
        FROM orders
        GROUP BY status
        ORDER BY order_count DESC;
    """

    results = run_query(query)

    for row in results:
        print(row)