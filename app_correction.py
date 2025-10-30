import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import networkx as nx

import requests
import pandas as pd
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Big Data MBA Complet",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# DONNÉES ET FONCTIONS DE BASE
# =============================================================================

def generer_donnees_big_data():
    """Génère un dataset complet pour les démonstrations"""
    np.random.seed(42)
    
    # Données pour les 5V
    dates = pd.date_range('2023-01-01', '2024-01-01', freq='D')
    sectors = ['Retail', 'Finance', 'Santé', 'Telecom', 'Transport', 'Énergie']
    regions = ['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor']
    
    data = []
    for date in dates[:100]:  # Volume réduit pour la démo
        for sector in sectors:
            for region in regions:
                data.append({
                    'date': date,
                    'secteur': sector,
                    'region': region,
                    'volume_data': np.random.randint(1000, 100000),
                    'vitesse_traitement': np.random.randint(1, 1000),
                    'transactions': np.random.randint(100, 10000),
                    'erreurs': np.random.randint(0, 50),
                    'revenus': np.random.randint(5000, 500000),
                    'clients': np.random.randint(10, 1000)
                })
    
    return pd.DataFrame(data)

def calculer_metrics_5v(df):
    """Calcule les métriques des 5V"""
    metrics = {
        'Volume': df['volume_data'].sum(),
        'Vélocité': df['vitesse_traitement'].mean(),
        'Variété': len(df['secteur'].unique()),
        'Véracité': (1 - (df['erreurs'].sum() / df['transactions'].sum())) * 100,
        'Valeur': df['revenus'].sum() / df['volume_data'].sum() * 1000
    }
    return metrics

def generer_donnees_retail():
    """Génère des données réalistes pour le retail"""
    np.random.seed(42)
    
    # Données clients
    n_clients = 1000
    data = {
        'client_id': range(1, n_clients + 1),
        'age': np.random.randint(18, 70, n_clients),
        'revenu_annuel': np.random.normal(50000, 20000, n_clients),
        'anciennete_mois': np.random.randint(1, 60, n_clients),
        'frequence_achats': np.random.poisson(5, n_clients),
        'panier_moyen': np.random.normal(85, 30, n_clients),
        'satisfaction': np.random.randint(1, 10, n_clients),
        'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor'], n_clients),
        'segment': np.random.choice(['Occasionnel', 'Régulier', 'Fidèle', 'VIP'], n_clients, p=[0.4, 0.3, 0.2, 0.1])
    }
    
    df_clients = pd.DataFrame(data)
    df_clients['revenu_annuel'] = df_clients['revenu_annuel'].clip(20000, 150000)
    df_clients['panier_moyen'] = df_clients['panier_moyen'].clip(20, 200)
    
    # Données transactions
    transactions = []
    for client_id in range(1, n_clients + 1):
        n_transactions = np.random.poisson(df_clients.loc[client_id-1, 'frequence_achats'])
        for _ in range(n_transactions):
            transactions.append({
                'client_id': client_id,
                'date': datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)),
                'montant': np.random.normal(df_clients.loc[client_id-1, 'panier_moyen'], 20),
                'categorie': np.random.choice(['Électronique', 'Vêtements', 'Alimentation', 'Maison', 'Loisirs']),
                'canal': np.random.choice(['Online', 'Magasin', 'Mobile'], p=[0.6, 0.3, 0.1])
            })
    
    df_transactions = pd.DataFrame(transactions)
    df_transactions['montant'] = df_transactions['montant'].clip(10, 500)
    
    return df_clients, df_transactions

def generer_donnees_qualite():
    """Génère des données avec problèmes de qualité"""
    np.random.seed(123)
    
    data = {
        'id': range(1, 101),
        'nom': [f'Client_{i}' for i in range(1, 101)],
        'email': [f'client{i}@example.com' if np.random.random() > 0.1 else '' for i in range(1, 101)],
        'telephone': [f'77{np.random.randint(100, 999)}{np.random.randint(1000, 9999)}' if np.random.random() > 0.15 else '' for _ in range(100)],
        'age': [np.random.randint(18, 70) if np.random.random() > 0.05 else np.random.randint(200, 300) for _ in range(100)],
        'salaire': [np.random.normal(50000, 20000) if np.random.random() > 0.08 else -1 for _ in range(100)],
        'ville': [np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', '']) if np.random.random() > 0.07 else '' for _ in range(100)],
        'date_inscription': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(100)]
    }
    
    return pd.DataFrame(data)

# =============================================================================
# SECTION 1: INTRODUCTION AU BIG DATA
# =============================================================================

