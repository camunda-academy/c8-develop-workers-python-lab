import random
import uuid


def get_random() -> dict[str, object]:
    request_id = str(uuid.uuid4()).replace("-", "")[:7]

    return {
        "requestId": request_id,
        "kitReady": False,
        "productName": random.choice(["Laptop", "Headphones", "Keyboard", "Monitor", "Mouse"]),
        "price": str(random.randint(20, 499)),
        "promotionCode": random.choice(["PROMO10", "PROMO15", "WELCOME", "SPRING", "NONE"]),
        "material": random.choice(["Steel", "Plastic", "Glass", "Carbon", "Aluminum"]),
        "department": random.choice(["Product", "Finance", "HR", "Customer Service", "Sales"]),
        "paymentConfirmation": "PENDING",
    }
