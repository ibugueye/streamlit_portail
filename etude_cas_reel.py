import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def section_etudes_cas_reels():
    st.header("🏢 Études de Cas Réels par Secteur")
    
    secteur = st.selectbox(
        "Sélectionnez un secteur:",
        [
            "🏥 Santé & Médical",
            "🏦 Finance & Banque", 
            "🛒 Retail & Commerce",
            "📞 Télécommunications",
            "🚚 Transport & Logistique",
            "⚡ Énergie & Utilities"
        ]
    )
    
    if secteur == "🏥 Santé & Médical":
        etudes_cas_sante()
    elif secteur == "🏦 Finance & Banque":
        etudes_cas_finance()
    elif secteur == "🛒 Retail & Commerce":
        etudes_cas_retail()
    elif secteur == "📞 Télécommunications":
        etudes_cas_telecom()
    elif secteur == "🚚 Transport & Logistique":
        etudes_cas_transport()
    elif secteur == "⚡ Énergie & Utilities":
        etudes_cas_energie()

def etudes_cas_sante():
    st.subheader("🏥 Études de Cas Réels - Secteur Santé")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "🎯 Mayo Clinic - Diagnostic IA du Cancer",
            "💊 Pfizer - R&D Accélérée par l'IA",
            "🏥 Kaiser Permanente - Télémédecine Intelligente",
            "🔬 Google Health - Dépistage Rétinopathie",
            "📊 NHS UK - Prédiction Pandémies"
        ]
    )
    
    if cas == "🎯 Mayo Clinic - Diagnostic IA du Cancer":
        st.markdown("""
        ### 🎯 Mayo Clinic - Diagnostic IA du Cancer du Sein
        
        **📊 Contexte:**
        - 2ème cancer le plus fréquent chez les femmes
        - 1 radiologue peut analyser 50-100 mammographies/jour
        - Risque d'erreur humaine: 10-30% des cas
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** CNN (ResNet-50) + Transfer Learning
        - **Données:** 200,000+ mammographies annotées
        - **Stack:** TensorFlow, DICOM, PACS intégration
        - **Traitement:** Analyse pattern micro-calcifications
        
        **📈 Résultats:**
        - **Précision diagnostic:** 94.5% vs 88.2% humain
        - **Temps analyse:** 1.2 secondes vs 3-5 minutes
        - **Détection précoce:** 6-8 mois plus tôt
        - **Réduction erreurs:** 67%
        
        **💰 Impact Business:**
        - Économies: $15M/an en réduction ré-interventions
        - Capacité: +300% de patients traités
        - Satisfaction patients: +35 points
        """)
        
        # Visualisation résultats
        data = {
            'Métrique': ['Précision', 'Temps analyse', 'Détection précoce', 'Réduction erreurs'],
            'Humain': [88.2, 240, 0, 0],
            'IA': [94.5, 1.2, 6, 67]
        }
        df = pd.DataFrame(data)
        fig = px.bar(df, x='Métrique', y=['Humain', 'IA'], barmode='group', 
                    title="Comparaison Performance Humain vs IA")
        st.plotly_chart(fig, use_container_width=True)
        
    elif cas == "💊 Pfizer - R&D Accélérée par l'IA":
        st.markdown("""
        ### 💊 Pfizer - R&D Accélérée pour Vaccin COVID-19
        
        **📊 Contexte:**
        - Développement vaccin traditionnel: 5-10 ans
        - Urgence pandémique COVID-19
        - 100,000+ composés à tester
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Reinforcement Learning + Molecular Dynamics
        - **Données:** 2.5PB données génomiques + essais cliniques
        - **Stack:** AWS Batch, Schrӧdinger Suite, AlphaFold
        - **Traitement:** Simulation 50,000 molécules/heure
        
        **📈 Résultats:**
        - **Temps développement:** 9 mois vs 5-10 ans
        - **Efficacité vaccin:** 95% démontrée
        - **Coût R&D:** $2B vs $5-10B typique
        - **Molécules testées:** 15,000+/jour vs 100/jour
        
        **💰 Impact Business:**
        - Revenus: $36B première année
        - Vies sauvées: 20+ millions estimées
        - Innovation: 8 brevets déposés
        - Leadership: Position dominante marché
        """)

