import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Cas Pratiques Avancés par Secteur",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sector-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">📊 Cas Pratiques Avancés par Secteur</h1>', unsafe_allow_html=True)
    
    # Navigation par secteur
    secteur = st.sidebar.selectbox(
        "🎯 Choisir un Secteur",
        [
            "🏥 Santé & Médical",
            "🏦 Finance & Banque", 
            "🛒 Retail & Commerce",
            "📞 Télécommunications",
            "🚚 Transport & Logistique",
            "⚡ Énergie & Utilities",
            "📚 Introduction Big Data"
        ]
    )
    
    # Affichage du secteur sélectionné
    st.sidebar.markdown(f"**Secteur actuel:** {secteur}")
    
    # Router vers le bon secteur
    if secteur == "🏥 Santé & Médical":
        section_sante_complete()
    elif secteur == "🏦 Finance & Banque":
        section_finance_complete()
    elif secteur == "🛒 Retail & Commerce":
        section_retail_complete()
    elif secteur == "📞 Télécommunications":
        section_telecom_complete()
    elif secteur == "🚚 Transport & Logistique":
        section_transport_complete()
    elif secteur == "⚡ Énergie & Utilities":
        section_energie_complete()
    elif secteur == "📚 Introduction Big Data":
        section_bigdata_intro()

# =============================================================================
# SECTION SANTÉ
# =============================================================================

def section_sante_complete():
    st.header("🏥 Secteur Santé - Applications Big Data")
    
    # Tableau de bord santé
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Consultations à Distance", "35%", "+15% vs 2023")
    with col2:
        st.metric("Économies Réalisées", "2.5M €", "+28%")
    with col3:
        st.metric("Satisfaction Patients", "4.5/5", "Stable")
    with col4:
        st.metric("Patients Monitorés", "12,458", "+42%")
    
    # Sous-sections
    tab1, tab2, tab3, tab4 = st.tabs(["🔮 Analytics Prédictif", "💊 Gestion Ressources", "🏥 Télémédecine", "🔬 Recherche"])
    
    with tab1:
        st.subheader("Calculateur de Risque Cardio-Vasculaire")
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Âge", 30, 80, 50)
            pression = st.slider("Pression artérielle", 110, 180, 130)
        with col2:
            cholesterol = st.slider("Cholestérol", 150, 300, 200)
            tabac = st.checkbox("Fumeur")
        
        if st.button("Calculer le risque"):
            risque = age * 0.5 + (pression - 120) * 0.15 + (cholesterol - 200) * 0.1
            if tabac:
                risque += 10
            risque = min(40, max(1, int(risque)))
            st.success(f"**Risque estimé: {risque}%**")
    
    with tab2:
        st.subheader("Optimisation Charge de Travail")
        medecins = ['Dr. Martin', 'Dr. Dubois', 'Dr. Leclerc']
        charge = [85, 92, 78]
        for medecin, charge in zip(medecins, charge):
            st.progress(charge/100, text=f"{medecin}: {charge}%")
    
    with tab3:
        st.subheader("Applications Télémédecine")
        applications = [
            "📱 Surveillance à Distance - Réduction hospitalisations 30%",
            "🩺 Diagnostic Assisté IA - Précision +25%", 
            "🔬 Recherche Clinique - Accélération découvertes 50%",
            "🛡️ Prévention Personnalisée - Santé population +20%"
        ]
        for app in applications:
            st.markdown(f"- {app}")
    
    with tab4:
        st.subheader("Innovations Recherche")
        st.markdown("""
        - **🧬 Médecine Génomique** - Prédiction risque 5-10 ans à l'avance
        - **🤖 Robotique Médicale** - Précision chirurgicale +45%
        - **🌐 Santé Digitale** - Expérience patient seamless
        """)

# =============================================================================
# SECTION FINANCE
# =============================================================================

