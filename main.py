from model import Product
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def greet():
    return "Vijitha"


products = [
    Product(id=1, name="Toyota", description="Toyota Raize car",
            price=8500000, quantity=5),
    Product(id=2, name="Honda", description="Honda Civic car",
            price=12000000, quantity=3),
    Product(id=3, name="Laptop", description="Dell laptop",
            price=250000, quantity=10),
    Product(id=4, name="Mobile Phone",
            description="Samsung Galaxy phone", price=180000, quantity=15),
    Product(id=5, name="Keyboard", description="Mechanical keyboard",
            price=12000, quantity=20),
    Product(id=6, name="Mouse", description="Wireless mouse",
            price=5000, quantity=30),
    Product(id=7, name="Monitor", description="Dell 24-inch monitor",
            price=65000, quantity=8),
    Product(id=8, name="Headphones",
            description="Bluetooth headphones", price=15000, quantity=12),
    Product(id=9, name="Printer", description="HP laser printer",
            price=45000, quantity=6),
    Product(id=10, name="Tablet", description="Samsung Galaxy tablet",
            price=95000, quantity=7)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    return products[id-1]