def etudes_cas_finance():
    st.subheader("🏦 Études de Cas Réels - Secteur Finance")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "🔍 JPMorgan Chase - Détection Fraude COIN",
            "📊 American Express - Scoring Crédit 2.0",
            "💳 Visa - Anti-Fraud Network",
            "🏦 HSBC - Compliance Automatisée",
            "📈 BlackRock - Aladdin Risk Analytics"
        ]
    )
    
    if cas == "🔍 JPMorgan Chase - Détection Fraude COIN":
        st.markdown("""
        ### 🔍 JPMorgan Chase - COIN (Contract Intelligence)
        
        **📊 Contexte:**
        - 12,000 contrats crédit commercial/an
        - 360,000 heures avocats/an pour révision
        - Erreurs humaines: $250M/an en pertes
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** NLP (BERT) + Computer Vision
        - **Données:** 1.2M contrats historiques + régulations
        - **Stack:** Apache Spark, TensorFlow, Kubernetes
        - **Traitement:** Analyse 12,000 clauses types
        
        **📈 Résultats:**
        - **Temps traitement:** secondes vs 360,000 heures
        - **Précision extraction:** 99.7% vs 85% humain
        - **Erreurs réduites:** 95%
        - **Couverture réglementaire:** 100% vs 80%
        
        **💰 Impact Business:**
        - Économies: $12M/an en frais légaux
        - Productivité: +400% équipes compliance
        - Risques: Réduction litiges de 75%
        - Innovation: 15 nouveaux produits lancés
        """)
        
        # Métriques de performance
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Contrats/jour", "1,200", "+900%")
        with col2:
            st.metric("Précision", "99.7%", "+14.7%")
        with col3:
            st.metric("Économies", "$12M/an", "ROI: 450%")
        with col4:
            st.metric("Litiges", "-75%", "$45M économisés")
            
    elif cas == "📊 American Express - Scoring Crédit 2.0":
        st.markdown("""
        ### 📊 American Express - Scoring avec Données Alternatives
        
        **📊 Contexte:**
        - 25% population US sans score crédit traditionnel
        - Perte marché: $150B/an en crédit non accordé
        - Modèles FICO limités (5-10 variables)
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** XGBoost + SHAP explicability
        - **Données:** 2,000+ variables (réseaux sociaux, historique paiements mobiles)
        - **Stack:** Hadoop, HBase, Spark MLlib
        - **Traitement:** 10M décisions crédit/jour
        
        **📈 Résultats:**
        - **Couverture population:** 95% vs 75%
        - **Précision défaut:** 89% vs 72% FICO
        - **Décisions:** 2 secondes vs 3 jours
        - **Inclusion financière:** +45M Américains
        
        **💰 Impact Business:**
        - Revenus additionnels: $4.2B/an
        - Défauts réduits: 28%
        - Satisfaction client: +35 points NPS
        - Part marché: +8% segments émergents
        """)

