import pandas as pd

from extract import extract_data


def transform_data(customers, products, orders):
    # Convert date columns to datetime
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    # Remove duplicate records
    customers = customers.drop_duplicates()
    products = products.drop_duplicates()
    orders = orders.drop_duplicates()

    # Join product price with orders
    orders = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="left"
    )

    # Calculate revenue
    orders["revenue"] = 0.0

    delivered_orders = orders["status"] == "Delivered"

    orders.loc[delivered_orders, "revenue"] = (
    orders.loc[delivered_orders, "quantity"]
    * orders.loc[delivered_orders, "price"]
)

    # Remove records with missing product prices
    orders = orders.dropna(subset=["price"])

    return customers, products, orders


if __name__ == "__main__":
    customers, products, orders = extract_data()

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )

    print("=== TRANSFORMED ORDERS ===")
    print(orders)

    print("\n=== TOTAL REVENUE ===")
    print(orders["revenue"].sum())