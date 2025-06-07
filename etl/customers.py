# Etape 1:Importation des bibliothèques nécessaires
import requests                      # Pour appeler l'API
import psycopg2                      # Pour se connecter à PostgreSQL
from psycopg2.extras import execute_batch
import os                            # Pour accéder aux variables d’environnement
from dotenv import load_dotenv       # Pour charger le fichier .env

# Etape 2: Chargement des variables définies dans le fichier .env pour accéder à PostgreSQL
load_dotenv()

# Etape 3: Appel de l'API FastAPI
def load_customers():
    """Charge les clients via l'API et les insère dans PostgreSQL."""
    url = "http://127.0.0.1:8500/customers"  # URL de l'API locale

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erreur API : {response.status_code}")

    data = response.json()

    # Connexion via les identifiants sécurisés
    with psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as conn:
        with conn.cursor() as cur:
            insert_query = """
INSERT INTO customers (
    customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
    PhoneService, MultipleLines, InternetService, OnlineSecurity,
    OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
    StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
    MonthlyCharges, TotalCharges, Churn
)
VALUES (
    %(customerID)s, %(gender)s, %(SeniorCitizen)s, %(Partner)s, %(Dependents)s, %(tenure)s,
    %(PhoneService)s, %(MultipleLines)s, %(InternetService)s, %(OnlineSecurity)s,
    %(OnlineBackup)s, %(DeviceProtection)s, %(TechSupport)s, %(StreamingTV)s,
    %(StreamingMovies)s, %(Contract)s, %(PaperlessBilling)s, %(PaymentMethod)s,
    %(MonthlyCharges)s, %(TotalCharges)s, %(Churn)s
)
ON CONFLICT (customerID) DO UPDATE SET
    gender = EXCLUDED.gender,
    SeniorCitizen = EXCLUDED.SeniorCitizen,
    Partner = EXCLUDED.Partner,
    Dependents = EXCLUDED.Dependents,
    tenure = EXCLUDED.tenure,
    PhoneService = EXCLUDED.PhoneService,
    MultipleLines = EXCLUDED.MultipleLines,
    InternetService = EXCLUDED.InternetService,
    OnlineSecurity = EXCLUDED.OnlineSecurity,
    OnlineBackup = EXCLUDED.OnlineBackup,
    DeviceProtection = EXCLUDED.DeviceProtection,
    TechSupport = EXCLUDED.TechSupport,
    StreamingTV = EXCLUDED.StreamingTV,
    StreamingMovies = EXCLUDED.StreamingMovies,
    Contract = EXCLUDED.Contract,
    PaperlessBilling = EXCLUDED.PaperlessBilling,
    PaymentMethod = EXCLUDED.PaymentMethod,
    MonthlyCharges = EXCLUDED.MonthlyCharges,
    TotalCharges = EXCLUDED.TotalCharges,
    Churn = EXCLUDED.Churn;
"""

            for row in data:
                try:
                    row["TotalCharges"] = float(row["TotalCharges"])
                except ValueError:
                    row["TotalCharges"] = None

            execute_batch(cur, insert_query, data)
            conn.commit()

    print(f"{len(data)} clients récupérés depuis l'API avec succès.")
    print("✅ Données insérées avec succès.")


if __name__ == "__main__":
    load_customers()