def etudes_cas_retail():
    st.subheader("🛒 Études de Cas Réels - Retail & Commerce")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "🎯 Amazon - Système Recommandation",
            "📦 Walmart - Supply Chain AI",
            "💰 Uber - Pricing Dynamique",
            "🏪 Starbucks - Personalisation",
            "📱 Alibaba - Singles' Day Optimization"
        ]
    )
    
    if cas == "🎯 Amazon - Système Recommandation":
        st.markdown("""
        ### 🎯 Amazon - Engine de Recommandation Personnalisée
        
        **📊 Contexte:**
        - 300+ millions clients actifs
        - 12+ millions produits catalogue
        - 5+ milliards interactions jour
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Collaborative Filtering + Deep Learning
        - **Données:** Historique clicks, achats, recherches, temps de vue
        - **Stack:** AWS SageMaker, DynamoDB, Apache Flink
        - **Traitement:** 100TB données/jour, <100ms latence
        
        **📈 Résultats:**
        - **Ventes générées:** 35% du chiffre d'affaires
        - **Précision recommandation:** 85% click-through rate
        - **Panier moyen:** +28% vs non-personnalisé
        - **Conversion:** +45% pour utilisateurs engagés
        
        **💰 Impact Business:**
        - CA additionnel: $25B+/an
        - Rétention client: +25% sur 12 mois
        - Acquisition coût: -40% vs marketing traditionnel
        - Satisfaction: 4.7/5 étoiles personalisation
        """)
        
        # Graphique impact recommandations
        data = {
            'Source': ['Recherche directe', 'Recommandations', 'Marketing', 'Autres'],
            'Pourcentage': [35, 35, 20, 10]
        }
        df = pd.DataFrame(data)
        fig = px.pie(df, values='Pourcentage', names='Source', 
                    title="Sources du Chiffre d'Affaires Amazon")
        st.plotly_chart(fig, use_container_width=True)
        
    elif cas == "📦 Walmart - Supply Chain AI":
        st.markdown("""
        ### 📦 Walmart - Supply Chain Intelligente
        
        **📊 Contexte:**
        - 4,700 magasins aux USA
        - 150+ centres distribution
        - 1.5M employés
        - 2.5PB données/heure de transactions
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Time Series Forecasting + Reinforcement Learning
        - **Données:** Ventes, météo, trends sociaux, données transport
        - **Stack:** Hadoop, Spark, Kafka, TensorFlow
        - **Traitement:** Prévision demande 8 semaines à l'avance
        
        **📈 Résultats:**
        - **Précision prévision:** 98% vs 85% précédent
        - **Rupture stock:** -90% sur produits clés
        - **Coûts logistiques:** -15%
        - **Frais obsolescence:** -60%
        
        **💰 Impact Business:**
        - Économies: $15B/an sur la supply chain
        - Satisfaction client: 95% disponibilité produits
        - Réduction gaspillage: 450,000 tonnes/an
        - Optimisation inventaire: $3B libérés
        """)

def etudes_cas_telecom():
    st.subheader("📞 Études de Cas Réels - Télécommunications")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "📱 T-Mobile - Customer Experience IA",
            "🚨 Verizon - Détection Fraude Réseau",
            "📊 AT&T - Optimisation 5G",
            "🎯 Vodafone - Marketing Prédictif",
            "🌐 China Mobile - Smart Network"
        ]
    )
    
    if cas == "📱 T-Mobile - Customer Experience IA":
        st.markdown("""
        ### 📱 T-Mobile - Service Client Intelligent
        
        **📊 Contexte:**
        - 100M+ clients USA
        - 500,000 appels service client/jour
        - Coût appel: $5-7 vs $0.10 chatbot
        - Attente moyenne: 8 minutes
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** NLP (GPT-4) + Sentiment Analysis
        - **Données:** Historique appels, tickets, feedback, usage réseau
        - **Stack:** Google Dialogflow, AWS Lex, Salesforce Einstein
        - **Traitement:** 85% requêtes résolues automatiquement
        
        **📈 Résultats:**
        - **Résolution automatique:** 85% vs 15% précédent
        - **Temps attente:** 45 secondes vs 8 minutes
        - **Coût contact:** $0.35 vs $5.50
        - **Satisfaction client:** 4.6/5 vs 3.8/5
        
        **💰 Impact Business:**
        - Économies: $350M/an service client
        - Productivité: +300% agents humains
        - Rétention client: +18% sur 6 mois
        - NPS: +25 points
        """)
        
        # Métriques service client
        metrics = {
            'Avant IA': [15, 480, 5.50, 3.8],
            'Après IA': [85, 45, 0.35, 4.6]
        }
        index = ['Résolution auto (%)', 'Temps attente (sec)', 'Coût/contact ($)', 'Satisfaction (/5)']
        df = pd.DataFrame(metrics, index=index)
        st.dataframe(df.style.format("{:.1f}"), use_container_width=True)
        
    elif cas == "🚨 Verizon - Détection Fraude Réseau":
        st.markdown("""
        ### 🚨 Verizon - Détection Fraude en Temps Réel
        
        **📊 Contexte:**
        - 150M+ lignes mobiles
        - 500M+ événements réseau/jour
        - Fraude: $3B+/an pertes industrie
        - SIM swapping: +400% en 2 ans
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Graph Neural Networks + Anomaly Detection
        - **Données:** CDR, usage data, localisation, IMEI patterns
        - **Stack:** Apache Kafka, Flink, Neo4j, Redis
        - **Traitement:** 100,000 événements/seconde, <50ms décision
        
        **📈 Résultats:**
        - **Détection fraude:** 99.2% vs 75% précédent
        - **Temps réponse:** 50ms vs 24-48 heures
        - **Faux positifs:** 0.8% vs 15%
        - **Fraude prévenue:** $450M/an
        
        **💰 Impact Business:**
        - ROI: 900% sur 3 ans
        - Sécurité: 99.9% clients protégés
        - Conformité: 100% régulations FCC
        - Confiance marque: +40% perception sécurité
        """)