def section_finance_complete():
    st.header("🏦 Secteur Finance - Applications Big Data")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Détection Fraude", "98.5%", "+5.2%")
    with col2:
        st.metric("Score Précision", "92.3%", "+3.1%")
    with col3:
        st.metric("Temps Réponse", "50ms", "-20ms")
    with col4:
        st.metric("Économies", "15M €", "+28%")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Détection Fraude", "📊 Scoring Crédit", "📋 Conformité", "⚠️ Gestion Risques"])
    
    with tab1:
        st.subheader("Détection de Fraude en Temps Réel")
        col1, col2 = st.columns(2)
        with col1:
            montant = st.slider("Montant Transaction (€)", 1, 10000, 500)
            localisation = st.selectbox("Localisation", ["Local", "International"])
        with col2:
            heure = st.selectbox("Heure", ["Jour", "Nuit"])
            comportement = st.select_slider("Comportement", ["Normal", "Suspect", "Très Suspect"])
        
        risque_fraude = calcul_risque_fraude(montant, localisation, heure, comportement)
        st.plotly_chart(create_fraud_gauge(risque_fraude), use_container_width=True)
    
    with tab2:
        st.subheader("Scoring Crédit Avancé")
        st.info("**Algorithmes:** XGBoost, LightGBM, SHAP pour l'explicabilité")
        st.markdown("""
        - **Données alternatives** utilisées: 15+ sources
        - **Précision améliorée:** +25% vs méthodes traditionnelles  
        - **Temps décision:** 2 secondes vs 3 jours
        """)
    
    with tab3:
        st.subheader("Conformité Automatisée")
        st.success("**Résultats:** 40% réduction coûts compliance")
        st.markdown("""
        - Surveillance 500M+ transactions/jour
        - Rapports automatiques BCBS 239, MiFID II
        - NLP pour analyse documents réglementaires
        """)
    
    with tab4:
        st.subheader("Gestion des Risques")
        st.warning("**Value at Risk (VaR)** calculée sur 50,000+ positions")
        st.markdown("""
        - Stress testing 200+ scénarios quotidien
        - Analyse portefeuille temps réel
        - Optimisation capital réglementaire
        """)

def calcul_risque_fraude(montant, localisation, heure, comportement):
    risque = 0
    if montant > 5000:
        risque += 30
    if localisation == "International":
        risque += 25
    if heure == "Nuit":
        risque += 20
    if comportement == "Suspect":
        risque += 15
    elif comportement == "Très Suspect":
        risque += 30
    return min(100, risque)

def create_fraud_gauge(risque):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risque,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risque de Fraude"},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}],
        }))
    return fig

# =============================================================================
# SECTION RETAIL
# =============================================================================

def section_retail_complete():
    st.header("🛒 Retail & Commerce - Applications Big Data")
    
    # Métriques e-commerce
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Recommandations", "35% des ventes", "+8%")
    with col2:
        st.metric("Panier Moyen", "85 €", "+15 €")
    with col3:
        st.metric("Conversion", "4.2%", "+1.1%")
    with col4:
        st.metric("Satisfaction", "4.3/5", "+0.4")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Recommandations", "📦 Stocks", "💰 Pricing", "🗺️ Parcours Client"])
    
    with tab1:
        st.subheader("Système de Recommandation")
        st.markdown("""
        **Algorithmes utilisés:**
        - Filtrage collaboratif (User-Based, Item-Based)
        - Content-Based Filtering
        - Hybrid Approaches
        - Deep Learning pour embeddings
        """)
        
        # Exemple interactif
        st.subheader("Simulateur de Recommandation")
        historique = st.multiselect("Historique d'achat", 
                                  ["Smartphone", "Casque Audio", "Montre Connectée", "Tablette"])
        if historique:
            st.success("**Recommandations:** Haut-parleur intelligent, Chargeur sans fil, Écouteurs Bluetooth")
    
    with tab2:
        st.subheader("Optimisation des Stocks")
        st.info("**Résultats:** Réduction rupture stock 40%")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Stock Moyen", "45 jours", "-8 jours")
        with col2:
            st.metric("Rotation", "8.1x", "+1.5x")
    
    with tab3:
        st.subheader("Pricing Dynamique")
        st.warning("**Impact:** Maximisation marge 8-12%")
        st.markdown("""
        - Analyse concurrentielle temps réel
        - Elasticité prix/demande
        - Reinforcement Learning pour optimisation
        """)
    
    with tab4:
        st.subheader("Analyse Parcours Client")
        st.success("**Résultats:** Augmentation conversion 20-35%")
        st.markdown("""
        - Tracking multi-canal
        - Attribution modeling
        - Optimisation expérience client
        """)

# =============================================================================
# SECTION TÉLÉCOM
# =============================================================================

