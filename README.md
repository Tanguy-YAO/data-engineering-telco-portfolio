# 📊 Telco Customer Churn – Data Engineering Portfolio

Projet de Data Engineering complet simulant le suivi de clients et de paiements
dans un contexte de résiliation client (churn) dans le secteur des télécoms.

Ce projet inclut : API FastAPI, ETL Python, stockage PostgreSQL et visualisation via Metabase.


## 🚀 Architecture du pipeline
API FastAPI → Scripts ETL Python → Base PostgreSQL → Tableaux de bord Metabase

## 📂 Contenu du projet

| Dossier/Fichier      | Description                                               |
|----------------------|-----------------------------------------------------------|
| `api/`               | API FastAPI simulant les endpoints clients et paiements   |
| `etl/`               | Scripts Python d'extraction, transformation, chargement   |
| `data/`              | Données clients et paiements simulées au format JSON      |
| `sql/`               | Scripts SQL pour créer les tables PostgreSQL              |
| `.env.example`       | Fichier modèle pour les variables d'environnement         |
| `requirements.txt`   | Liste des bibliothèques Python nécessaires                |
| `README.md`          | Le fichier de documentation                               |


## 🛠️ Technologies utilisées

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23336791.svg?logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Metabase](https://img.shields.io/badge/Metabase-0063F7?logo=metabase&logoColor=white)
![ETL](https://img.shields.io/badge/ETL%20Pipeline-Automated-success)

![Architecture Diagram](docs/architecture.png)


## ▶️ Exécuter ce projet localement

### 1. Cloner le dépôt
```
git clone https://github.com/Tanguy-YAO/data-engineering-telco-portfolio.git
cd data-engineering-telco-portfolio
```

### 2. Créer et activer l'environnement virtuel (Windows)
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Installer les dépendances
```
pip install -r requirements.txt
```

### 4. Lancer l'API FastAPI
```
uvicorn api.main:app --reload --port 8500
```

### 5. Exécuter les scripts ETL
```
python etl/customers.py
python etl/generate_payments.py
python etl/payments.py
```

## 👤 Auteur

Tanguy Boris YAO
Business Intelligence Manager - Passionné de Data Engineering

- 🧑‍💻 🧑‍💻 GitHub : [@Tanguy-YAO](https://github.com/Tanguy-YAO)
-  LinkedIn : [linkedin.com/in/tanguy-boris-romuald-yao-567a66169](https://www.linkedin.com/in/tanguy-boris-romuald-yao-567a66169/)
- 📧 Email : tanguyboris.yao@gmail.com

## 🧪 Tests & validation

Ce projet étant un pipeline de données, la validation repose sur :

### Tests manuels via Swagger UI pour s'assurer que les endpoints API répondent correctement :
- GET /customers retourne tous les clients simulés
- GET /customers/{customer_id} retourne un client spécifique
- GET /payments retourne tous les paiements associés

### Vérification des données dans PostgreSQL :
- Les données clients et paiements sont insérées ou mises à jour avec succès
- Les relations entre clients et paiements sont cohérentes

### Validation visuelle via Metabase :
- Les dashboards s'affichent correctement avec les bonnes jointures
- Les KPIs sont alignés avec les données brutes et simulées