def etudes_cas_transport():
    st.subheader("🚚 Études de Cas Réels - Transport & Logistique")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "🚛 UPS - ORION Route Optimization",
            "📦 FedEx - SenseAware Tracking",
            "🚗 Uber - ETA Prédictif",
            "🚆 SNCF - Maintenance Prédictive",
            "✈️ DHL - Global Forwarding AI"
        ]
    )
    
    if cas == "🚛 UPS - ORION Route Optimization":
        st.markdown("""
        ### 🚛 UPS - ORION (On-Road Integrated Optimization and Navigation)
        
        **📊 Contexte:**
        - 100,000+ véhicules worldwide
        - 20M+ colis/jour
        - 400M miles/an économisables
        - 1 mile économisé = $50M/an
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Genetic Algorithms + Constraint Programming
        - **Données:** Traffic historique, commandes, contraintes livraison
        - **Stack:** Google OR-Tools, Hadoop, Spark
        - **Traitement:** 200,000+ routes optimisées/jour
        
        **📈 Résultats:**
        - **Distance réduite:** 8-10% par tournée
        - **Carburant économisé:** 10M gallons/an
        - **CO2 réduit:** 100,000 tonnes métriques/an
        - **Livraisons/jour:** +5-8 par chauffeur
        
        **💰 Impact Business:**
        - Économies: $400M+/an
        - Productivité: +35% capacité réseau
        - Satisfaction client: 98.5% à temps
        - Durabilité: 25% réduction empreinte carbone
        """)
        
        # Impact environnemental
        data = {
            'Année': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
            'CO2 réduit (tonnes)': [25000, 45000, 65000, 80000, 90000, 95000, 100000],
            'Économies ($M)': [150, 220, 290, 340, 380, 395, 400]
        }
        df = pd.DataFrame(data)
        fig = px.line(df, x='Année', y=['CO2 réduit (tonnes)', 'Économies ($M)'], 
                     title="Progression Impact ORION")
        st.plotly_chart(fig, use_container_width=True)
        
    elif cas == "📦 FedEx - SenseAware Tracking":
        st.markdown("""
        ### 📦 FedEx - SenseAware Tracking Intelligent
        
        **📊 Contexte:**
        - 15M+ colis/jour worldwide
        - 30% colis sensibles (médicaux, high-value)
        - $2B+/an pertes et dommages
        - 15% délais imprévus
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** IoT Analytics + Predictive Maintenance
        - **Données:** Capteurs température, humidité, choc, localisation
        - **Stack:** AWS IoT, Snowflake, Tableau, Machine Learning
        - **Traitement:** 5M+ données capteurs/heure
        
        **📈 Résultats:**
        - **Visibilité:** 100% colis sensibles
        - **Alertes précoces:** 2+ heures avant incidents
        - **Dommages réduits:** 65%
        - **Délais réduits:** 45%
        
        **💰 Impact Business:**
        - Économies: $350M/an réduction dommages
        - Prime pricing: +25% pour services surveillés
        - Satisfaction client: 99.2% colis intacts
        - Conformité: 100% régulations pharma
        """)