def section_telecom_complete():
    st.header("📞 Secteur Télécom - Applications Big Data")
    
    # Tableau de bord
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Clients", "1,000", "+5%")
    with col2:
        st.metric("Satisfaction", "5.5/10", "-0.2")
    with col3:
        st.metric("Data moyenne", "19.6 Go", "+2.1 Go")
    with col4:
        st.metric("Facture moyenne", "25.2 €", "+1.5 €")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📱 Analyse Clients", "🎯 Marketing", "🚨 Fraude", "📊 Performance"])
    
    with tab1:
        st.subheader("Segmentation Clients")
        segments = {
            "📊 Faibles Utilisateurs": "253 clients - Satisfaction: 5.6/10",
            "📱 Utilisateurs Data": "298 clients - Data: 14.7 Go", 
            "📞 Utilisateurs Voix": "164 clients - Facture: 24.6 €"
        }
        for segment, desc in segments.items():
            with st.expander(segment):
                st.write(desc)
    
    with tab2:
        st.subheader("Stratégies de Fidélisation")
        risque = st.selectbox("Niveau de risque client", ["Faible", "Moyen", "Élevé"])
        if risque == "Faible":
            st.success("**606 clients** - Offres fidélité, parrainage")
        elif risque == "Moyen":
            st.warning("**383 clients** - Contact proactif, offres personnalisées")
        else:
            st.error("**11 clients** - Intervention immédiate, offres promotionnelles")
    
    with tab3:
        st.subheader("Détection de Fraude")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Seuil data anormale", "46.1 Go")
            st.metric("Clients suspects", "140")
        with col2:
            st.metric("Seuil appels anormaux", "319 min")
            st.metric("Seuil SMS anormaux", "39")
    
    with tab4:
        st.subheader("Performance Réseau")
        st.metric("Couverture 4G/5G", "98.2%", "+0.5%")
        st.metric("Débit moyen", "87.4 Mbps", "+12.3 Mbps")

# =============================================================================
# SECTION TRANSPORT
# =============================================================================

def section_transport_complete():
    st.header("🚚 Transport & Logistique - Applications Big Data")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Retard moyen", "2.0 h", "+0.3 h")
    with col2:
        st.metric("Livraison à temps", "36.6%", "-5.2%")
    with col3:
        st.metric("Coût moyen", "258.6 €", "+12.4 €")
    with col4:
        st.metric("Satisfaction", "5.0/10", "-0.5")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📦 Performance", "🚛 Optimisation", "📊 Prédictif", "🔧 Flotte"])
    
    with tab1:
        st.subheader("Performance par Région")
        regions = ['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis']
        performance = [45.2, 38.7, 32.1, 28.9]
        fig = px.bar(x=regions, y=performance, title="Taux Livraison à Temps par Région")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Optimisation d'Itinéraire")
        col1, col2 = st.columns(2)
        with col1:
            livraisons = st.slider("Nombre livraisons", 5, 50, 15)
            capacite = st.slider("Capacité véhicule (kg)", 500, 2000, 1000)
        with col2:
            trafic = st.select_slider("Trafic", ["Faible", "Moyen", "Élevé"])
            meteo = st.select_slider("Météo", ["Bonnes", "Moyennes", "Mauvaises"])
        
        if st.button("Optimiser"):
            distance = livraisons * 8
            temps = livraisons * 0.5
            cout = livraisons * 15
            st.success(f"**Résultat:** {distance} km, {temps} h, {cout} €")
    
    with tab3:
        st.subheader("Calculateur Risque Retard")
        distance = st.slider("Distance (km)", 10, 500, 150)
        poids = st.slider("Poids (kg)", 1, 1000, 300)
        risque = min(100, distance * 0.1 + poids * 0.05)
        st.plotly_chart(create_risk_gauge(risque), use_container_width=True)
    
    with tab4:
        st.subheader("Gestion de Flotte")
        st.metric("Taux utilisation", "78.5%", "+5.2%")
        st.metric("Consommation carburant", "12.4 L/100km", "-0.8 L")

def create_risk_gauge(risque):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risque,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risque de Retard"},
        gauge={'axis': {'range': [None, 100]}}))
    return fig

# =============================================================================
# SECTION ÉNERGIE
# =============================================================================

