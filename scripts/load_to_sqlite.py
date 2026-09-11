import sqlite3

import pandas as pd


DATABASE = "processed/ecommerce.db"


def load_to_sqlite():
    connection = sqlite3.connect(DATABASE)

    customers = pd.read_csv(
        "processed/customers_processed.csv"
    )

    products = pd.read_csv(
        "processed/products_processed.csv"
    )

    orders = pd.read_csv(
        "processed/orders_processed.csv"
    )

    customers.to_sql(
        "customers",
        connection,
        if_exists="replace",
        index=False
    )

    products.to_sql(
        "products",
        connection,
        if_exists="replace",
        index=False
    )

    orders.to_sql(
        "orders",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Data successfully loaded into SQLite.")


if __name__ == "__main__":
    load_to_sqlite()