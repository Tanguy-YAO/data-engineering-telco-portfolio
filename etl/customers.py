# Etape 1:Importation des bibliothèques nécessaires
import requests                      # Pour appeler l'API
import psycopg2                      # Pour se connecter à PostgreSQL
import os                            # Pour accéder aux variables d’environnement
from dotenv import load_dotenv       # Pour charger le fichier .env

# Etape 2: Chargement des variables définies dans le fichier .env pour accéder à PostgreSQL
load_dotenv()

# Etape 3: Appel de l'API FastAPI
url = "http://127.0.0.1:8500/customers"  # URL de ton endpoint local

response = requests.get(url) # Appel GET à l'API

# Vérifie que la réponse est correcte (status 200)
if response.status_code != 200:
    raise Exception(f"Erreur API : {response.status_code}")

# Récupère les données au format JSON (liste de dictionnaires)
data = response.json()

#print(f"{len(data)} clients récupérés depuis l'API avec succès.")

# Etape 4: Connexion à la base PostgreSQL

# Connexion via les identifiants sécurisés
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# Création d’un curseur pour exécuter les requêtes
cur = conn.cursor()

#print("Connexion à PostgreSQL réussie.")

# ---------------------------------------------
# Étape 6 – Insertion des données dans PostgreSQL
# ---------------------------------------------

# Requête SQL avec gestion des doublons
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

# Insertion ligne par ligne
for row in data:
    try:
        # Gestion du champ TotalCharges qui peut être vide ou invalide
        row["TotalCharges"] = float(row["TotalCharges"])
    except:
        row["TotalCharges"] = None

    cur.execute(insert_query, row)

# Validation des insertions
conn.commit()

# Étape 7 – Fermeture propre + log final

print(f"{len(data)} clients récupérés depuis l'API avec succès.")
print("✅ Données insérées avec succès.")

cur.close() # Ferme le curseur qui est l'objet facilitant la connexion à PostgreSQL.
conn.close() # Ferme la connexion à PostgreSQL.
print("✅ Connexion PostgreSQL fermée.")

