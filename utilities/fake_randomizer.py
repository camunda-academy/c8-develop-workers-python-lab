import random
import uuid


def get_random() -> dict[str, object]:
    order_id = str(uuid.uuid4()).replace("-", "")[:7]

    return {
        "orderId": order_id,
        "packaged": False,
        "productName": random.choice(["Laptop", "Headphones", "Keyboard", "Monitor", "Mouse"]),
        "price": str(random.randint(20, 499)),
        "promotionCode": random.choice(["PROMO10", "PROMO15", "WELCOME", "SPRING", "NONE"]),
        "material": random.choice(["Steel", "Plastic", "Wood", "Carbon", "Aluminum"]),
        "department": random.choice(["Electronics", "Home", "Sports", "Fashion", "Books"]),
        "paymentConfirmation": "PENDING",
    }