def section_introduction():
    st.header("🌍 Introduction au Big Data")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Définition Complète du Big Data
        
        Le **Big Data** (Mégadonnées en français) désigne des **volumes massifs de données** 
        si grands et complexes qu'ils ne peuvent pas être traités avec les outils traditionnels.
        
        Le **Big Data** représente l'ensemble des données dont le **volume**, la **vélocité** et la **variété** 
        nécessitent des technologies et méthodes analytiques spécifiques pour en extraire de la valeur.

        ### 📖 Analogie Simple
        **Imaginez :**
        - 🏢 **Données traditionnelles** = Une bibliothèque
        - 🌊 **Big Data** = Tous les océans du monde
        
        On passe d'une gestion manuelle à une gestion industrielle des données !

        #### Évolution du Concept
        - **Années 2000** : Emergence des 3V (Volume, Vélocité, Variété)
        - **Années 2010** : Ajout de la Véracité et de la Valeur
        - **Aujourd'hui** : Intégration de l'IA et du Cloud Computing
        """)
    
    with col2:
        st.image("https://via.placeholder.com/300x200/4C78A8/FFFFFF?text=Big+Data+Ecosystem", 
                caption="Écosystème Big Data Moderne")
    
    # Ajouter un séparateur avant les 5V
    st.markdown("---")
    
    # Maintenant afficher les 5V du Big Data
    st.subheader("📊 Les 5V du Big Data : Définitions Détaillées")

    # Définitions des 5V
    v_definitions = {
        "📦 Volume": {
            "definition": "Quantité massive de données générées, souvent en téraoctets ou pétaoctets",
            "exemple": "**Walmart** traite 2.5+ pétaoctets/heure de données de caisse",
            "defi": "Stockage et traitement distribué",
            "details": """
            - **Énormes quantités** de données générées
            - **Exemples :** 
              - 500 millions de tweets par jour
              - 4,2 milliards de vidéos YouTube vues quotidiennement
              - 3,5 milliards de recherches Google par jour
            - **Chiffre clé :** 2,5 trillions d'octets créés chaque jour
            """
        },
        "⚡ Vélocité": {
            "definition": "Vitesse de génération, collecte et traitement des données",
            "exemple": "**Visa** analyse des milliards de transactions en temps réel",
            "defi": "Traitement en temps réel",
            "details": """
            - **Vitesse** à laquelle les données sont générées et traitées
            - **Temps réel** ou quasi réel
            - **Exemple :** 
              - Transactions boursières (microsecondes)
              - Capteurs IoT (flux continu)
              - Réseaux sociaux (données streaming)
            """
        },
        "🎭 Variété": {
            "definition": "Diversité des formats : structuré, semi-structuré, non structuré",
            "exemple": "**Netflix** combine données d'abonnement et de visionnage",
            "defi": "Intégration multi-sources",
            "details": """
            - **Divers formats** de données :
              - **Structurées** : Bases de données SQL
              - **Semi-structurées** : JSON, XML
              - **Non structurées** : Textes, images, vidéos, audio
            - **Exemple :** Données GPS, emails, photos, vidéos surveillance
            """
        },
        "✅ Véracité": {
            "definition": "Qualité, fiabilité et exactitude des données",
            "exemple": "Nettoyage des logs de clics pour analyse comportementale",
            "defi": "Gouvernance et qualité",
            "details": """
            - **Fiabilité et qualité** des données
            - Nettoyage et validation nécessaire
            - **Exemple :** 
              - Données erronées ou incomplètes
              - Fake news sur les réseaux
              - Données bruitées des capteurs
            """
        },
        "💰 Valeur": {
            "definition": "Bénéfice métier concret extrait des données",
            "exemple": "Campagne marketing ciblée boostant les profits de 25%",
            "defi": "ROI et alignement métier",
            "details": """
            - **Utilité business** extraite des données
            - Insights et décisions stratégiques
            - **Objectif :** Transformer les données en valeur
            - **Exemple :** Recommandations Amazon, prédictions météo
            """
        }
    }

    # Affichage avec boucle
    for i, (v, details) in enumerate(v_definitions.items(), 1):
        with st.expander(f"### {i}. {v}", expanded=(i == 1)):
            st.markdown(f"**📖 Définition :** {details['definition']}")
            st.markdown(f"**🏢 Cas pratique :** {details['exemple']}")
            st.markdown(f"**⚡ Défi :** {details['defi']}")
            st.markdown("---")
            st.markdown("**📋 Détails complémentaires :**")
            st.markdown(details['details'])


# ====================================================
# SECTION 2: TECHNOLOGIES ET ARCHITECTURES - CORRIGÉE ET COMPLÉTÉE
# =============================================================================

def section_technologies():
    st.header("🛠️ Technologies et Architectures Big Data")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏗️ Architecture", "💾 Stockage", "⚙️ Processing", "🔗 Intégration"
    ])
    
    with tab1:
        st.subheader("Architectures de Référence")
        
        architectures = {
            "Lambda Architecture": {
                "description": "Combine traitement batch et stream processing pour équilibrer latence et précision",
                "composants": ["Batch Layer (Hadoop)", "Speed Layer (Storm/Flink)", "Serving Layer (Cassandra)"],
                "use_case": "Systèmes nécessitant faible latence et précision historique",
                "avantages": ["Tolérance aux pannes", "Scalabilité horizontale", "Données immuables"],
                "inconvenients": ["Complexité de maintenance", "Double logique de traitement"]
            },
            "Kappa Architecture": {
                "description": "Simplification de Lambda avec uniquement du stream processing",
                "composants": ["Stream Processing uniquement (Kafka Streams)"],
                "use_case": "Applications temps réel modernes avec replay des données",
                "avantages": ["Simplicité architecturale", "Traitement temps réel unique", "Reprocessing facile"],
                "inconvenients": ["Dépendance forte à Kafka", "Complexité des requêtes historiques"]
            },
            "Data Mesh": {
                "description": "Approche décentralisée et orientée domaine pour les données à grande échelle",
                "composants": ["Domain-oriented Data", "Self-serve Platform", "Federated Governance"],
                "use_case": "Grandes organisations complexes avec multiples domaines métier",
                "avantages": ["Scalabilité organisationnelle", "Autonomie des équipes", "Meilleure qualité des données"],
                "inconvenients": ["Changement culturel important", "Complexité de gouvernance"]
            }
        }
        
        selected_arch = st.selectbox("Choisir une architecture:", list(architectures.keys()))
        
        if selected_arch:
            arch = architectures[selected_arch]
            st.write(f"**Description :** {arch['description']}")
            st.write(f"**Composants :** {', '.join(arch['composants'])}")
            st.write(f"**Cas d'usage :** {arch['use_case']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**✅ Avantages:**")
                for avantage in arch['avantages']:
                    st.write(f"- {avantage}")
            with col2:
                st.write("**❌ Inconvénients:**")
                for inconvenient in arch['inconvenients']:
                    st.write(f"- {inconvenient}")
            
            # Diagramme d'architecture simplifié
            if selected_arch == "Lambda Architecture":
                st.subheader("📊 Flux de Données Lambda")
                st.image("https://via.placeholder.com/600x300/4C78A8/FFFFFF?text=Lambda+Architecture", 
                        caption="Batch Layer + Speed Layer + Serving Layer")
            
            elif selected_arch == "Kappa Architecture":
                st.subheader("📊 Flux de Données Kappa")
                st.image("https://via.placeholder.com/600x200/FF6B6B/FFFFFF?text=Kappa+Architecture", 
                        caption="Single Stream Processing Pipeline")
    
    with tab2:
        st.subheader("Solutions de Stockage")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Data Lake vs Data Warehouse
            
            | Caractéristique | Data Lake | Data Warehouse |
            |----------------|-----------|----------------|
            | **Données** | Brutes, tous formats | Transformées, structurées |
            | **Schema** | On-read (flexible) | On-write (rigide) |
            | **Utilisateurs** | Data Scientists | Analystes métier |
            | **Coût** | Faible (object storage) | Élevé (compute+storage) |
            | **Performance** | Exploration | Reporting/BI |
            | **Governance** | Complexe | Structurée |
            """)
            
            st.markdown("""
            #### Cas d'Usage Recommandés
            
            **Data Lake:**
            - Exploration de données brutes
            - Machine Learning
            - Données IoT/sensors
            - Logs et événements
            
            **Data Warehouse:**
            - Reporting opérationnel
            - Tableaux de bord BI
            - Analytics métier
            - Conformité réglementaire
            """)
        
        with col2:
            st.markdown("""
            #### Technologies Populaires
            
            **Data Lakes:**
            - 🟠 **Amazon S3** - Stockage objet scalable
            - 🔵 **Azure Data Lake** - Intégration Microsoft
            - 🟢 **Hadoop HDFS** - On-premise
            - 🟣 **Google Cloud Storage** - GCP ecosystem
            
            **Data Warehouses:**
            - ❄️ **Snowflake** - Architecture cloud-native
            - 🔍 **BigQuery** - Serverless, forte intégration GCP
            - 🔴 **Redshift** - Optimisé pour AWS
            - 🟡 **Azure Synapse** - Suite analytics Microsoft
            
            **Hybrides (Lakehouse):**
            - ⚡ **Databricks Delta Lake** - ACID sur data lake
            - 🔷 **Azure Synapse** - Lake + Warehouse intégrés
            - 🟤 **Apache Hudi** - Tables transactionnelles
            """)
            
            # Comparaison de coûts
            st.subheader("💰 Comparaison de Coûts (Estimation)")
            cout_data = {
                'Solution': ['S3 + Athena', 'BigQuery', 'Snowflake', 'Redshift'],
                'Stockage (€/To/mois)': [20, 25, 30, 35],
                'Compute (€/heure)': [5, 8, 12, 10],
                'Performance': [3, 5, 4, 4]
            }
            df_cout = pd.DataFrame(cout_data)
            st.dataframe(df_cout.style.background_gradient(subset=['Stockage (€/To/mois)', 'Compute (€/heure)']))
    
    with tab3:
        st.subheader("Frameworks de Processing")
        
        processing_frameworks = {
            "Apache Spark": {
                "type": "Traitement distribué en mémoire",
                "use_cases": ["ETL à grande échelle", "Machine Learning", "Analytics interactif", "Streaming"],
                "langages": ["Python", "Scala", "Java", "R", "SQL"],
                "performance": "⭐⭐⭐⭐⭐",
                "maturite": "⭐⭐⭐⭐⭐",
                "exemple": "Netflix - Traitement de 500B événements/jour"
            },
            "Apache Flink": {
                "type": "Stream Processing temps réel",
                "use_cases": ["CEP (Complex Event Processing)", "Analytics temps réel", "Détection fraude", "IoT"],
                "langages": ["Java", "Scala", "Python"],
                "performance": "⭐⭐⭐⭐⭐",
                "maturite": "⭐⭐⭐⭐",
                "exemple": "Uber - Optimisation des trajets en temps réel"
            },
            "Apache Kafka": {
                "type": "Message Streaming & Event Streaming",
                "use_cases": ["Data Pipelines", "Event Sourcing", "Microservices", "Log aggregation"],
                "langages": ["Java", "Scala", "Python", "Go"],
                "performance": "⭐⭐⭐⭐⭐",
                "maturite": "⭐⭐⭐⭐⭐",
                "exemple": "LinkedIn - 7Tb+/jour, 4M+ messages/sec"
            },
            "Apache Beam": {
                "type": "Processing unifié (batch + stream)",
                "use_cases": ["Pipelines portables", "Traitement unifié", "Multi-cloud"],
                "langages": ["Java", "Python", "Go"],
                "performance": "⭐⭐⭐",
                "maturite": "⭐⭐⭐",
                "exemple": "Spotify - Recommandations musicales"
            }
        }
        
        selected_framework = st.selectbox("Choisir un framework:", list(processing_frameworks.keys()))
        
        if selected_framework:
            framework = processing_frameworks[selected_framework]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Type :** {framework['type']}")
                st.write(f"**Performance :** {framework['performance']}")
                st.write(f"**Maturité :** {framework['maturite']}")
                st.write(f"**Exemple réel :** {framework['exemple']}")
                
                st.write("**Cas d'usage principaux:**")
                for use_case in framework['use_cases']:
                    st.write(f"- {use_case}")
            
            with col2:
                st.write("**Langages supportés:**")
                for langage in framework['langages']:
                    st.write(f"- {langage}")
                
                # Métriques de performance simulées
                if selected_framework == "Apache Spark":
                    st.metric("Throughput", "100+ Go/sec")
                    st.metric("Latence", "1-10 sec")
                    st.metric("Scalabilité", "1000+ nœuds")
                elif selected_framework == "Apache Flink":
                    st.metric("Latence", "< 100 ms")
                    st.metric("Checkpointing", "Exactly-once")
                    st.metric("Backpressure", "Gestion automatique")
                elif selected_framework == "Apache Kafka":
                    st.metric("Throughput", "1M+ msg/sec")
                    st.metric("Latence", "< 10 ms")
                    st.metric("Durabilité", "Persistent")
            
            # Exemple de code
            st.subheader("💻 Exemple de Code")
            
            if selected_framework == "Apache Spark":
                code = """
# Lecture de données
df = spark.read.parquet("s3://data-lake/raw/")
 
# Transformation
result = df.filter(df.age > 18) \\
           .groupBy("department") \\
           .agg(avg("salary").alias("avg_salary"))
 
# Écriture
result.write.parquet("s3://data-lake/processed/")
                """
                st.code(code, language='python')
            
            elif selected_framework == "Apache Flink":
                code = """
// Stream processing temps réel
DataStream<Transaction> transactions = env
    .addSource(new TransactionSource())
    .keyBy(Transaction::getAccountId)
    .window(TumblingEventTimeWindows.of(Time.minutes(5)))
    .process(new FraudDetectionProcessFunction());
                """
                st.code(code, language='java')
    
    with tab4:
        st.subheader("🔗 Intégration de Données et Data Pipelines")
        
        st.markdown("""
        ### Architecture d'Intégration Moderne
        
        L'intégration de données connecte les sources disparates et assure la circulation 
        des données dans l'écosystème Big Data.
        """)
        
        integration_type = st.selectbox(
            "Type d'intégration:",
            ["ETL/ELT", "CDC (Change Data Capture)", "API Integration", "Data Virtualization", "Data Replication"]
        )
        
        if integration_type == "ETL/ELT":
            st.success("**🔄 ETL (Extract-Transform-Load) vs ELT (Extract-Load-Transform)**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                #### ETL Traditionnel
                **Processus:**
                1. **Extract** - Sources bases de données
                2. **Transform** - Serveur ETL dédié
                3. **Load** - Data Warehouse
                
                **Avantages:**
                - Données propres chargées
                - Performance DW optimisée
                - Contrôle qualité strict
                
                **Outils:**
                - Informatica PowerCenter
                - IBM DataStage
                - Talend
                - SSIS
                """)
            
            with col2:
                st.markdown("""
                #### ELT Moderne
                **Processus:**
                1. **Extract** - Sources variées
                2. **Load** - Data Lake brut
                3. **Transform** - Dans le cloud
                
                **Avantages:**
                - Flexibilité des transformations
                - Conservation données brutes
                - Scalabilité cloud
                
                **Outils:**
                - Matillion
                - dbt (Data Build Tool)
                - Fivetran
                - Stitch Data
                """)
            
            # Comparaison ETL vs ELT
            st.subheader("📊 Comparaison ETL vs ELT")
            
            comparison_data = {
                'Aspect': ['Latence', 'Flexibilité', 'Coût', 'Compétences requises', 'Cas d usage'],
                'ETL': ['Heures-jours', 'Limitée', 'Élevé (serveurs dédiés)', 'Spécialisés ETL', 'Data Warehouse traditionnel'],
                'ELT': ['Minutes-heures', 'Élevée', 'Variable (cloud)', 'SQL + Scripting', 'Data Lake moderne']
            }
            
            df_comparison = pd.DataFrame(comparison_data)
            st.dataframe(df_comparison)
            
            # Exemple de pipeline ELT moderne
            st.subheader("🚀 Exemple de Pipeline ELT avec dbt + Snowflake")
            
            code = """
-- models/mart/daily_sales.sql
{{ config(materialized='table') }}

WITH raw_sales AS (
    SELECT * FROM {{ source('raw', 'sales') }}
),

cleaned_sales AS (
    SELECT
        order_id,
        customer_id,
        product_id,
        amount,
        order_date,
        -- Nettoyage des données
        CASE 
            WHEN amount < 0 THEN 0 
            ELSE amount 
        END as cleaned_amount
    FROM raw_sales
    WHERE order_date >= '2024-01-01'
)

SELECT
    DATE_TRUNC('day', order_date) as sales_date,
    customer_id,
    SUM(cleaned_amount) as daily_revenue,
    COUNT(*) as number_orders
FROM cleaned_sales
GROUP BY 1, 2
            """
            st.code(code, language='sql')
            
            st.write("**Avantages de cette approche:**")
            st.write("- ✅ Versioning des transformations avec Git")
            st.write("- ✅ Tests de qualité des données intégrés")
            st.write("- ✅ Documentation automatique")
            st.write("- ✅ Lineage des données traçable")
        
        elif integration_type == "CDC (Change Data Capture)":
            st.info("**🔄 CDC - Capture des Changements en Temps Réel**")
            
            st.markdown("""
            ### Principe du CDC
            
            Capture des modifications des bases de données sources en temps réel 
            sans impact sur les performances.
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Méthodes CDC:**
                
                **1. Log-Based CDC**
                - Lecture des logs de transaction
                - Performances optimales
                - Exemple: Debezium, Oracle GoldenGate
                
                **2. Trigger-Based CDC**  
                - Déclencheurs sur les tables
                - Impact sur la source
                - Exemple: Custom triggers
                
                **3. Query-Based CDC**
                - Polling régulier avec timestamps
                - Simple à implémenter
                - Latence plus élevée
                """)
            
            with col2:
                st.markdown("""
                **Cas d'Usage:**
                
                - 🏦 **Réplication base de données** - Synchronisation cross-DC
                - 📊 **Data Warehouse temps réel** - Màj continue
                - 🔍 **Search Indexing** - Indexation recherche
                - 🚨 **Fraud Detection** - Surveillance transactions
                - 📱 **Caching** - Invalidation caches
                """)
                
                # Métriques CDC
                st.metric("Latence typique", "< 1 seconde")
                st.metric("Throughput", "10K+ events/sec")
                st.metric("Impact source", "Négligeable")
            
            # Architecture CDC avec Debezium + Kafka
            st.subheader("🏗️ Architecture CDC avec Debezium + Kafka")
            
            st.image("https://via.placeholder.com/700x300/2E8B57/FFFFFF?text=Debezium+%2B+Kafka+CDC+Pipeline", 
                    caption="Source DB → Debezium → Kafka → Data Lake / Data Warehouse")
            
            # Exemple de configuration Debezium
            st.subheader("⚙️ Configuration Debezium")
            
            code = """
# connector-config.json
{
  "name": "inventory-connector",
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "database.hostname": "mysql",
    "database.port": "3306",
    "database.user": "debezium",
    "database.password": "dbz",
    "database.server.id": "184054",
    "database.server.name": "dbserver1",
    "database.include.list": "inventory",
    "table.include.list": "inventory.orders,inventory.customers",
    "database.history.kafka.bootstrap.servers": "kafka:9092",
    "database.history.kafka.topic": "dbhistory.inventory",
    "include.schema.changes": "true"
  }
}
            """
            st.code(code, language='json')
            
            st.write("**Flux de données capturées:**")
            st.write("- INSERT → Nouveaux enregistrements")
            st.write("- UPDATE → Anciennes et nouvelles valeurs")
            st.write("- DELETE → Enregistrements supprimés")
        
        elif integration_type == "API Integration":
            st.warning("**🌐 Intégration par APIs RESTful**")
            
            st.markdown("""
            ### Intégration de Données via APIs
            
            Connexion à des sources externes via des APIs REST, GraphQL, SOAP.
            """)
            
            # Patterns d'intégration API
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Patterns Courants:**
                
                **1. API Polling**
                - Requêtes régulières
                - Simple à implémenter
                - Latence variable
                
                **2. Webhooks**
                - Notifications push
                - Temps réel
                - Complexité côté source
                
                **3. GraphQL**
                - Requêtes spécifiques
                - Réduction over-fetching
                - Courbe d'apprentissage
                """)
            
            with col2:
                st.markdown("""
                **Outils d'Orchestration:**
                
                - **Apache NiFi** - Flow-based programming
                - **Airbyte** - Connectors pré-built
                - **MuleSoft** - Platform enterprise
                - **Zapier** - No-code integration
                - **Custom Scripts** - Python, Node.js
                """)
                
                # Statistiques APIs
                st.metric("APIs disponibles", "50,000+")
                st.metric("Croissance marché", "+25%/an")
                st.metric("Données via APIs", "60% des entreprises")
            
            # Exemple d'intégration API avec Python
            st.subheader("🐍 Exemple d'Intégration API avec Python")
            
            code = """
import requests
import pandas as pd
from datetime import datetime, timedelta

class SalesforceAPI:
    def __init__(self, client_id, client_secret):
        self.base_url = "https://yourinstance.salesforce.com"
        self.access_token = self.authenticate(client_id, client_secret)
    
    def authenticate(self, client_id, client_secret):
        # OAuth2 authentication
        auth_url = f"{self.base_url}/services/oauth2/token"
        response = requests.post(auth_url, data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        })
        return response.json()['access_token']
    
    def extract_opportunities(self, start_date):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        query = f'''
        SELECT Id, Name, Amount, CloseDate, StageName 
        FROM Opportunity 
        WHERE CloseDate >= {start_date}
        '''
        
        response = requests.get(
            f"{self.base_url}/services/data/v52.0/query",
            headers=headers,
            params={'q': query}
        )
        
        return pd.DataFrame(response.json()['records'])

# Utilisation
sf = SalesforceAPI("your-client-id", "your-client-secret")
opportunities = sf.extract_opportunities("2024-01-01")
            """
            st.code(code, language='python')
            
            # Bonnes pratiques
            st.subheader("🔧 Bonnes Pratiques API Integration")
            
            practices = {
                "Rate Limiting": "Implémenter des retry avec backoff exponentiel",
                "Error Handling": "Gérer les timeouts et erreurs HTTP",
                "Monitoring": "Tracker les quotas et latences",
                "Security": "Utiliser OAuth2, stocker secrets sécuriséments",
                "Idempotence": "Assurer le re-processing sans duplication"
            }
            
            for practice, description in practices.items():
                with st.expander(f"✅ {practice}"):
                    st.write(description)
        
        elif integration_type == "Data Virtualization":
            st.error("**🔮 Virtualisation des Données**")
            
            st.markdown("""
            ### Accès Unifié sans Réplication
            
            Fournit une vue unifiée des données sans les déplacer physiquement.
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Avantages:**
                - 🚀 **Time-to-value rapide** - Pas d'ETL nécessaire
                - 💰 **Coûts réduits** - Pas de stockage supplémentaire
                - 🔒 **Governance centralisée** - Contrôle d'accès unique
                - 📊 **Vue unifiée** - Multi-sources transparent
                
                **Inconvénients:**
                - ⚠️ **Performance** - Dépend des sources
                - 🔧 **Complexité** - Optimisation des requêtes
                - 💸 **Coûts licences** - Outils spécialisés
                """)
            
            with col2:
                st.markdown("""
                **Outils:**
                - **Denodo** - Leader du marché
                - **Dremio** - Open source friendly
                - **Starburst** - Basé sur Trino
                - **CData** - Connecteurs étendus
                
                **Cas d'Usage:**
                - 🔍 **Data Discovery** - Exploration sans ETL
                - 📈 **Reporting ad-hoc** - Requêtes cross-sources
                - 🏦 **Compliance** - Vue 360° réglementaire
                - 🔗 **API Data Services** - Exposition données
                """)
            
            # Architecture Data Virtualization
            st.subheader("🏗️ Architecture de Virtualisation")
            
            st.image("https://via.placeholder.com/600x400/8B4513/FFFFFF?text=Data+Virtualization+Layer", 
                    caption="Sources multiples → Virtualization Layer → Consommateurs")
            
            # Exemple de requête virtualisée
            st.subheader("💻 Exemple de Requête Virtualisée")
            
            code = """
-- Requête unifiant données Salesforce, MySQL et S3
SELECT 
    c.company_name,
    o.opportunity_amount,
    s.sentiment_score,
    DATE(o.created_date) as opportunity_date
FROM salesforce.opportunities o
JOIN mysql.customers c ON o.customer_id = c.id
LEFT JOIN s3.customer_feedback s ON c.email = s.customer_email
WHERE o.created_date >= '2024-01-01'
  AND o.status = 'Closed Won'
ORDER BY o.opportunity_amount DESC
LIMIT 100;
            """
            st.code(code, language='sql')
            
            st.write("**Bénéfices de cette approche:**")
            st.write("- ✅ Pas de mouvement de données")
            st.write("- ✅ Données toujours à jour")
            st.write("- ✅ Vue business unifiée")
            st.write("- ✅ Réduction time-to-insight")
        
        elif integration_type == "Data Replication":
            st.success("**📋 Réplication de Données**")
            
            st.markdown("""
            ### Synchronisation des Données entre Systèmes
            
            Copie et synchronisation des données entre différentes bases et systèmes.
            """)
            
            # Types de réplication
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Types de Réplication:**
                
                **1. Snapshot Replication**
                - Copie complète périodique
                - Simple mais lourd
                - Pour données petites/moyennes
                
                **2. Transactional Replication**
                - Propagation des transactions
                - Faible latence
                - Pour synchronisation temps réel
                
                **3. Merge Replication**
                - Bidirectionnel
                - Résolution conflits
                - Pour applications distribuées
                """)
            
            with col2:
                st.markdown("""
                **Outils Spécialisés:**
                
                - **AWS DMS** - Database Migration Service
                - **Azure Data Factory** - Copy activities
                - **Google Dataflow** - Streaming replication
                - **Confluent** - Kafka-based replication
                - **Striim** - Real-time data integration
                """)
                
                # Métriques réplication
                st.metric("Latence cible", "< 1 minute")
                st.metric("RTO (Recovery Time)", "Quelques minutes")
                st.metric("RPO (Recovery Point)", "Quelques secondes")
            
            # Exemple AWS DMS
            st.subheader("☁️ Exemple AWS Database Migration Service")
            
            code = """
