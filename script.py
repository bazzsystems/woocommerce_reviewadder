import csv

reviews = []

with open("reviews.csv", "r", newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        reviews.append(row)
import random
from woocommerce import API

# Set up your WooCommerce API credentials
wcapi = API(
    url="https://x.com/",  # Replace with your website URL
    consumer_key="ck_x",
    consumer_secret="cs_x",
    version="wc/v3"
)

# Get the list of product IDs
response = wcapi.get("products")
products = response.json()
product_ids = [product["id"] for product in products]

# Randomly assign reviews to products
for review in reviews:
    product_id = random.choice(product_ids)
    rating, author, date, review_text = review
    review_data = {
        "product_id": product_id,
        "review": review_text,
        "reviewer": author,
        "reviewer_email": "example@example.com",  # Use a placeholder email or add a real one
        "rating": int(float(rating)),
        "status": "approved",  # Automatically approve the review
    }

    response = wcapi.post("products/reviews", review_data)
    if response.status_code == 201:
        print(f"Successfully added review to product {product_id}: {review_text}")
    else:
        print(f"Error adding review to product {product_id}: {response.text}")

print("Finished adding reviews to products")
