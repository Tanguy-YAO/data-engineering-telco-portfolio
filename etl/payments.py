# Étape 1 – Importation des bibliothèques nécessaires
import requests
import psycopg2
from psycopg2.extras import execute_batch
import os
from dotenv import load_dotenv

# Étape 2 – Chargement des identifiants de connexion
load_dotenv()


def load_payments():
    """Récupère les paiements via l'API et les insère dans PostgreSQL."""
    url = "http://127.0.0.1:8500/payments"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erreur API /payments : {response.status_code}")

    data = response.json()

    with psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as conn:
        with conn.cursor() as cur:
            create_table_query = """
CREATE TABLE IF NOT EXISTS payments (
    payment_id VARCHAR PRIMARY KEY,
    customerID VARCHAR,
    payment_date DATE,
    amount FLOAT,
    payment_method VARCHAR,
    payment_status VARCHAR
);
"""
            cur.execute(create_table_query)

            insert_query = """
INSERT INTO payments (
    payment_id, customerID, payment_date, amount, payment_method, payment_status
)
VALUES (
    %(payment_id)s, %(customerID)s, %(payment_date)s, %(amount)s, %(payment_method)s, %(payment_status)s
)
ON CONFLICT (payment_id) DO UPDATE SET
    customerID = EXCLUDED.customerID,
    payment_date = EXCLUDED.payment_date,
    amount = EXCLUDED.amount,
    payment_method = EXCLUDED.payment_method,
    payment_status = EXCLUDED.payment_status;
"""
            execute_batch(cur, insert_query, data)
            conn.commit()

    print(f"✅ {len(data)} paiements insérés ou mis à jour.")


if __name__ == "__main__":
    load_payments()