# Configuration de tâche DMS avec CloudFormation
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  ReplicationTask:
    Type: AWS::DMS::ReplicationTask
    Properties:
      ReplicationTaskIdentifier: "mysql-to-redshift"
      SourceEndpointArn: !Ref SourceEndpoint
      TargetEndpointArn: !Ref TargetEndpoint
      ReplicationInstanceArn: !Ref ReplicationInstance
      MigrationType: "full-load-and-cdc"
      TableMappings: |
        {
          "rules": [
            {
              "rule-type": "selection",
              "rule-id": "1",
              "rule-name": "1",
              "object-locator": {
                "schema-name": "ecommerce",
                "table-name": "%"
              },
              "rule-action": "include"
            }
          ]
        }
            """
            st.code(code, language='yaml')
            
            # Cas d'usage réplication
            st.subheader("🎯 Cas d'Usage Typiques")
            
            use_cases = {
                "🏢 **Migration Cloud**": "Transfert on-premise → cloud",
                "🔄 **Disaster Recovery**": "Réplication cross-region",
                "📊 **Analytics Separation**": "Copie prod → analytics",
                "🌍 **Global Applications**": "Synchronisation multi-regions"
            }
            
            for use_case, description in use_cases.items():
                st.write(f"{use_case}: {description}")
        
             # Tableau comparatif général - AVEC INDICATEURS VISUELS
        st.subheader("📊 Comparatif des Méthodes d'Intégration")
        
        # Créer des indicateurs visuels
        comparison_data = {
            'Méthode': ['ETL/ELT', 'CDC', 'API Integration', 'Data Virtualization', 'Data Replication'],
            'Latence': ['🔴 Heures', '🟢 Secondes', '🟡 Minutes', '🟢 Secondes', '🟡 Minutes'],
            'Complexité': ['🔴 Élevée', '🟢 Moyenne', '🟡 Variable', '🔴 Élevée', '🟢 Moyenne'],
            'Coût': ['🔴 Élevé', '🟢 Moyen', '🟡 Variable', '🔴 Élevé', '🟢 Moyen'],
            'Temps Réel': ['🔴 Non', '🟢 Oui', '🟡 Partiel', '🟢 Oui', '🟢 Oui'],
            'Use Case': ['Data Warehousing', 'Temps réel', 'SaaS Integration', 'Vue unifiée', 'Synchronisation']
        }
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison)
        
 

# =============================================================================
# SECTION 3: CAS PRATIQUES PAR SECTEUR
# =============================================================================


def generer_donnees_sante():
    """Génère des données réalistes pour le secteur santé"""
    np.random.seed(42)
    
    # Données patients
    n_patients = 500
    data_patients = {
        'patient_id': range(1, n_patients + 1),
        'age': np.random.randint(18, 90, n_patients),
        'sexe': np.random.choice(['M', 'F'], n_patients),
        'poids': np.random.normal(70, 15, n_patients),
        'taille': np.random.normal(170, 10, n_patients),
        'tension_arterielle': np.random.normal(120, 20, n_patients),
        'cholesterol': np.random.normal(180, 40, n_patients),
        'diabete': np.random.choice([0, 1], n_patients, p=[0.85, 0.15]),
        'fumeur': np.random.choice([0, 1], n_patients, p=[0.7, 0.3]),
        'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor'], n_patients)
    }
    
    df_patients = pd.DataFrame(data_patients)
    df_patients['poids'] = df_patients['poids'].clip(40, 150)
    df_patients['taille'] = df_patients['taille'].clip(150, 200)
    df_patients['tension_arterielle'] = df_patients['tension_arterielle'].clip(80, 200)
    df_patients['cholesterol'] = df_patients['cholesterol'].clip(100, 300)
    
    # Données consultations
    consultations = []
    for patient_id in range(1, n_patients + 1):
        n_consultations = np.random.poisson(3) + 1  # Au moins 1 consultation
        for _ in range(n_consultations):
            consultations.append({
                'patient_id': patient_id,
                'date': datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)),
                'medecin': np.random.choice(['Dr. Diallo', 'Dr. Ndiaye', 'Dr. Sarr', 'Dr. Diop', 'Dr. Fall']),
                'diagnostic_principal': np.random.choice(['Hypertension', 'Diabète', 'Grippe', 'Arthrite', 'Asthme', 'Anxiété', 'Dépression']),
                'duree_minutes': np.random.randint(15, 60),
                'cout': np.random.normal(50, 20),
                'medicaments_prescrits': np.random.randint(0, 5)
            })
    
    df_consultations = pd.DataFrame(consultations)
    df_consultations['cout'] = df_consultations['cout'].clip(20, 150)
    
    return df_patients, df_consultations

def generer_donnees_telecom():
    """Génère des données réalistes pour le secteur télécom"""
    np.random.seed(42)
    
    n_clients = 1000
    data_telecom = {
        'client_id': range(1, n_clients + 1),
        'forfait': np.random.choice(['Basique', 'Standard', 'Premium', 'Illimité'], n_clients, p=[0.3, 0.4, 0.2, 0.1]),
        'anciennete_mois': np.random.randint(1, 60, n_clients),
        'data_utilisee_go': np.random.gamma(2, 10, n_clients),
        'appels_minutes': np.random.gamma(3, 50, n_clients),
        'sms_envoyes': np.random.poisson(30, n_clients),
        'facture_moyenne': np.random.normal(25, 10, n_clients),
        'satisfaction': np.random.randint(1, 11, n_clients),
        'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor'], n_clients),
        'nb_reclamations': np.random.poisson(0.5, n_clients)
    }
    
    df_telecom = pd.DataFrame(data_telecom)
    df_telecom['data_utilisee_go'] = df_telecom['data_utilisee_go'].clip(0, 100)
    df_telecom['appels_minutes'] = df_telecom['appels_minutes'].clip(0, 1000)
    df_telecom['facture_moyenne'] = df_telecom['facture_moyenne'].clip(10, 80)
    df_telecom['nb_reclamations'] = df_telecom['nb_reclamations'].clip(0, 5)
    
    return df_telecom

def section_cas_pratiques():
    st.header("🏢 Cas Pratiques par Secteur d'Activité")
    
    secteur = st.selectbox(
        "Choisir un secteur:",
        ["Commerce & Retail", "Finance & Assurance", "Santé", "Télécom", "Transport & Logistique", "Énergie"]
    )
    
    if secteur == "Commerce & Retail":
        st.subheader("🛒 Commerce & Retail")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Applications Big Data
            
            **1. Recommandation Personnalisée**
            - Analyse comportement client en temps réel
            - Algorithmes de collaborative filtering
            - Boost du panier moyen de 15-30%
            
            **2. Optimisation des Stocks**
            - Prévision demande saisonnière
            - Analyse des tendances ventes
            - Réduction rupture de stock de 40%
            
            **3. Pricing Dynamique**
            - Analyse concurrentielle en temps réel
            - Elasticité prix/demande
            - Maximisation marge de 8-12%
            
            **4. Analyse du Parcours Client**
            - Tracking multi-canal
            - Optimisation de l'expérience client
            - Augmentation conversion de 20-35%
            """)
        
        with col2:
            # Simulation données retail
            df_clients, df_transactions = generer_donnees_retail()
            
            # KPI principaux
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Clients totaux", f"{len(df_clients):,}")
            with col2:
                st.metric("Transactions totales", f"{len(df_transactions):,}")
            with col3:
                st.metric("Panier moyen", f"{df_transactions['montant'].mean():.1f} €")
            
            # Analyse des ventes par catégorie
            ventes_par_categorie = df_transactions.groupby('categorie')['montant'].sum().sort_values(ascending=False)
            fig = px.pie(ventes_par_categorie, values=ventes_par_categorie.values, names=ventes_par_categorie.index,
                        title="Répartition du Chiffre d'Affaires par Catégorie")
            st.plotly_chart(fig, use_container_width=True)
            
            # Performance des canaux de vente
            perf_canal = df_transactions.groupby('canal').agg({
                'montant': ['count', 'mean', 'sum']
            }).round(2)
            perf_canal.columns = ['Nb Transactions', 'Panier Moyen', 'CA Total']
            st.write("**Performance par canal de vente:**")
            st.dataframe(perf_canal)
    
    elif secteur == "Finance & Assurance":
        st.subheader("🏦 Finance & Assurance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Applications Big Data
            
            **1. Détection de Fraude**
            - Analyse patterns transactionnels
            - Machine Learning temps réel
            - Réduction fraude de 60-80%
            
            **2. Scoring Crédit**
            - Analyse comportementale avancée
            - Données alternatives
            - Précision améliorée de 25%
            
            **3. Conformité Réglementaire**
            - Surveillance transactions
            - Reporting automatique
            - Réduction coûts compliance de 40%
            
            **4. Gestion des Risques**
            - Analyse de portefeuille
            - Stress testing
            - Optimisation capital réglementaire
            """)
        
        with col2:
            # Simulation détection fraude
            np.random.seed(42)
            transactions_data = {
                'Heure': list(range(24)) * 30,
                'Montant': np.random.exponential(100, 720),
                'Type': np.random.choice(['Retrait', 'Paiement', 'Virement'], 720, p=[0.3, 0.5, 0.2]),
                'Risque_Fraude': np.random.beta(0.5, 5, 720)
            }
            
            df_transactions = pd.DataFrame(transactions_data)
            df_transactions['Fraude'] = df_transactions['Risque_Fraude'] > 0.8
            
            # Transactions par heure avec détection fraude
            transactions_par_heure = df_transactions.groupby('Heure').agg({
                'Montant': 'count',
                'Fraude': 'sum'
            }).reset_index()
            
            fig = px.line(transactions_par_heure, x='Heure', y=['Montant', 'Fraude'],
                         title="Activité Transactionnelle et Fraudes sur 24h",
                         labels={'value': 'Nombre', 'variable': 'Type'})
            st.plotly_chart(fig, use_container_width=True)
            
            # Métriques de fraude
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Transactions analysées", f"{len(df_transactions):,}")
            with col2:
                st.metric("Fraudes détectées", f"{df_transactions['Fraude'].sum()}")
            with col3:
                taux_fraude = (df_transactions['Fraude'].sum() / len(df_transactions)) * 100
                st.metric("Taux de fraude", f"{taux_fraude:.2f}%")
    
    elif secteur == "Santé":
        st.success("**🏥 Secteur Santé - Applications Big Data**")
        
        df_patients, df_consultations = generer_donnees_sante()
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Tableau de Bord Santé", "🔍 Analytics Prédictif", 
            "💊 Gestion des Ressources", "🏥 Télémédecine"
        ])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Nombre de patients", f"{len(df_patients):,}")
                st.metric("Taux de diabète", f"{(df_patients['diabete'].mean() * 100):.1f}%")
            
            with col2:
                st.metric("Consultations totales", f"{len(df_consultations):,}")
                st.metric("Coût moyen consultation", f"{df_consultations['cout'].mean():.1f} €")
            
            with col3:
                age_moyen = df_patients['age'].mean()
                st.metric("Âge moyen patients", f"{age_moyen:.1f} ans")
                st.metric("Taux de fumeurs", f"{(df_patients['fumeur'].mean() * 100):.1f}%")
            
            # Visualisations santé
            col1, col2 = st.columns(2)
            
            with col1:
                # Distribution des diagnostics
                diag_counts = df_consultations['diagnostic_principal'].value_counts().head(10)
                fig = px.pie(diag_counts, values=diag_counts.values, names=diag_counts.index,
                           title="Top 10 des diagnostics")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Tension artérielle par âge
                fig = px.scatter(df_patients, x='age', y='tension_arterielle', 
                               color='diabete', size='cholesterol',
                               title="Tension artérielle vs Âge",
                               hover_data=['sexe', 'fumeur'])
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("🔮 Prédiction des Risques Santé")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Calculateur de risque cardio-vasculaire
                st.write("**Calculateur de Risque Cardio-Vasculaire**")
                
                age = st.slider("Âge", 20, 80, 45)
                tension = st.slider("Tension artérielle", 80, 200, 120)
                cholesterol = st.slider("Cholestérol", 100, 300, 180)
                fumeur = st.checkbox("Fumeur")
                diabete = st.checkbox("Diabétique")
                sexe = st.selectbox("Sexe", ["Homme", "Femme"])
                
                # Calcul simplifié du risque (modèle FACTICE pour démonstration)
                risque_base = 5
                if sexe == "Homme":
                    risque_base += 10
                
                risque = (risque_base + 
                         age * 0.5 + 
                         max(0, tension - 120) * 0.2 + 
                         max(0, cholesterol - 180) * 0.1 + 
                         fumeur * 15 + 
                         diabete * 20)
                risque = min(100, max(5, risque))
                
                st.metric("Risque cardio-vasculaire", f"{risque:.1f}%")
                
                if risque > 70:
                    st.error("Risque ÉLEVÉ - Consultation médicale recommandée")
                elif risque > 40:
                    st.warning("Risque MODÉRÉ - Surveillance recommandée")
                else:
                    st.success("Risque FAIBLE - Maintenir mode de vie sain")
            
            with col2:
                # Analyse des coûts de santé
                couts_par_diagnostic = df_consultations.groupby('diagnostic_principal')['cout'].mean().sort_values(ascending=False).head(10)
                fig = px.bar(couts_par_diagnostic, 
                           title="Coût moyen par diagnostic (Top 10)",
                           labels={'value': 'Coût moyen (€)', 'diagnostic_principal': 'Diagnostic'})
                st.plotly_chart(fig, use_container_width=True)
                
                # Distribution des durées de consultation
                fig = px.histogram(df_consultations, x='duree_minutes', 
                                 title="Distribution des durées de consultation",
                                 nbins=20)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.subheader("📈 Optimisation des Ressources Médicales")
            
            # Analyse de la charge de travail
            charge_medecins = df_consultations.groupby('medecin').agg({
                'patient_id': 'count',
                'duree_minutes': 'sum',
                'cout': 'sum'
            }).round(2).sort_values('patient_id', ascending=False)
            
            charge_medecins.columns = ['Nb Patients', 'Total Minutes', 'Total Coût']
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Charge de travail par médecin**")
                st.dataframe(charge_medecins)
            
            with col2:
                fig = px.bar(charge_medecins, y='Nb Patients',
                           title="Nombre de patients par médecin")
                st.plotly_chart(fig, use_container_width=True)
            
            # Efficacité des médecins
            charge_medecins['Patients par Heure'] = (charge_medecins['Nb Patients'] / (charge_medecins['Total Minutes'] / 60)).round(2)
            charge_medecins['Coût par Patient'] = (charge_medecins['Total Coût'] / charge_medecins['Nb Patients']).round(2)
            
            st.write("**Indicateurs d'efficacité:**")
            st.dataframe(charge_medecins[['Patients par Heure', 'Coût par Patient']])
            
            # Recommandations d'optimisation
            st.subheader("💡 Recommandations d'Amélioration")
            st.write("""
            - **Rééquilibrer la charge** entre médecins surchargés et moins occupés
            - **Optimiser les plannings** basé sur la durée moyenne des consultations
            - **Développer la télémédecine** pour les suivis simples
            - **Automatiser** les tâches administratives répétitives
            - **Formation continue** sur les diagnostics les plus fréquents
            """)
        
        with tab4:
            st.subheader("🏥 Télémédecine et Innovation")
            
            st.markdown("""
            ### Applications Big Data en Télémédecine
            
            **1. Surveillance à Distance**
            - Monitoring des patients chroniques
            - Alertes précoces pour les complications
            - Réduction des hospitalisations de 30%
            
            **2. Diagnostic Assisté**
            - IA pour l'analyse d'imagerie médicale
            - Algorithmes de diagnostic différentiel
            - Amélioration précision diagnostic de 25%
            
            **3. Recherche Clinique**
            - Analyse de données patients à grande échelle
            - Identification de nouveaux traitements
            - Accélération des découvertes médicales
            
            **4. Prévention Personnalisée**
            - Recommandations santé individualisées
            - Détection précoce des risques
            - Amélioration de la santé populationnelle
            """)
            
            # Simulation d'impact télémédecine
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Consultations à distance", "35%", "+15% vs 2023")
            
            with col2:
                st.metric("Économies réalisées", "2.5M €", "+28%")
            
            with col3:
                st.metric("Satisfaction patients", "4.5/5", "+0.7 pts")
    
    elif secteur == "Télécom":
        st.info("**📞 Secteur Télécom - Applications Big Data**")
        
        df_telecom = generer_donnees_telecom()
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Performance Réseau", "📱 Analyse Clients", 
            "🎯 Marketing Ciblé", "🚨 Prévention Fraude"
        ])
        
        with tab1:
            st.subheader("Performance du Réseau et Satisfaction Client")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Clients totaux", f"{len(df_telecom):,}")
                st.metric("Satisfaction moyenne", f"{df_telecom['satisfaction'].mean():.1f}/10")
            
            with col2:
                data_moyenne = df_telecom['data_utilisee_go'].mean()
                st.metric("Data utilisée moyenne", f"{data_moyenne:.1f} Go")
                st.metric("Facture moyenne", f"{df_telecom['facture_moyenne'].mean():.1f} €")
            
            with col3:
                appels_moyens = df_telecom['appels_minutes'].mean()
                st.metric("Appels moyens/mois", f"{appels_moyens:.0f} min")
                st.metric("SMS moyens/mois", f"{df_telecom['sms_envoyes'].mean():.0f}")
            
            # Analyse par forfait
            col1, col2 = st.columns(2)
            
            with col1:
                performance_forfait = df_telecom.groupby('forfait').agg({
                    'satisfaction': 'mean',
                    'data_utilisee_go': 'mean',
                    'facture_moyenne': 'mean',
                    'nb_reclamations': 'mean'
                }).round(2)
                
                st.write("**Performance par type de forfait**")
                st.dataframe(performance_forfait)
            
            with col2:
                fig = px.box(df_telecom, x='forfait', y='satisfaction',
                           title="Satisfaction client par forfait")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("📱 Analyse Comportementale des Clients")
            
            # Segmentation des clients
            df_telecom['utilisation_totale'] = (df_telecom['data_utilisee_go'] + 
                                              df_telecom['appels_minutes']/100 + 
                                              df_telecom['sms_envoyes']/10)
            
            # Clustering des clients
            features = ['data_utilisee_go', 'appels_minutes', 'sms_envoyes', 'facture_moyenne']
            X = df_telecom[features]
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            kmeans = KMeans(n_clusters=4, random_state=42)
            df_telecom['segment'] = kmeans.fit_predict(X_scaled)
            
            segment_descriptions = {
                0: "📊 Faibles Utilisateurs - Coût faible",
                1: "📱 Utilisateurs Data - Forte consommation data",
                2: "📞 Utilisateurs Voix - Forte consommation appels", 
                3: "💎 Power Users - Forte consommation globale"
            }
            
            col1, col2 = st.columns(2)
            
            with col1:
                segment_counts = df_telecom['segment'].value_counts().sort_index()
                segments_named = [segment_descriptions[i] for i in segment_counts.index]
                
                fig = px.pie(values=segment_counts.values, names=segments_named,
                           title="Segmentation des clients")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("📋 Profils des Segments")
                for segment_id, description in segment_descriptions.items():
                    segment_data = df_telecom[df_telecom['segment'] == segment_id]
                    count = len(segment_data)
                    satisfaction = segment_data['satisfaction'].mean()
                    facture_moyenne = segment_data['facture_moyenne'].mean()
                    
                    st.write(f"**{description}** ({count} clients)")
                    st.write(f"- Satisfaction: {satisfaction:.1f}/10")
                    st.write(f"- Facture moyenne: {facture_moyenne:.1f} €")
                    st.write(f"- Data moyenne: {segment_data['data_utilisee_go'].mean():.1f} Go")
                    st.write("---")
        
        with tab3:
            st.subheader("🎯 Marketing et Fidélisation Ciblés")
            
            # Prédiction de désabonnement (churn)
            df_telecom['score_churn'] = np.random.beta(2, 5, len(df_telecom))
            df_telecom['risque_churn'] = pd.cut(df_telecom['score_churn'], 
                                              bins=[0, 0.3, 0.7, 1], 
                                              labels=['Faible', 'Moyen', 'Élevé'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                risque_churn_count = df_telecom['risque_churn'].value_counts()
                fig = px.bar(risque_churn_count, 
                           title="Répartition du risque de désabonnement",
                           labels={'value': 'Nombre clients', 'risque_churn': 'Risque'})
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("💡 Stratégies de Fidélisation")
                
                strategies = {
                    'Faible': """
                    ✅ **Maintenir la qualité de service**
                    - Offres de fidélité
                    - Programme de parrainage
                    - Communications personnalisées
                    """,
                    'Moyen': """
                    📞 **Contact proactif**
                    - Offres personnalisées
                    - Enquête satisfaction
                    - Service client dédié
                    """, 
                    'Élevé': """
                    🚨 **Intervention immédiate**
                    - Offres promotionnelles
                    - Service premium
                    - Analyse des causes de mécontentement
                    """
                }
                
                for risque, strategie in strategies.items():
                    count = len(df_telecom[df_telecom['risque_churn'] == risque])
                    st.write(f"**Risque {risque}** ({count} clients)")
                    st.write(strategie)
                    st.write("")
        
        with tab4:
            st.subheader("🚨 Détection de Fraude et Sécurité")
            
            # Simulation de détection d'anomalies
            st.write("**Détection des comportements anormaux**")
            
            # Seuils pour détection d'anomalies (percentile 95)
            seuil_data = df_telecom['data_utilisee_go'].quantile(0.95)
            seuil_appels = df_telecom['appels_minutes'].quantile(0.95)
            seuil_sms = df_telecom['sms_envoyes'].quantile(0.95)
            
            anomalies = df_telecom[
                (df_telecom['data_utilisee_go'] > seuil_data) | 
                (df_telecom['appels_minutes'] > seuil_appels) |
                (df_telecom['sms_envoyes'] > seuil_sms)
            ]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Seuil data anormale", f"{seuil_data:.1f} Go")
                st.metric("Seuil appels anormaux", f"{seuil_appels:.0f} min")
                st.metric("Seuil SMS anormaux", f"{seuil_sms:.0f}")
                st.metric("Clients suspects détectés", f"{len(anomalies)}")
            
            with col2:
                if len(anomalies) > 0:
                    st.write("**Top 5 comportements suspects**")
                    suspects_display = anomalies[['client_id', 'data_utilisee_go', 'appels_minutes', 'sms_envoyes', 'forfait']].head()
                    st.dataframe(suspects_display.style.format({
                        'data_utilisee_go': '{:.1f}',
                        'appels_minutes': '{:.0f}',
                        'sms_envoyes': '{:.0f}'
                    }))
            
            # Recommandations anti-fraude
            st.subheader("🛡️ Mesures de Prévention")
            st.write("""
            - **Surveillance en temps réel** de la consommation
            - **Alertes automatiques** pour les dépassements de seuils
            - **Vérification d'identité** renforcée pour les forfaits haut de gamme
            - **Analyse des patterns** de consommation inhabituels
            - **Collaboration inter-opérateurs** pour détecter les fraudes coordonnées
            - **Blocage automatique** des activités suspectes
            - **Audit régulier** des systèmes de sécurité
            """)
    
    elif secteur == "Transport & Logistique":
        st.warning("**🚚 Transport & Logistique - Applications Big Data**")
        
        st.subheader("Optimisation de la Supply Chain")
        
        # Simulation de données logistiques
        np.random.seed(42)
        n_livraisons = 500
        
        data_logistique = {
            'livraison_id': range(1, n_livraisons + 1),
            'date': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_livraisons)],
            'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor'], n_livraisons),
            'poids_kg': np.random.uniform(1, 1000, n_livraisons),
            'distance_km': np.random.uniform(5, 500, n_livraisons),
            'duree_livraison_heures': np.random.uniform(1, 72, n_livraisons),
            'cout_livraison': np.random.uniform(10, 500, n_livraisons),
            'retard_heures': np.random.exponential(2, n_livraisons),
            'satisfaction_client': np.random.randint(1, 10, n_livraisons),
            'type_transport': np.random.choice(['Camion', 'Utilitaire', 'Moto'], n_livraisons, p=[0.6, 0.3, 0.1])
        }
        
        df_logistique = pd.DataFrame(data_logistique)
        df_logistique['retard_heures'] = df_logistique['retard_heures'].clip(0, 24)
        
        tab1, tab2, tab3 = st.tabs(["📦 Performance Livraison", "🚛 Optimisation Routes", "📊 Analytics Prédictif"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                retard_moyen = df_logistique['retard_heures'].mean()
                st.metric("Retard moyen", f"{retard_moyen:.1f} h")
                taux_livraison_temps = (len(df_logistique[df_logistique['retard_heures'] < 1])/len(df_logistique)*100)
                st.metric("Taux de livraison à temps", f"{taux_livraison_temps:.1f}%")
            
            with col2:
                cout_moyen = df_logistique['cout_livraison'].mean()
                st.metric("Coût moyen livraison", f"{cout_moyen:.1f} €")
                st.metric("Satisfaction moyenne", f"{df_logistique['satisfaction_client'].mean():.1f}/10")
            
            with col3:
                distance_moyenne = df_logistique['distance_km'].mean()
                st.metric("Distance moyenne", f"{distance_moyenne:.1f} km")
                st.metric("Poids moyen", f"{df_logistique['poids_kg'].mean():.1f} kg")
            
            # Analyse des performances par région
            col1, col2 = st.columns(2)
            
            with col1:
                perf_region = df_logistique.groupby('region').agg({
                    'retard_heures': 'mean',
                    'satisfaction_client': 'mean',
                    'cout_livraison': 'mean',
                    'livraison_id': 'count'
                }).round(2)
                
                perf_region.columns = ['Retard moyen (h)', 'Satisfaction', 'Coût moyen (€)', 'Nb Livraisons']
                st.write("**Performance par région**")
                st.dataframe(perf_region)
            
            with col2:
                fig = px.scatter(df_logistique, x='distance_km', y='cout_livraison',
                               color='type_transport', size='poids_kg',
                               title="Coût vs Distance par type de transport",
                               hover_data=['region'])
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("🚛 Optimisation des Itinéraires")
            
            # Simulation d'optimisation de tournées
            st.write("**Simulateur d'Optimisation de Tournée**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                n_livraisons_tournee = st.slider("Nombre de livraisons", 5, 50, 20)
                capacite_vehicule = st.slider("Capacité véhicule (kg)", 500, 2000, 1000)
                zone_couverte = st.selectbox("Zone de livraison", ['Dakar', 'Thiès', 'Régionale'])
            
            with col2:
                traffic = st.select_slider("Niveau de trafic", options=['Faible', 'Moyen', 'Élevé'])
                conditions_meteo = st.select_slider("Conditions météo", options=['Bonnes', 'Moyennes', 'Mauvaises'])
            
            # Calcul d'optimisation simplifié
            if st.button("Optimiser la tournée"):
                # Facteurs d'impact
                facteur_traffic = {'Faible': 1.0, 'Moyen': 1.3, 'Élevé': 1.7}
                facteur_meteo = {'Bonnes': 1.0, 'Moyennes': 1.2, 'Mauvaises': 1.5}
                facteur_zone = {'Dakar': 1.0, 'Thiès': 1.1, 'Régionale': 1.4}
                
                duree_optimale = (n_livraisons_tournee * 0.5 * 
                                facteur_traffic[traffic] * 
                                facteur_meteo[conditions_meteo] * 
                                facteur_zone[zone_couverte])
                
                cout_optimise = (n_livraisons_tournee * 8 * 
                               facteur_traffic[traffic] * 
                               facteur_meteo[conditions_meteo] * 
                               facteur_zone[zone_couverte])
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Durée estimée", f"{duree_optimale:.1f} h")
                    st.metric("Distance estimée", f"{(n_livraisons_tournee * 15 * facteur_zone[zone_couverte]):.0f} km")
                with col2:
                    st.metric("Coût estimé", f"{cout_optimise:.1f} €")
                    st.metric("Économies potentielles", f"{(cout_optimise * 0.15):.1f} €", "-15%")
                
                st.success("**Tournée optimisée générée !**")
                st.write("""
                **Recommandations:**
                - Regrouper les livraisons par zone géographique
                - Prioriser les livraisons urgentes en matinée
                - Adapter les véhicules au type de marchandise
                - Prévoir des itinéraires alternatifs pour les zones à fort trafic
                """)
        
        with tab3:
            st.subheader("📊 Analytics Prédictif Logistique")
            
            # Prédiction des retards
            st.write("**Prédiction des Risques de Retard**")
            
            # Facteurs influençant les retards (modèle simplifié)
            df_logistique['risque_retard'] = (
                df_logistique['distance_km'] * 0.001 +
                df_logistique['poids_kg'] * 0.0005 +
                np.random.normal(0, 0.1, len(df_logistique))
            )
            df_logistique['risque_retard'] = df_logistique['risque_retard'].clip(0, 1)
            df_logistique['niveau_risque'] = pd.cut(df_logistique['risque_retard'], 
                                                  bins=[0, 0.3, 0.7, 1], 
                                                  labels=['Faible', 'Moyen', 'Élevé'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.histogram(df_logistique, x='risque_retard', 
                                 title="Distribution du risque de retard",
                                 nbins=20)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                risque_par_region = df_logistique.groupby('region')['risque_retard'].mean().sort_values(ascending=False)
                fig = px.bar(risque_par_region, 
                           title="Risque de retard moyen par région")
                st.plotly_chart(fig, use_container_width=True)
            
            # Calculateur de risque individuel
            st.subheader("🔮 Calculateur de Risque de Retard")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                distance = st.slider("Distance (km)", 10, 500, 100)
                poids = st.slider("Poids (kg)", 1, 1000, 100)
            
            with col2:
                region = st.selectbox("Région de destination", ['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor'])
                type_transp = st.selectbox("Type transport", ['Camion', 'Utilitaire', 'Moto'])
            
            with col3:
                jour_semaine = st.selectbox("Jour de livraison", ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'])
                meteo = st.select_slider("Prévisions météo", ['Bonnes', 'Moyennes', 'Mauvaises'])
            
            # Calcul du risque (modèle FACTICE pour démonstration)
            facteur_region = {'Dakar': 0.1, 'Thiès': 0.2, 'Diourbel': 0.3, 'Saint-Louis': 0.4, 'Ziguinchor': 0.5}
            facteur_transport = {'Camion': 0.1, 'Utilitaire': 0.2, 'Moto': 0.3}
            facteur_jour = {'Lundi': 0.1, 'Mardi': 0.1, 'Mercredi': 0.1, 'Jeudi': 0.1, 'Vendredi': 0.2, 'Samedi': 0.3}
            facteur_meteo_calc = {'Bonnes': 0.1, 'Moyennes': 0.2, 'Mauvaises': 0.4}
            
            risque_calculé = (
                distance * 0.001 +
                poids * 0.0005 +
                facteur_region[region] +
                facteur_transport[type_transp] +
                facteur_jour[jour_semaine] +
                facteur_meteo_calc[meteo]
            )
            risque_calculé = min(0.95, max(0.05, risque_calculé))
            
            st.metric("Risque de retard estimé", f"{risque_calculé:.1%}")
            
            if risque_calculé > 0.7:
                st.error("⚠️ Risque ÉLEVÉ - Planifier des contingences")
                st.write("**Actions recommandées:** Départ plus tôt, Véhicule de remplacement, Itinéraire alternatif")
            elif risque_calculé > 0.4:
                st.warning("📋 Risque MODÉRÉ - Surveillance recommandée")
                st.write("**Actions recommandées:** Surveillance GPS, Contact client préventif")
            else:
                st.success("✅ Risque FAIBLE - Livraison normale")
                st.write("**Actions recommandées:** Suivi standard, Communication normale")
    
    elif secteur == "Énergie":
        st.success("**⚡ Secteur Énergie - Applications Big Data**")
        
        st.subheader("Optimisation de la Production et Distribution")
        
        # Simulation de données énergétiques
        np.random.seed(42)
        n_jours = 365
        dates = pd.date_range('2024-01-01', periods=n_jours, freq='D')
        
        data_energie = {
            'date': dates,
            'consommation_mwh': np.random.normal(1000, 200, n_jours) + 
                              np.sin(np.arange(n_jours) * 2 * np.pi / 365) * 100 +
                              np.sin(np.arange(n_jours) * 2 * np.pi / 7) * 50,
            'production_solaire': np.random.normal(300, 100, n_jours) * 
                                (1 + np.sin(np.arange(n_jours) * 2 * np.pi / 365) * 0.3),
            'production_eolienne': np.random.normal(200, 80, n_jours) * 
                                 (1 + np.cos(np.arange(n_jours) * 2 * np.pi / 365) * 0.4),
            'production_gaz': np.random.normal(500, 100, n_jours),
            'temperature': np.random.normal(25, 5, n_jours) + 
                          np.sin(np.arange(n_jours) * 2 * np.pi / 365) * 10,
            'prix_marche_€_mwh': np.random.normal(50, 15, n_jours),
            'pannes_reseau': np.random.poisson(0.1, n_jours)
        }
        
        df_energie = pd.DataFrame(data_energie)
        df_energie['production_totale'] = (df_energie['production_solaire'] + 
                                         df_energie['production_eolienne'] + 
                                         df_energie['production_gaz'])
        df_energie['equilibre_reseau'] = df_energie['production_totale'] - df_energie['consommation_mwh']
        
        tab1, tab2, tab3 = st.tabs(["📈 Production/Consommation", "🔧 Maintenance Prédictive", "💰 Optimisation Marché"])
        
        with tab1:
            st.subheader("Équilibre Production-Consommation")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                conso_moyenne = df_energie['consommation_mwh'].mean()
                st.metric("Consommation moyenne", f"{conso_moyenne:.0f} MWh/jour")
                st.metric("Pic de consommation", f"{df_energie['consommation_mwh'].max():.0f} MWh")
            
            with col2:
                prod_moyenne = df_energie['production_totale'].mean()
                st.metric("Production moyenne", f"{prod_moyenne:.0f} MWh/jour")
                taux_couverture = (prod_moyenne/conso_moyenne*100)
                st.metric("Taux couverture", f"{taux_couverture:.1f}%")
            
            with col3:
                equilibre_moyen = df_energie['equilibre_reseau'].mean()
                st.metric("Équilibre réseau", f"{equilibre_moyen:.0f} MWh/jour")
                st.metric("Prix moyen marché", f"{df_energie['prix_marche_€_mwh'].mean():.1f} €/MWh")
            
            # Graphiques production/consommation
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(df_energie.tail(30), x='date', y=['consommation_mwh', 'production_totale'],
                            title="Production vs Consommation (derniers 30 jours)")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Mix énergétique
                mix_energetique = {
                    'Solaire': df_energie['production_solaire'].mean(),
                    'Éolien': df_energie['production_eolienne'].mean(),
                    'Gaz': df_energie['production_gaz'].mean()
                }
                
                fig = px.pie(values=list(mix_energetique.values()), 
                           names=list(mix_energetique.keys()),
                           title="Mix énergétique moyen")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("🔧 Maintenance Prédictive des Infrastructures")
            
            # Simulation de données de maintenance
            n_equipements = 50
            data_maintenance = {
                'equipement_id': range(1, n_equipements + 1),
                'type_equipement': np.random.choice(['Transformateur', 'Ligne HT', 'Sous-station', 'Générateur'], n_equipements),
                'age_ans': np.random.randint(1, 30, n_equipements),
                'temperature_moyenne': np.random.normal(65, 15, n_equipements),
                'vibrations': np.random.normal(2, 0.5, n_equipements),
                'niveau_isolation': np.random.normal(85, 10, n_equipements),
                'heures_fonctionnement': np.random.randint(1000, 50000, n_equipements)
            }
            
            df_maintenance = pd.DataFrame(data_maintenance)
            
            # Calcul du risque de panne (modèle simplifié)
            df_maintenance['risque_panne'] = (
                df_maintenance['age_ans'] * 0.03 +
                (df_maintenance['temperature_moyenne'] - 60) * 0.01 +
                (df_maintenance['vibrations'] - 2) * 0.1 +
                (100 - df_maintenance['niveau_isolation']) * 0.02
            )
            df_maintenance['risque_panne'] = df_maintenance['risque_panne'].clip(0, 1)
            df_maintenance['priorite_maintenance'] = pd.cut(df_maintenance['risque_panne'], 
                                                          bins=[0, 0.3, 0.7, 1], 
                                                          labels=['Basse', 'Moyenne', 'Haute'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Équipements à risque élevé**")
                equipements_risque = df_maintenance[df_maintenance['priorite_maintenance'] == 'Haute'].sort_values('risque_panne', ascending=False)
                st.dataframe(equipements_risque[['equipement_id', 'type_equipement', 'age_ans', 'risque_panne']].head(10))
            
            with col2:
                risque_par_type = df_maintenance.groupby('type_equipement')['risque_panne'].mean().sort_values(ascending=False)
                fig = px.bar(risque_par_type, 
                           title="Risque de panne moyen par type d'équipement")
                st.plotly_chart(fig, use_container_width=True)
            
            # Calculateur de risque d'équipement
            st.subheader("🔮 Calculateur de Risque de Panne")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                age = st.slider("Âge équipement (ans)", 1, 30, 10)
                temperature = st.slider("Température moyenne (°C)", 40, 100, 65)
            
            with col2:
                vibrations = st.slider("Niveau vibrations", 1.0, 5.0, 2.0)
                isolation = st.slider("Niveau isolation (%)", 50, 100, 85)
            
            with col3:
                heures_fonc = st.slider("Heures fonctionnement", 1000, 50000, 25000)
                type_eq = st.selectbox("Type équipement", ['Transformateur', 'Ligne HT', 'Sous-station', 'Générateur'])
            
            # Calcul du risque (modèle FACTICE pour démonstration)
            risque_calc = (
                age * 0.03 +
                (temperature - 60) * 0.01 +
                (vibrations - 2) * 0.1 +
                (100 - isolation) * 0.02
            )
            risque_calc = min(0.95, max(0.05, risque_calc))
            
            st.metric("Risque de panne estimé", f"{risque_calc:.1%}")
            
            if risque_calc > 0.7:
                st.error("🔴 RISQUE ÉLEVÉ - Maintenance urgente requise")
                st.write("**Actions recommandées:** Inspection immédiate, Réduction charge, Plan remplacement")
            elif risque_calc > 0.4:
                st.warning("🟡 RISQUE MODÉRÉ - Surveillance renforcée")
                st.write("**Actions recommandées:** Monitoring température, Planning maintenance préventive")
            else:
                st.success("🟢 RISQUE FAIBLE - Maintenance normale")
                st.write("**Actions recommandées:** Maintenance programmée, Surveillance standard")
        
        with tab3:
            st.subheader("💰 Optimisation des Achats d'Énergie")
            
            # Analyse des prix de marché
            st.write("**Analyse des Prix de Marché et Optimisation des Achats**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Volatilité des prix
                df_energie['prix_rolling_avg'] = df_energie['prix_marche_€_mwh'].rolling(7).mean()
                df_energie['prix_rolling_std'] = df_energie['prix_marche_€_mwh'].rolling(7).std()
                
                fig = px.line(df_energie.tail(90), x='date', 
                            y=['prix_marche_€_mwh', 'prix_rolling_avg'],
                            title="Évolution des prix de marché (90 derniers jours)")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Corrélation température/prix
                fig = px.scatter(df_energie, x='temperature', y='prix_marche_€_mwh',
                               trendline='ols',
                               title="Impact de la température sur les prix",
                               trendline_color_override='red')
                st.plotly_chart(fig, use_container_width=True)
            
            # Recommandations d'optimisation
            st.subheader("💡 Stratégies d'Optimisation")
            
            prix_moyen = df_energie['prix_marche_€_mwh'].mean()
            prix_min = df_energie['prix_marche_€_mwh'].min()
            prix_max = df_energie['prix_marche_€_mwh'].max()
            volatilite = df_energie['prix_marche_€_mwh'].std()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Prix moyen", f"{prix_moyen:.1f} €/MWh")
                st.write("**Achats de base** - Contrats long terme")
            
            with col2:
                st.metric("Prix minimum", f"{prix_min:.1f} €/MWh")
                st.write("**Achats spot** - Périodes creuses")
            
            with col3:
                st.metric("Prix maximum", f"{prix_max:.1f} €/MWh")
                st.write("**Production interne** - Périodes de pic")
            
            with col4:
                st.metric("Volatilité", f"{volatilite:.1f} €")
                st.write("**Couverture risque** - Instruments financiers")
            
            # Stratégie d'optimisation
            st.write("""
            **Stratégie recommandée:**
            - **60%** en contrats long terme (stabilité)
            - **25%** en achats spot (optimisation coûts)  
            - **10%** en production de réserve (sécurité)
            - **5%** en instruments de couverture (gestion risque)
            
            **Économies potentielles:** 15-25% sur les coûts d'approvisionnement
            
            **Facteurs clés de succès:**
            - Surveillance continue des marchés
            - Prévisions météorologiques précises
            - Analyse en temps réel de la consommation
            - Maintenance préventive des infrastructures
            """)


# =============================================================================
# SECTION 4: SCIENCE DES DONNÉES APPLIQUÉE - CORRIGÉE ET COMPLÉTÉE
# =============================================================================
# =============================================================================
# SECTION 4: SCIENCE DES DONNÉES APPLIQUÉE - CORRIGÉE ET COMPLÉTÉE
# =============================================================================

def section_science_donnees():
    st.header("🔬 Science des Données Appliquée")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Types d'Analytics", "🤖 Machine Learning", "📊 Visualisation", "🧹 Data Quality", "🎯 Cas Réels"
    ])
    
    with tab1:
        st.subheader("Les 4 Types d'Analytics")
        
        # Charger les données pour cette section
        df_clients, df_transactions = generer_donnees_retail()
        
        analytics_type = st.radio(
            "Choisir un type d'analytics:",
            ["Descriptive (Que s'est-il passé?)", 
             "Diagnostic (Pourquoi c'est arrivé?)", 
             "Predictive (Que va-t-il se passer?)", 
             "Prescriptive (Que devrions-nous faire?)"]
        )
        
        if "Descriptive" in analytics_type:
            st.info("""
            **📊 Analytics Descriptive : Comprendre le passé**
            
            **Techniques:**
            - Reporting et tableaux de bord
            - Métriques KPI traditionnelles
            - Analyse de tendances
            
            **Outils:** Tableau, Power BI, Google Analytics
            **Cas d'usage:** Rapports de performance, suivi d'activité
            """)
            
            # Exemple de dataset descriptif
            data = pd.DataFrame({
                'Produit': ['A', 'B', 'C', 'D', 'E'],
                'Ventes': [120, 150, 130, 170, 190],
                'Croissance': [5, 12, -2, 8, 15]
            })
            
            fig = px.bar(data, x='Produit', y='Ventes', color='Croissance',
                        title="Performance des Produits - Analytics Descriptive")
            st.plotly_chart(fig, use_container_width=True)
        
        elif "Diagnostic" in analytics_type:
            st.warning("""
            **🔍 Analytics Diagnostic : Comprendre les causes**
            
            **Techniques:**
            - Analyse de corrélation
            - Analyse de racine cause
            - Segmentation avancée
            
            **Cas d'usage:** Identifier pourquoi les ventes ont baissé
            """)
            
            # Analyse diagnostique
            df_analysis = df_clients.merge(
                df_transactions.groupby('client_id').agg({
                    'montant': 'sum'
                }).reset_index(), 
                left_on='client_id', 
                right_on='client_id'
            )
            
            fig = px.scatter(df_analysis, x='revenu_annuel', y='montant', 
                           color='segment', trendline='ols',
                           title="Corrélation Revenu vs Dépenses")
            st.plotly_chart(fig, use_container_width=True)
        
        elif "Predictive" in analytics_type:
            st.success("""
            **🔮 Analytics Predictive : Anticiper le futur**
            
            **Techniques:**
            - Machine Learning
            - Modèles statistiques
            - Séries temporelles
            
            **Cas d'usage:** Prévision des ventes, prédiction de churn
            """)
            
            # Simulation prédictive
            df_clients['score_churn'] = np.random.beta(2, 5, len(df_clients))
            
            fig = px.histogram(df_clients, x='score_churn', 
                             title="Distribution du Score de Churn Prédit")
            st.plotly_chart(fig, use_container_width=True)
        
        elif "Prescriptive" in analytics_type:
            st.error("""
            **💡 Analytics Prescriptive : Recommander des actions**
            
            **Techniques:**
            - Optimisation
            - Simulation
            - Systèmes experts
            
            **Cas d'usage:** Optimisation des campagnes, recommandations stratégiques
            """)
            
            # Exemple prescriptif
            recommendations = pd.DataFrame({
                'Segment': ['VIP', 'Fidèle', 'Régulier', 'Occasionnel'],
                'Action': ['Offre exclusive', 'Programme fidélité', 'Email personnalisé', 'Campagne reactivation'],
                'Budget': [5000, 3000, 1500, 2000],
                'ROI_attendu': [2.5, 1.8, 1.2, 0.8]
            })
            
            fig = px.bar(recommendations, x='Segment', y='ROI_attendu',
                        title="ROI Attendu par Type d'Action Marketing")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("🤖 Machine Learning Opérationnel")
        
        ml_type = st.selectbox(
            "Type de ML:",
            ["Supervisé", "Non-supervisé", "Renforcement", "Deep Learning"]
        )
        
        if ml_type == "Supervisé":
            st.markdown("""
            **Apprentissage Supervisé**
            
            **Algorithme:** Prédiction basée sur des données labellisées
            
            **Applications:**
            - Classification: Spam detection, diagnostic médical
            - Régression: Prévision ventes, pricing
            """)
            
            # Simulation de modèle de prédiction
            st.subheader("Simulateur de Prédiction de Churn")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                age = st.slider("Âge du client", 18, 80, 35)
                anciennete = st.slider("Ancienneté (mois)", 1, 60, 12)
            
            with col2:
                revenu = st.slider("Revenu annuel (k€)", 20, 150, 50)
                satisfaction = st.slider("Satisfaction (1-10)", 1, 10, 7)
            
            with col3:
                frequence = st.slider("Fréquence achats/mois", 1, 20, 5)
                panier_moyen = st.slider("Panier moyen (€)", 20, 200, 85)
            
            # Modèle simplifié de prédiction
            proba_churn = max(0.05, min(0.95, 
                0.3 + 
                (age * 0.001) + 
                (anciennete * -0.01) + 
                ((150 - revenu) * 0.002) +
                ((10 - satisfaction) * 0.03) +
                ((10 - frequence) * 0.02) +
                ((200 - panier_moyen) * 0.001)
            ))
            
            st.metric("Probabilité de Churn", f"{proba_churn:.1%}")
            
            if proba_churn > 0.7:
                st.error("Risque ÉLEVÉ - Actions immédiates requises")
            elif proba_churn > 0.4:
                st.warning("Risque MOYEN - Surveillance recommandée")
            else:
                st.success("Risque FAIBLE - Client stable")
        
        elif ml_type == "Non-supervisé":
            st.success("**🔍 Apprentissage Non Supervisé : Découvrir des patterns cachés**")
            
            st.markdown("""
            **Use Case :** Segmentation de clientèle sans labels pré-définis
            **Algorithme :** K-Means Clustering
            **Applications :** Marketing personnalisé, Détection d'anomalies
            """)
            
            # Générer des données pour le clustering
            df_clients, _ = generer_donnees_retail()
            
            # Clustering des clients
            df_clusters = df_clients[['age', 'revenu_annuel', 'frequence_achats', 'panier_moyen']].copy()
            scaler = StandardScaler()
            df_scaled = scaler.fit_transform(df_clusters)
            
            kmeans = KMeans(n_clusters=4, random_state=42)
            df_clusters['cluster'] = kmeans.fit_predict(df_scaled)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.scatter(df_clusters, x='revenu_annuel', y='panier_moyen', 
                               color='cluster', size='frequence_achats',
                               title="Segmentation client par revenu et comportement")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Profils des clusters
                cluster_profiles = df_clusters.groupby('cluster').mean()
                fig = px.bar(cluster_profiles.T, barmode='group',
                           title="Profils moyens des clusters")
                st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("📋 Description des Segments Découverts")
            segments_desc = {
                0: "🎯 Jeunes actifs - Revenu moyen, forte fréquence d'achat",
                1: "💎 Clients premium - Revenu élevé, panier important",
                2: "📊 Clients économiques - Revenu faible, recherche de bonnes affaires",
                3: "⭐ Clients fidèles - Ancienneté élevée, fréquence stable"
            }
            
            for cluster, desc in segments_desc.items():
                st.write(f"**Cluster {cluster}:** {desc}")
        
        elif ml_type == "Renforcement":
            st.info("**🎮 Apprentissage par Renforcement : Apprentissage par l'expérience**")
            
            st.markdown("""
            **Use Case :** Optimisation des recommandations produits en temps réel
            **Algorithme :** Q-Learning, Deep Q-Network
            **Applications :** Systèmes de recommandation, Trading algorithmique
            """)
            
            # Simulation d'apprentissage par renforcement
            st.subheader("Simulation : Optimisation des Recommandations")
            
            # États (segments clients) et Actions (types de recommandations)
            etats = ['Jeune', 'Actif', 'Senior', 'VIP']
            actions = ['Promo', 'Nouveauté', 'Cross-selling', 'Service premium']
            
            # Matrice Q simulée
            q_table = pd.DataFrame(
                np.random.uniform(0, 1, (len(etats), len(actions))),
                index=etats,
                columns=actions
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Matrice Q (Apprentissage)**")
                st.dataframe(q_table.style.background_gradient(cmap='Blues'))
            
            with col2:
                # Simulation d'épisode
                etat_courant = st.selectbox("Segment client actuel:", etats)
                action_choisie = q_table.loc[etat_courant].idxmax()
                
                st.metric("Meilleure action recommandée", action_choisie)
                st.metric("Confiance du modèle", f"{q_table.loc[etat_courant, action_choisie]:.3f}")
                
                # Feedback d'apprentissage
                satisfaction = st.slider("Satisfaction client (récompense):", 0.0, 1.0, 0.8)
                
                if st.button("Mettre à jour l'apprentissage"):
                    # Mise à jour Q-learning simplifiée
                    q_table.loc[etat_courant, action_choisie] = satisfaction
                    st.success("Modèle mis à jour avec le feedback!")
        
        elif ml_type == "Deep Learning":
            st.error("**🧠 Deep Learning : Réseaux de neurones profonds**")
            
            st.markdown("""
            **Applications:**
            - Vision par ordinateur
            - Traitement du langage naturel
            - Reconnaissance vocale
            
            **Cas d'usage:**
            - Classification d'images
            - Traduction automatique
            - Chatbots intelligents
            """)
            
            # Simulation de réseau de neurones
            st.subheader("Architecture de Réseau de Neurones")
            
            layers = st.slider("Nombre de couches cachées", 1, 5, 3)
            neurons = st.slider("Neurones par couche", 10, 100, 50)
            
            st.write(f"**Architecture:** 10 → {' → '.join([str(neurons)] * layers)} → 1")
            st.metric("Complexité du modèle", f"{(10 * neurons + neurons * neurons * (layers-1) + neurons * 1):,} paramètres")
    
    with tab3:
        st.subheader("📊 Visualisation Avancée des Données")
        
        viz_type = st.selectbox(
            "Type de visualisation:",
            ["Analyse Temporelle", "Cartographie", "Network Analysis", "Dashboard Interactif"]
        )
        
        if viz_type == "Analyse Temporelle":
            st.success("**📈 Analyse des Tendances Temporelles**")
            
            # Générer des données temporelles
            _, df_transactions = generer_donnees_retail()
            
            # Agrégation par mois
            df_transactions['mois'] = df_transactions['date'].dt.to_period('M')
            trends = df_transactions.groupby('mois').agg({
                'montant': ['sum', 'count'],
                'client_id': 'nunique'
            }).reset_index()
            
            trends.columns = ['mois', 'ca_total', 'nb_transactions', 'clients_uniques']
            trends['mois'] = trends['mois'].astype(str)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(trends, x='mois', y='ca_total', 
                            title="Évolution du Chiffre d'Affaires Mensuel")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.area(trends, x='mois', y=['nb_transactions', 'clients_uniques'],
                            title="Activité commerciale mensuelle")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Cartographie":
            st.info("**🗺️ Visualisation Géographique et Cartographie**")
            
            # Données géographiques simulées pour le Sénégal
            regions_senegal = {
                'Region': ['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor', 'Kaolack', 'Kolda', 'Matam', 'Fatick', 'Louga'],
                'Latitude': [14.7167, 14.8, 14.75, 16.0167, 12.5833, 14.15, 12.8833, 15.1167, 14.3333, 15.6167],
                'Longitude': [-17.4672, -16.9667, -16.2333, -16.5, -16.2667, -16.0833, -14.95, -13.65, -16.4167, -16.2167],
                'Ventes': [500000, 250000, 180000, 150000, 120000, 100000, 80000, 70000, 60000, 50000],
                'Clients': [15000, 8000, 6000, 5000, 4000, 3500, 3000, 2500, 2000, 1500]
            }
            
            df_geo = pd.DataFrame(regions_senegal)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Carte choroplèthe
                fig = px.scatter_geo(df_geo, 
                                   lat='Latitude', 
                                   lon='Longitude',
                                   size='Ventes',
                                   color='Clients',
                                   hover_name='Region',
                                   scope='africa',
                                   title="Performance Commerciale par Région Sénégal",
                                   size_max=30)
                fig.update_geos(visible=False, resolution=50,
                              showcountries=True, countrycolor="Black",
                              showsubunits=True, subunitcolor="Blue")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Carte de chaleur géographique
                fig = px.density_mapbox(df_geo, 
                                      lat='Latitude', 
                                      lon='Longitude', 
                                      z='Ventes',
                                      radius=20,
                                      center=dict(lat=14.5, lon=-14.5),
                                      zoom=5,
                                      mapbox_style="stamen-terrain",
                                      title="Densité des Ventes par Région")
                st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des flux
            st.subheader("📊 Cartographie des Flux Logistiques")
            
            # Simulation de flux entre régions
            flux_data = {
                'Source': ['Dakar', 'Dakar', 'Thiès', 'Saint-Louis', 'Dakar'],
                'Target': ['Thiès', 'Saint-Louis', 'Diourbel', 'Ziguinchor', 'Kaolack'],
                'Volume': [500, 300, 200, 150, 250],
                'Cout': [10000, 15000, 8000, 20000, 12000]
            }
            
            df_flux = pd.DataFrame(flux_data)
            
            fig = px.line_geo(df_flux,
                            lat=[14.7167, 14.8, 14.75, 16.0167, 12.5833, 14.15],
                            lon=[-17.4672, -16.9667, -16.2333, -16.5, -16.2667, -16.0833],
                            projection="natural earth")
            st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Network Analysis":
            st.warning("**🕸️ Analyse de Réseaux et Relations**")
            
            st.markdown("""
            **Applications:**
            - Analyse des relations clients
            - Détection de communautés
            - Optimisation des réseaux logistiques
            """)
            
            # Simulation d'un réseau social de clients
            np.random.seed(42)
            n_nodes = 30
            
            # Création d'un graph de réseau
            G = nx.erdos_renyi_graph(n_nodes, 0.1)
            pos = nx.spring_layout(G)
            
            # Attributs des nœuds
            for i in range(n_nodes):
                G.nodes[i]['segment'] = np.random.choice(['VIP', 'Fidèle', 'Régulier', 'Occasionnel'])
                G.nodes[i]['valeur'] = np.random.randint(1000, 50000)
            
            # Visualisation avec plotly
            edge_x = []
            edge_y = []
            for edge in G.edges():
                x0, y0 = pos[edge[0]]
                x1, y1 = pos[edge[1]]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])
            
            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.5, color='#888'),
                hoverinfo='none',
                mode='lines')
            
            node_x = []
            node_y = []
            node_text = []
            node_color = []
            for node in G.nodes():
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                node_text.append(f"Client {node}<br>Segment: {G.nodes[node]['segment']}<br>Valeur: {G.nodes[node]['valeur']}€")
                node_color.append(G.nodes[node]['valeur'])
            
            node_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers',
                hoverinfo='text',
                marker=dict(
                    showscale=True,
                    colorscale='YlGnBu',
                    size=10,
                    colorbar=dict(
                        thickness=15,
                        title='Valeur Client',
                        xanchor='left',
                        titleside='right'
                    ),
                    line_width=2))
            
            node_trace.text = node_text
            node_trace.marker.color = node_color
            
            fig = go.Figure(data=[edge_trace, node_trace],
                          layout=go.Layout(
                              title='Réseau des Relations Clients',
                              showlegend=False,
                              hovermode='closest',
                              margin=dict(b=20,l=5,r=5,t=40),
                              annotations=[ dict(
                                  text="Analyse des communautés clients",
                                  showarrow=False,
                                  xref="paper", yref="paper",
                                  x=0.005, y=-0.002 ) ],
                              xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                              yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                          )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Métriques du réseau
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Nombre de nœuds", G.number_of_nodes())
            with col2:
                st.metric("Nombre de liens", G.number_of_edges())
            with col3:
                st.metric("Densité du réseau", f"{nx.density(G):.3f}")
        
        elif viz_type == "Dashboard Interactif":
            st.success("**📱 Tableau de Bord Interactif Temps Réel**")
            
            # Simulation de données temps réel
            st.subheader("📊 Tableau de Bord Commercial Temps Réel")
            
            # Génération de données dynamiques
            np.random.seed(42)
            heures = list(range(24))
            data_temps_reel = {
                'Heure': heures,
                'Visites': np.random.poisson(100, 24) + np.sin(np.array(heures) * np.pi / 12) * 50,
                'Conversions': np.random.poisson(20, 24) + np.sin(np.array(heures) * np.pi / 12) * 10,
                'Chiffre_Affaires': np.random.normal(5000, 1000, 24) + np.sin(np.array(heures) * np.pi / 12) * 2000
            }
            
            df_temps_reel = pd.DataFrame(data_temps_reel)
            
            # Métriques en temps réel
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                visites_actuelles = df_temps_reel['Visites'].iloc[-1]
                st.metric("Visites actuelles", f"{visites_actuelles}", "+5%")
            
            with col2:
                conversions_actuelles = df_temps_reel['Conversions'].iloc[-1]
                st.metric("Conversions", f"{conversions_actuelles}", "+3%")
            
            with col3:
                ca_actuel = df_temps_reel['Chiffre_Affaires'].iloc[-1]
                st.metric("Chiffre d'Affaires", f"{ca_actuel:.0f} €", "+8%")
            
            with col4:
                taux_conversion = (conversions_actuelles / visites_actuelles) * 100
                st.metric("Taux Conversion", f"{taux_conversion:.1f}%", "+0.5%")
            
            # Graphiques interactifs
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(df_temps_reel, x='Heure', y=['Visites', 'Conversions'],
                            title="Activité Commerciale sur 24h")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.area(df_temps_reel, x='Heure', y='Chiffre_Affaires',
                            title="Évolution du Chiffre d'Affaires")
                st.plotly_chart(fig, use_container_width=True)
            
            # Filtres interactifs
            st.subheader("🔧 Filtres Avancés")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                segment_filter = st.multiselect(
                    "Segment client:",
                    ['VIP', 'Fidèle', 'Régulier', 'Occasionnel'],
                    default=['VIP', 'Fidèle']
                )
            
            with col2:
                region_filter = st.selectbox(
                    "Région:",
                    ['Toutes'] + ['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis', 'Ziguinchor']
                )
            
            with col3:
                date_range = st.date_input(
                    "Période:",
                    [datetime(2024, 1, 1), datetime(2024, 12, 31)]
                )
            
            # Alertes et notifications
            st.subheader("🚨 Alertes et Recommandations")
            
            alert_col1, alert_col2, alert_col3 = st.columns(3)
            
            with alert_col1:
                if taux_conversion < 15:
                    st.error("⚠️ Taux de conversion bas")
                else:
                    st.success("✅ Taux de conversion optimal")
            
            with alert_col2:
                if visites_actuelles < 80:
                    st.warning("📉 Traffic faible - Vérifier le référencement")
                else:
                    st.success("📈 Traffic normal")
            
            with alert_col3:
                if ca_actuel < 4000:
                    st.error("💰 CA en baisse - Actions marketing requises")
                else:
                    st.success("💰 CA dans les objectifs")
    
    with tab4:
        st.subheader("🧹 Data Quality - Diagnostic Complet")
        
        df_qualite = generer_donnees_qualite()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Échantillon des données avec problèmes**")
            st.dataframe(df_qualite.head(10))
        
        with col2:
            # Métriques de qualité
            completude = (1 - df_qualite.isnull().mean()) * 100
            validite = pd.Series({
                'email': (df_qualite['email'].str.contains('@', na=False).mean()) * 100,
                'telephone': (df_qualite['telephone'].str.len() == 9).mean() * 100,
                'age': ((df_qualite['age'] >= 18) & (df_qualite['age'] <= 100)).mean() * 100,
                'salaire': (df_qualite['salaire'] > 0).mean() * 100
            })
            
            st.write("**Métriques de Qualité**")
            for col in completude.index:
                st.metric(f"Complétude {col}", f"{completude[col]:.1f}%")
            
            st.write("**Validité des données**")
            for col, score in validite.items():
                st.metric(f"Validité {col}", f"{score:.1f}%")
        
        # Recommandations d'amélioration
        st.subheader("🔧 Plan d'Amélioration de la Qualité")
        
        problems = []
        if completude['email'] < 95:
            problems.append("📧 Implémenter la validation des emails en temps réel")
        if validite['age'] < 95:
            problems.append("🎂 Ajouter des contrôles de plage pour l'âge")
        if completude['ville'] < 95:
            problems.append("🏙️ Utiliser l'autocomplétion pour les villes")
        
        for problem in problems:
            st.write(f"- {problem}")
    
    with tab5:
        st.subheader("🎯 Cas Réels d'Implémentation")
        
        cas = st.selectbox(
            "Choisir un cas réel:",
            ["Netflix - Système de recommandation", 
             "Uber - Optimisation des trajets",
             "Amazon - Détection de fraude",
             "Airbnb - Pricing dynamique",
             "Tesla - Conduite autonome"]
        )
        
        if "Netflix" in cas:
            st.success("**🎬 Netflix : Système de Recommandation Avancé**")
            
            st.markdown("""
            **Challenge :** Personnaliser l'expérience pour 200M+ d'utilisateurs
            **Solution :** Algorithmes de collaborative filtering + Deep Learning
            **Résultats :**
            - 80% du contenu visionné vient des recommandations
            - Réduction du churn de 25%
            - Augmentation du temps de visionnage de 30%
            """)
            
            # Simulation des algorithmes Netflix
            st.subheader("Simulation d'Algorithme de Recommandation")
            
            films = ['Action Hero', 'Romantic Story', 'Sci-Fi Adventure', 'Comedy Night', 'Documentary World']
            user_profiles = {
                'Jeune': [0.9, 0.3, 0.8, 0.7, 0.2],
                'Famille': [0.6, 0.7, 0.5, 0.9, 0.6],
                'Cinéphile': [0.7, 0.8, 0.9, 0.6, 0.9]
            }
            
            profile = st.selectbox("Profil utilisateur:", list(user_profiles.keys()))
            scores = user_profiles[profile]
            
            fig = px.bar(x=films, y=scores, title=f"Recommandations pour profil {profile}",
                       labels={'x': 'Films', 'y': 'Score de recommandation'})
            st.plotly_chart(fig, use_container_width=True)
        
        elif "Uber" in cas:
            st.info("**🚗 Uber : Optimisation des Trajets en Temps Réel**")
            
            st.markdown("""
            **Challenge :** Minimiser les temps d'attente et maximiser l'efficacité des trajets
            **Solution :** Algorithmes de matching + Optimisation de routes en temps réel
            **Résultats :**
            - Réduction temps d'attente moyen de 40%
            - Augmentation du nombre de courses par chauffeur de 25%
            - Optimisation du prix dynamique
            """)
            
            # Simulation d'optimisation de trajets Uber
            st.subheader("Simulation d'Optimisation de Trajets")
            
            # Données de simulation
            np.random.seed(42)
            n_requests = 20
            n_drivers = 15
            
            requests_data = {
                'request_id': range(n_requests),
                'pickup_lat': np.random.uniform(14.6, 14.8, n_requests),
                'pickup_lon': np.random.uniform(-17.5, -17.3, n_requests),
                'dropoff_lat': np.random.uniform(14.6, 14.8, n_requests),
                'dropoff_lon': np.random.uniform(-17.5, -17.3, n_requests),
                'priority': np.random.choice(['Haute', 'Moyenne', 'Basse'], n_requests, p=[0.2, 0.5, 0.3])
            }
            
            drivers_data = {
                'driver_id': range(n_drivers),
                'current_lat': np.random.uniform(14.6, 14.8, n_drivers),
                'current_lon': np.random.uniform(-17.5, -17.3, n_drivers),
                'status': np.random.choice(['Libre', 'En course'], n_drivers, p=[0.6, 0.4])
            }
            
            df_requests = pd.DataFrame(requests_data)
            df_drivers = pd.DataFrame(drivers_data)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Carte des demandes
                fig = px.scatter_mapbox(df_requests, 
                                      lat="pickup_lat", 
                                      lon="pickup_lon",
                                      color="priority",
                                      size_max=15,
                                      zoom=12,
                                      mapbox_style="open-street-map",
                                      title="Demandes de course à Dakar")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Optimisation du matching
                st.write("**Optimisation du Matching Conducteurs-Clients**")
                
                # Algorithme simplifié de matching
                free_drivers = len(df_drivers[df_drivers['status'] == 'Libre'])
                waiting_requests = len(df_requests)
                
                st.metric("Conducteurs disponibles", free_drivers)
                st.metric("Demandes en attente", waiting_requests)
                st.metric("Temps d'attente moyen", "3.2 min")
                st.metric("Taux de matching", "92%")
                
                if st.button("Lancer l'optimisation"):
                    st.success("✅ Matching optimisé !")
                    st.write("""
                    **Résultats de l'optimisation:**
                    - 18 demandes assignées
                    - Temps d'attente moyen réduit à 2.1 min
                    - Distance totale économisée: 15.7 km
                    """)
        
        elif "Amazon" in cas:
            st.error("**📦 Amazon : Détection de Fraude Avancée**")
            
            st.markdown("""
            **Challenge :** Protéger 300M+ de comptes contre la fraude
            **Solution :** Machine Learning temps réel + Analyse comportementale
            **Résultats :**
            - Réduction des fraudes de 75%
            - Faux positifs réduits à moins de 0.1%
            - Économies de 1.2 milliard $ par an
            """)
            
            # Simulation de détection de fraude Amazon
            st.subheader("Simulation de Détection de Fraude")
            
            # Génération de données de transactions
            np.random.seed(42)
            n_transactions = 1000
            
            fraud_data = {
                'transaction_id': range(n_transactions),
                'montant': np.random.exponential(50, n_transactions),
                'distance_domicile': np.random.exponential(10, n_transactions),
                'heure': np.random.randint(0, 24, n_transactions),
                'pays': np.random.choice(['Sénégal', 'France', 'USA', 'Autre'], n_transactions, p=[0.6, 0.2, 0.1, 0.1]),
                'nouveau_merchant': np.random.choice([0, 1], n_transactions, p=[0.7, 0.3])
            }
            
            df_fraud = pd.DataFrame(fraud_data)
            
            # Calcul du score de fraude (modèle simplifié)
            df_fraud['score_fraude'] = (
                (df_fraud['montant'] > 200) * 0.3 +
                (df_fraud['distance_domicile'] > 50) * 0.2 +
                ((df_fraud['heure'] < 6) | (df_fraud['heure'] > 22)) * 0.2 +
                (df_fraud['pays'] == 'Autre') * 0.2 +
                (df_fraud['nouveau_merchant'] == 1) * 0.1 +
                np.random.normal(0, 0.05, n_transactions)
            )
            
            df_fraud['alerte_fraude'] = df_fraud['score_fraude'] > 0.7
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Distribution des scores de fraude
                fig = px.histogram(df_fraud, x='score_fraude', 
                                 color='alerte_fraude',
                                 title="Distribution des Scores de Fraude",
                                 nbins=30)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Métriques de performance
                vraies_alertes = df_fraud['alerte_fraude'].sum()
                taux_fraude = (vraies_alertes / len(df_fraud)) * 100
                
                st.metric("Transactions analysées", f"{n_transactions:,}")
                st.metric("Alertes de fraude", vraies_alertes)
                st.metric("Taux de fraude détecté", f"{taux_fraude:.2f}%")
                st.metric("Précision du modèle", "99.2%")
            
            # Test de transaction suspecte
            st.subheader("🔍 Testez une Transaction")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                montant_test = st.slider("Montant (€)", 1, 500, 100)
                heure_test = st.slider("Heure de la transaction", 0, 23, 12)
            
            with col2:
                distance_test = st.slider("Distance du domicile (km)", 0, 100, 10)
                pays_test = st.selectbox("Pays", ['Sénégal', 'France', 'USA', 'Autre'])
            
            with col3:
                nouveau_merchant_test = st.checkbox("Nouveau marchand")
            
            # Calcul du score
            score_test = (
                (montant_test > 200) * 0.3 +
                (distance_test > 50) * 0.2 +
                ((heure_test < 6) | (heure_test > 22)) * 0.2 +
                (pays_test == 'Autre') * 0.2 +
                nouveau_merchant_test * 0.1
            )
            
            st.metric("Score de risque de fraude", f"{score_test:.2f}")
            
            if score_test > 0.7:
                st.error("🚨 TRANSACTION SUSPECTE - Vérification requise")
                st.write("**Actions recommandées:** Vérification 2FA, Contact client, Retard traitement")
            elif score_test > 0.4:
                st.warning("⚠️ RISQUE MODÉRÉ - Surveillance recommandée")
            else:
                st.success("✅ TRANSACTION NORMALE - Traitement immédiat")
        
        elif "Airbnb" in cas:
            st.warning("**🏠 Airbnb : Pricing Dynamique Intelligent**")
            
            st.markdown("""
            **Challenge :** Optimiser les prix pour 7M+ de logements worldwide
            **Solution :** Machine Learning + Analyse du marché en temps réel
            **Résultats :**
            - Augmentation des revenus des hôtes de 20-40%
            - Amélioration du taux d'occupation de 15%
            - Satisfaction client améliorée
            """)
            
            # Simulation de pricing dynamique Airbnb
            st.subheader("Simulateur de Pricing Dynamique")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Facteurs influençant le prix
                type_logement = st.selectbox("Type de logement", 
                                           ['Appartement', 'Maison', 'Studio', 'Villa'])
                nb_chambres = st.slider("Nombre de chambres", 1, 5, 2)
                equipements = st.multiselect("Équipements",
                                           ['WiFi', 'Piscine', 'Parking', 'Climatisation', 'Cuisine équipée'])
                
            with col2:
                localisation = st.selectbox("Localisation", 
                                          ['Dakar Plateau', 'Almadies', 'Ngor', 'Ouest Foire', 'Sacre Coeur'])
                saison = st.selectbox("Saison", 
                                    ['Basse', 'Moyenne', 'Haute', 'Très haute'])
                evenements = st.checkbox("Événements spéciaux dans la région")
            
            # Calcul du prix optimisé
            prix_base = 50  # Prix de base en €
            
            # Facteurs multiplicatifs
            facteurs = {
                'type_logement': {'Appartement': 1.0, 'Maison': 1.3, 'Studio': 0.8, 'Villa': 2.0},
                'nb_chambres': {1: 0.8, 2: 1.0, 3: 1.3, 4: 1.6, 5: 2.0},
                'localisation': {'Dakar Plateau': 1.2, 'Almadies': 1.5, 'Ngor': 1.4, 'Ouest Foire': 1.0, 'Sacre Coeur': 1.3},
                'saison': {'Basse': 0.7, 'Moyenne': 1.0, 'Haute': 1.5, 'Très haute': 2.0},
                'equipements': len(equipements) * 0.1,
                'evenements': 1.2 if evenements else 1.0
            }
            
            prix_optimise = prix_base * (
                facteurs['type_logement'][type_logement] *
                facteurs['nb_chambres'][nb_chambres] *
                facteurs['localisation'][localisation] *
                facteurs['saison'][saison] *
                (1 + facteurs['equipements']) *
                facteurs['evenements']
            )
            
            # Comparaison avec le marché
            prix_marche = prix_optimise * np.random.uniform(0.8, 1.2)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Prix recommandé", f"{prix_optimise:.0f} €/nuit")
            
            with col2:
                st.metric("Prix moyen marché", f"{prix_marche:.0f} €/nuit")
            
            with col3:
                difference = ((prix_optimise - prix_marche) / prix_marche) * 100
                st.metric("Écart marché", f"{difference:+.1f}%")
            
            # Recommandations
            st.subheader("💡 Recommandations de Pricing")
            
            if difference > 10:
                st.error("Prix TROP ÉLEVÉ - Risque de faible occupation")
                st.write("**Actions:** Réviser à la baisse, Offres promotionnelles")
            elif difference < -10:
                st.warning("Prix TROP BAS - Manque à gagner")
                st.write("**Actions:** Augmenter progressivement, Mettre en valeur les atouts")
            else:
                st.success("Prix OPTIMAL - Bon équilibre")
                st.write("**Actions:** Maintenir la stratégie, Surveiller la concurrence")
            
            # Analyse de sensibilité
            st.subheader("📈 Analyse de Sensibilité au Prix")
            
            prix_test = np.linspace(prix_optimise * 0.5, prix_optimise * 1.5, 10)
            occupation_test = 100 - (prix_test - prix_optimise) / prix_optimise * 50
            occupation_test = np.clip(occupation_test, 10, 95)
            revenu_test = prix_test * occupation_test / 100
            
            df_sensibilite = pd.DataFrame({
                'Prix': prix_test,
                'Taux_Occupation': occupation_test,
                'Revenu_Relatif': revenu_test
            })
            
            fig = px.line(df_sensibilite, x='Prix', y=['Taux_Occupation', 'Revenu_Relatif'],
                         title="Impact du Prix sur l'Occupation et le Revenu",
                         labels={'value': 'Pourcentage', 'variable': 'Métrique'})
            st.plotly_chart(fig, use_container_width=True)
        
        elif "Tesla" in cas:
            st.success("**🚗 Tesla : Conduite Autonome par Deep Learning**")
            
            st.markdown("""
            **Challenge :** Développer une conduite autonome de niveau 4-5
            **Solution :** Réseaux de neurones convolutionnels + Reinforcement Learning
            **Résultats :**
            - 8 milliards de miles parcourus en mode autonome
            - Réduction des accidents de 40%
            - Amélioration continue via learning fédéré
            """)
            
            # Simulation de conduite autonome Tesla
            st.subheader("Simulation de Perception Autonome")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Simulation des capteurs
                st.write("**Données des Capteurs**")
                
                # Radar
                st.metric("Distance véhicule avant", "25.3 m")
                st.metric("Vitesse relative", "-2.1 km/h")
                
                # Caméras
                st.metric("Détection piétons", "3")
                st.metric("Détection véhicules", "5")
                st.metric("Reconnaissance feux", "Vert")
                
                # Lidar
                st.metric("Précision carte 3D", "98.7%")
                st.metric("Points cloud/s", "2.4M")
            
            with col2:
                # Décisions de conduite
                st.write("**Décisions de Conduite**")
                
                vitesses = {
                    'Limite légale': '50 km/h',
                    'Vitesse conseillée': '45 km/h', 
                    'Vitesse actuelle': '43 km/h'
                }
                
                for decision, valeur in vitesses.items():
                    st.metric(decision, valeur)
                
                st.write("**Actions en cours:**")
                st.write("✅ Maintenir la voie")
                st.write("✅ Distance de sécurité")
                st.write("🔄 Adaptation vitesse trafic")
                st.write("✅ Surveillance piétons")
            
            # Simulation d'apprentissage
            st.subheader("🧠 Apprentissage du Modèle Autonome")
            
            # Données d'apprentissage simulées
            learning_data = {
                'Époque': range(1, 101),
                'Précision': np.minimum(0.95, 0.3 + 0.65 * (1 - np.exp(-np.arange(100)/20)) + np.random.normal(0, 0.02, 100)),
                'Perte': np.maximum(0.05, 2.0 * np.exp(-np.arange(100)/15) + np.random.normal(0, 0.1, 100))
            }
            
            df_learning = pd.DataFrame(learning_data)
            
            fig = px.line(df_learning, x='Époque', y=['Précision', 'Perte'],
                         title="Courbe d'Apprentissage du Modèle Autonome",
                         labels={'value': 'Valeur', 'variable': 'Métrique'})
            st.plotly_chart(fig, use_container_width=True)
            
            # Métriques de sécurité
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Kilométrage autonome", "8.2B miles")
            with col2:
                st.metric("Interventions humaines", "1/5M miles")
            with col3:
                st.metric("Fiabilité perception", "99.98%")

# =============================================================================
# SECTION 5: GOUVERNANCE ET BEST PRACTICES
# =============================================================================

def section_gouvernance():
    st.header("🏛️ Gouvernance des Données")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cadre de Gouvernance")
        
        st.markdown("""
        **1. Qualité des Données**
        - Exactitude et complétude
        - Consistance et intégrité
        - Actualité et disponibilité
        
        **2. Sécurité et Confidentialité**
        - Chiffrement des données
        - Contrôle d'accès RBAC
        - Audit et conformité RGPD
        
        **3. Métadonnées et Lineage**
        - Catalogue de données
        - Traçabilité des transformations
        - Documentation automatique
        """)
    
    with col2:
        st.subheader("Évaluation de la Maturité Data")
        
        aspects = {
            "Stratégie Data": st.slider("Stratégie Data", 1, 5, 3),
            "Gouvernance": st.slider("Gouvernance", 1, 5, 2),
            "Qualité": st.slider("Qualité des données", 1, 5, 3),
            "Sécurité": st.slider("Sécurité", 1, 5, 4),
            "Culture Data": st.slider("Culture Data", 1, 5, 2)
        }
        
        if st.button("Calculer le Score de Maturité"):
            score = sum(aspects.values()) / (len(aspects) * 5) * 100
            st.metric("Score de Maturité Data", f"{score:.1f}%")
            
            if score >= 80:
                st.success("🎯 Niveau Expert - Focus optimisation")
            elif score >= 60:
                st.info("📈 Niveau Avancé - Développement capacités")
            elif score >= 40:
                st.warning("📚 Niveau Intermédiaire - Renforcement")
            else:
                st.error("🌱 Niveau Débutant - Construction fondations")

# =============================================================================
# SECTION 6: IMPLÉMENTATION ET ROI
# =============================================================================

def section_implementation():
    st.header("🚀 Implémentation et Calcul de ROI")
    
    st.subheader("Calculateur de ROI Big Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Investissements**")
        cout_infrastructure = st.number_input("Infrastructure (k€)", min_value=10, value=100)
        cout_formation = st.number_input("Formation (k€)", min_value=5, value=30)
        cout_maintenance = st.number_input("Maintenance annuelle (k€)", min_value=10, value=50)
        
        st.write("**Gains Attendus**")
        gain_efficacite = st.slider("Gain d'efficacité (%)", 1, 50, 15)
        augmentation_ventes = st.slider("Augmentation ventes (%)", 1, 30, 10)
        reduction_couts = st.slider("Réduction coûts (%)", 1, 40, 12)
    
    with col2:
        # Calculs ROI
        investissement_total = cout_infrastructure + cout_formation + cout_maintenance
        gains_annuels = (gain_efficacite + augmentation_ventes + reduction_couts) / 3 * investissement_total / 10
        
        roi = (gains_annuels - cout_maintenance) / investissement_total * 100
        payback_period = investissement_total / gains_annuels if gains_annuels > 0 else float('inf')
        
        st.metric("ROI Annuel Estimé", f"{roi:.1f}%")
        st.metric("Période de Retour", f"{payback_period:.1f} ans")
        st.metric("Gains Annuels Nets", f"{gains_annuels - cout_maintenance:.0f} k€")
        
        # Recommandations
        if roi > 50:
            st.success("🎯 ROI Excellent - Projet très attractif")
        elif roi > 20:
            st.info("📈 ROI Bon - Projet recommandé")
        else:
            st.warning("⚠️ ROI Faible - Réévaluer le projet")

# =============================================================================
# APPLICATION PRINCIPALE
# =============================================================================

def main():
    # Sidebar Navigation
    st.sidebar.title("📚 Big Data MBA Complet")
    
    menu_options = [
        "🌍 Introduction au Big Data",
        "🛠️ Technologies et Architectures", 
        "🏢 Cas Pratiques par Secteur",
        "🔬 Science des Données Appliquée",
        "🏛️ Gouvernance et Best Practices",
        "🚀 Implémentation et ROI"
    ]
    
    choix = st.sidebar.radio("Navigation:", menu_options)
    
    # Chargement des données
    df = generer_donnees_big_data()
    
    # Router vers la section sélectionnée
    if choix == menu_options[0]:
        section_introduction()
    elif choix == menu_options[1]:
        section_technologies()
    elif choix == menu_options[2]:
        section_cas_pratiques()
    elif choix == menu_options[3]:
        section_science_donnees()
    elif choix == menu_options[4]:
        section_gouvernance()
    elif choix == menu_options[5]:
        section_implementation()
    
    # Footer avec métriques
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Métriques Globales")
    
    metrics = calculer_metrics_5v(df)
    for metric, value in metrics.items():
        if metric == 'Véracité':
            st.sidebar.metric(metric, f"{value:.1f}%")
        elif metric == 'Valeur':
            st.sidebar.metric(metric, f"{value:.2f}")
        else:
            st.sidebar.metric(metric, f"{value:,.0f}")





if __name__ == "__main__":
    main()
