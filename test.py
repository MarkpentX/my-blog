products = [
    {
        "name": "Iphone 12",
        "price": 19999,
        "year": 2022,
    },
    {
        "name": "Iphone 13",
        "price": 29999,
        "year": 2023,
    },
]

user_request = "Iphone"

for product in products:
    if product["name"] == user_request:
        print("Some information...")

