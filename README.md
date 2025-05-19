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

![image](https://github.com/user-attachments/assets/7f1c76ff-43dd-4904-9ddb-6de43ace8009)

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

## Dashboard interactif dans Metabase
- Suivi du churn rate global
- Répartition des contrats et statuts de paiement
- Revenus collectés par mois
- Analyse croisée entre churn et services internet.

_📸Voir ci-dessous un aperçu du tableau de bord construit dans Metabase:_
![image](https://github.com/user-attachments/assets/189319e8-a235-4b00-9083-71e824d04b46)


## 🧠 Conclusion & Perspectives

Ce projet fait la simulation d'un cas pratique et concret de suivi de la réiliation client dans le secteur des télécommunications. Il démontre parfaitement l'intégration complète d'un pipeline Data Engineering, de l'API à la visualisation décisionnelle via Metabase.

## Compétences développées
- Construction d'une API avec FastAPI
- Scripts ETL Python bien structurés et automatisables
- Stockage structuré des données dans une base de données PostgreSQL
- Création de dashboards dynamiques avec Metabase
- Utilisation de GitHub pour le versioning et la documentation

## Prochaines étapes / Pistes d'amélioration
- Orchestration de l'ETL avec Apchache Airflow
- Passer à une architecture cloud-native
- Prédiction du churn