def etudes_cas_energie():
    st.subheader("⚡ Études de Cas Réels - Énergie & Utilities")
    
    cas = st.selectbox(
        "Sélectionnez un cas:",
        [
            "🔧 General Electric - Predix Platform",
            "💰 Shell - Trading Algorithmique",
            "🌞 Enel - Smart Grid Optimization",
            "⚡ EDF - Maintenance Prédictive",
            "🔋 Tesla - Autobidder Energy Trading"
        ]
    )
    
    if cas == "🔧 General Electric - Predix Platform":
        st.markdown("""
        ### 🔧 General Electric - Predix IIoT Platform
        
        **📊 Contexte:**
        - 2,000+ turbines gaz worldwide
        - 1 heure arrêt turbine = $50,000 pertes
        - Maintenance préventive: 30% trop tôt, 20% trop tard
        - 99.9% disponibilité requise
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Digital Twin + Predictive Analytics
        - **Données:** 50M+ points données/capteurs, historique maintenance
        - **Stack:** Pivotal Cloud Foundry, Predix, Time Series DB
        - **Traitement:** 1PB données/jour, 10,000+ assets monitorés
        
        **📈 Résultats:**
        - **Disponibilité turbines:** 99.95% vs 98.5%
        - **Maintenance optimisée:** 25% coûts réduits
        - **Pannes évitées:** 85% détectées 30+ jours à l'avance
        - **Efficacité énergétique:** +3.5%
        
        **💰 Impact Business:**
        - Revenus services: $12B+/an
        - Économies clients: $1.2B/an maintenance
        - Durée vie équipements: +15%
        - Émissions CO2: -15% par MWh
        """)
        
        # Impact maintenance
        data = {
            'Type Maintenance': ['Corrective', 'Préventive', 'Prédictive'],
            'Coût Relatif': [100, 60, 35],
            'Disponibilité (%)': [95, 98, 99.5],
            'Pannes Inattendues (%)': [25, 10, 2]
        }
        df = pd.DataFrame(data)
        fig = px.bar(df, x='Type Maintenance', y=['Coût Relatif', 'Disponibilité (%)', 'Pannes Inattendues (%)'],
                    title="Comparaison Stratégies Maintenance")
        st.plotly_chart(fig, use_container_width=True)
        
    elif cas == "💰 Shell - Trading Algorithmique":
        st.markdown("""
        ### 💰 Shell - Global Energy Trading AI
        
        **📊 Contexte:**
        - 13M barils pétrole/jour trading
        - 150+ pays opérations
        - 10,000+ transactions/jour
        - Volatilité prix: 5-20%/jour
        
        **🤖 Solution Big Data:**
        - **Algorithmes:** Reinforcement Learning + Market Microstructure
        - **Données:** Prix spot, futures, géopolitique, météo, stocks
        - **Stack:** QuantConnect, AWS, proprietary algorithms
        - **Traitement:** 1M+ décisions trading/jour, <1ms latence
        
        **📈 Résultats:**
        - **P&L trading:** +28% vs traders humains
        - **Exécution:** 0.8% spread amélioration
        - **Risque réduit:** VaR -35%
        - **Efficacité opérationnelle:** +45%
        
        **💰 Impact Business:**
        - Profits additionnels: $2.5B+/an
        - Réduction risques: $850M Value-at-Risk
        - Liquidité: 25% meilleure exécution
        - Conformité: 100% surveillance automatique
        """)

# Fonction principale
def main():
    st.set_page_config(
        page_title="Études de Cas Réels Big Data",
        page_icon="🏢",
        layout="wide"
    )
    
    st.title("🏢 Études de Cas Réels Big Data par Secteur")
    st.markdown("### Cas concrets d'implémentation avec résultats business mesurés")
    
    section_etudes_cas_reels()
    
    # Insights clés
    st.sidebar.markdown("---")
    st.sidebar.header("📈 Insights Clés")
    st.sidebar.markdown("""
    **🎯 Patterns Communs de Succès:**
    - ROI moyen: 300-900% sur 3 ans
    - Temps développement: 6-18 mois
    - Données utilisées: 80% existantes, 20% nouvelles
    - Skills requis: 60% technique, 40% métier
    
    **🚀 Facteurs Critiques:**
    - Sponsorship executive fort
    - Data quality foundation
    - Agile methodology
    - Cross-functional teams
    
    **💰 Impact Business Typique:**
    - Réduction coûts: 15-40%
    - Augmentation revenus: 10-35%
    - Amélioration satisfaction: 20-50 points
    - Innovation accélérée: 2-5x
    """)

if __name__ == "__main__":
    main()