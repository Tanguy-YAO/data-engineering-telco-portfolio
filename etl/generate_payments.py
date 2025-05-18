import json
import random
from datetime import datetime, timedelta

# Étape 1 – Charger les clients existants
with open("data/customers.json", "r") as f:
    customers = json.load(f)

# : Extraire tous les customerID
customer_ids = [customer["customerID"] for customer in customers]

print(f"{len(customer_ids)} clients chargés.")

# Étape 2 – Générer des paiements aléatoires
payment_methods = ["Credit Card", "Mobile Money", "Bank Transfer", "Cash"]
statuses = ["Completed", "Pending", "Failed"]

payments = []
payment_id = 1

for customer_id in customer_ids:
    num_payments = random.randint(1, 5)  # entre 1 et 5 paiements par client

    for _ in range(num_payments):
        payment = {
            "payment_id": f"PAY{payment_id:05}",
            "customerID": customer_id,
            "payment_date": (datetime.today() - timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d"),
            "amount": round(random.uniform(10, 200), 2),
            "payment_method": random.choice(payment_methods),
            "payment_status": random.choice(statuses)
        }
        payments.append(payment)
        payment_id += 1

print(f"{len(payments)} paiements générés.")

# Étape 3 – Sauvegarder les paiements dans un fichier JSON
with open("data/payments.json", "w") as f:
    json.dump(payments, f, indent=4)

print(f"{len(payments)} paiements enregistrés dans data/payments.json.")
