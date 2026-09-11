import os

from extract import extract_data
from transform import transform_data


def load_data(customers, products, orders):
    # Create processed directory if it doesn't exist
    os.makedirs("processed", exist_ok=True)

    # Save transformed datasets
    customers.to_csv(
        "processed/customers_processed.csv",
        index=False
    )

    products.to_csv(
        "processed/products_processed.csv",
        index=False
    )

    orders.to_csv(
        "processed/orders_processed.csv",
        index=False
    )

    print("Data successfully loaded into processed directory.")


if __name__ == "__main__":
    customers, products, orders = extract_data()

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )

    load_data(customers, products, orders)