def section_energie_complete():
    st.header("⚡ Secteur Énergie - Applications Big Data")
    
    # Métriques énergie
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Consommation", "1002 MWh/j", "+45 MWh")
    with col2:
        st.metric("Pic", "1687 MWh", "+123 MWh")
    with col3:
        st.metric("Production", "1013 MWh/j", "+38 MWh")
    with col4:
        st.metric("Couverture", "101.1%", "+1.2%")
    with col5:
        st.metric("Équilibre", "11 MWh/j", "+3 MWh")
    with col6:
        st.metric("Prix moyen", "49.9 €/MWh", "-2.1 €")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Production", "🔧 Maintenance", "💰 Marché", "🌞 Smart Grid"])
    
    with tab1:
        st.subheader("Mix Énergétique")
        sources = ['Solaire', 'Éolien', 'Gaz', 'Charbon', 'Nucléaire']
        production = [120, 180, 250, 150, 280]
        fig = px.pie(values=production, names=sources, title="Répartition Production")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Calculateur Risque Panne")
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Âge équipement (ans)", 1, 30, 8)
            temperature = st.slider("Température (°C)", 40, 100, 75)
        with col2:
            vibrations = st.slider("Vibrations", 1.0, 5.0, 2.5)
            isolation = st.slider("Isolation (%)", 50, 100, 80)
        
        risque = age * 1.5 + (temperature - 40) * 0.3 + (vibrations - 1) * 10 + (100 - isolation) * 0.2
        risque = min(100, max(0, int(risque)))
        
        if risque < 30:
            st.success(f"Risque: {risque}% - FAIBLE")
        elif risque < 70:
            st.warning(f"Risque: {risque}% - MODÉRÉ")
        else:
            st.error(f"Risque: {risque}% - ÉLEVÉ")
    
    with tab3:
        st.subheader("Optimisation Achats")
        st.info("**Stratégie recommandée:**")
        st.markdown("""
        - 60% Contrats long terme (stabilité)
        - 25% Achats spot (optimisation) 
        - 10% Production réserve (sécurité)
        - 5% Couverture risque
        """)
        st.success("**Économies potentielles: 15-25%**")
    
    with tab4:
        st.subheader("Smart Grid")
        st.markdown("""
        - Compteurs intelligents: 12,500 installés
        - Economies réalisées: 12-25% selon segment
        - Stockage batterie: 250 MWh capacité
        - Réduction pics: 15-25%
        """)

# =============================================================================
# SECTION INTRODUCTION BIG DATA
# =============================================================================

def section_bigdata_intro():
    st.header("📚 Introduction au Big Data")
    
    st.markdown("""
    ## 🌟 Les 5V du Big Data
    
    ### 1. 📦 Volume
    - **Énormes quantités** de données générées
    - **Exemples:** 500M tweets/jour, 4.2B vidéos YouTube/jour
    - **Chiffre clé:** 2.5 trillions d'octets créés chaque jour
    
    ### 2. ⚡ Vélocité  
    - **Vitesse** génération et traitement données
    - **Temps réel** ou quasi réel
    - **Exemple:** Transactions boursières (microsecondes)
    
    ### 3. 🎭 Variété
    - **Divers formats:** Structuré, semi-structuré, non structuré
    - **Exemple:** Textes, images, vidéos, audio, données capteurs
    
    ### 4. ✅ Véracité
    - **Fiabilité et qualité** des données
    - Nettoyage et validation nécessaires
    - **Exemple:** Données erronées, fake news
    
    ### 5. 💰 Valeur
    - **Utilité business** extraite des données  
    - Insights et décisions stratégiques
    - **Objectif:** Transformer données en valeur
    """)
    
    # Technologies Big Data
    with st.expander("🛠️ Technologies du Big Data"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🐘 Écosystème Hadoop")
            st.markdown("""
            - HDFS (Stockage)
            - MapReduce (Traitement)
            - Spark (Processing mémoire)
            - HBase (Base données)
            """)
        
        with col2:
            st.subheader("🗄️ Bases NoSQL")
            st.markdown("""
            - MongoDB (Documents)
            - Cassandra (Colonnes)
            - Neo4j (Graphes)
            - Redis (Clé-valeur)
            """)
        
        with col3:
            st.subheader("☁️ Cloud")
            st.markdown("""
            - AWS (S3, Redshift)
            - Azure (Data Lake)
            - GCP (BigQuery)
            - Databricks
            """)
    
    # Applications par secteur
    with st.expander("🏢 Applications par Secteur"):
        secteurs = {
            "🏥 Santé": "Diagnostic IA, Recherche clinique, Télémédecine",
            "🏦 Finance": "Détection fraude, Scoring crédit, Conformité",
            "🛒 Retail": "Recommandations, Pricing dynamique, Optimisation stocks", 
            "📞 Télécom": "Analyse clients, Détection fraude, Optimisation réseau",
            "🚚 Transport": "Optimisation routes, Gestion flotte, Tracking temps réel",
            "⚡ Énergie": "Maintenance prédictive, Smart grid, Trading énergie"
        }
        
        for secteur, applications in secteurs.items():
            st.markdown(f"**{secteur}**: {applications}")

# =============================================================================
# FONCTION PRINCIPALE
# =============================================================================

if __name__ == "__main__": 
    main()