import pandas as pd


def extract_data():
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")

    return customers, products, orders


if __name__ == "__main__":
    customers, products, orders = extract_data()

    print("Customers:")
    print(customers.head())

    print("\nProducts:")
    print(products.head())

    print("\nOrders:")
    print(orders.head())

if __name__ == "__main__":
    customers, products, orders = extract_data()

    print("=== CUSTOMERS ===")
    print(customers.head())
    print("\nCustomer Data Types:")
    print(customers.dtypes)

    print("\n=== PRODUCTS ===")
    print(products.head())
    print("\nProduct Data Types:")
    print(products.dtypes)

    print("\n=== ORDERS ===")
    print(orders.head())
    print("\nOrder Data Types:")
    print(orders.dtypes)