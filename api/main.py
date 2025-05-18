# Import du framework FastAPI
from fastapi import FastAPI

# Import de pandas pour charger et manipuler les données
import pandas as pd

# Le chemin d'accès de l'API pour extraire les données
url = "http://localhost:8500/customers"

# Initialisation de l'application FastAPI
app = FastAPI()

# Chargement du fichier JSON contenant les données clients
df = pd.read_json("data/customers.json")

# Chargement des paiements depuis le fichier JSON
payments_df = pd.read_json("data/payments.json")

# Définition de la route principale (homepage de l'API)
@app.get("/")
def home():
    # Retourne un message simple pour vérifier que l'API fonctionne
    return {"message": "API telco Portfolio"}

# Définition de l'endpoint GET /customers
@app.get("/customers")
def get_customers():
    # Retourne tous les clients au format liste de dictionnaires JSON
    return df.to_dict(orient="records")

# Définition de l'endpoint GET /customers/{customer_id}
@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    # Filtrage du DataFrame pour trouver le client correspondant à l'ID
    customer = df[df["customerID"] == customer_id]
    # Si aucun client ne correspond
    if customer.empty:
        return {"error": "Customer not found"}
    # Sinon, retourne le client trouvé sous forme de dictionnaire
    return customer.to_dict(orient="records")[0]

@app.get("/payments")
def get_payments():
    return payments_df.to_dict(orient="records")
