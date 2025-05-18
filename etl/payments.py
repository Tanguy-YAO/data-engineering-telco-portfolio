# Étape 1 – Importation des bibliothèques nécessaires
import requests
import psycopg2
import os
from dotenv import load_dotenv

# Étape 2 – Chargement des identifiants de connexion
load_dotenv()

# Étape 3 – Appel de l’API FastAPI (GET /payments)
url = "http://127.0.0.1:8500/payments"
response = requests.get(url)

# Vérifie que l'API a bien répondu
if response.status_code != 200:
    raise Exception(f"Erreur API /payments : {response.status_code}")

# Récupère les données au format JSON
data = response.json()

# print(f"{len(data)} paiements récupérés depuis l’API.")

# Étape 4 – Connexion à la base PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()
#print("Connexion à PostgreSQL réussie.")

# Étape 5 – Création et insertion dans la table payments
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
conn.commit()
#print("Table payments prête.")

# Étape 6 – Insertion des paiements dans la table PostgreSQL

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

count = 0
for row in data:
    cur.execute(insert_query, row)
    count += 1

conn.commit()
print(f"✅ {count} paiements insérés ou mis à jour.")

# Étape 7 – Fermeture des connexions
cur.close()
conn.close()
print("✅ Connexion PostgreSQL fermée.")
