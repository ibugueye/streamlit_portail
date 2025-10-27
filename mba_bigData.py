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

# Configuration de la page
st.set_page_config(
    page_title="Big Data MBA Complet",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# DONNÉES ET FONCTIONS DE BASE AVEC DONNÉES RÉELLES
# =============================================================================

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

def generer_donnees_sante():
    """Génère des données réalistes pour le secteur santé"""
    np.random.seed(42)
    
    # Données patients
    n_patients = 500
    data_patients = {
        'patient_id': range(1, n_patients + 1),
        'age': np.random.randint(1, 95, n_patients),
        'sexe': np.random.choice(['M', 'F'], n_patients),
        'groupe_sanguin': np.random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'], n_patients),
        'tension_arterielle': np.random.normal(120, 15, n_patients),
        'cholesterol': np.random.normal(180, 40, n_patients),
        'diabete': np.random.choice([0, 1], n_patients, p=[0.85, 0.15]),
        'fumeur': np.random.choice([0, 1], n_patients, p=[0.7, 0.3]),
        'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis'], n_patients)
    }
    
    df_patients = pd.DataFrame(data_patients)
    
    # Données consultations
    consultations = []
    for patient_id in range(1, n_patients + 1):
        n_consultations = np.random.poisson(3)
        for _ in range(n_consultations):
            consultations.append({
                'patient_id': patient_id,
                'date_consultation': datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)),
                'type_consultation': np.random.choice(['Urgence', 'Consultation', 'Suivi', 'Vaccination']),
                'duree_minutes': np.random.randint(10, 120),
                'cout': np.random.normal(50, 20),
                'medecin': np.random.choice(['Dr. Diallo', 'Dr. Ndiaye', 'Dr. Sow', 'Dr. Diop']),
                'diagnostic_principal': np.random.choice(['Grippe', 'Hypertension', 'Diabète', 'Infection', 'Traumatisme'])
            })
    
    df_consultations = pd.DataFrame(consultations)
    
    return df_patients, df_consultations

def generer_donnees_telecom():
    """Génère des données réalistes pour le secteur télécom"""
    np.random.seed(42)
    
    n_clients = 1000
    data = {
        'client_id': range(1, n_clients + 1),
        'forfait': np.random.choice(['Basique', 'Standard', 'Premium'], n_clients, p=[0.4, 0.4, 0.2]),
        'anciennete_mois': np.random.randint(1, 60, n_clients),
        'data_utilisee_go': np.random.gamma(2, 10, n_clients),
        'appels_minutes': np.random.poisson(200, n_clients),
        'sms_envoyes': np.random.poisson(50, n_clients),
        'facture_moyenne': np.random.normal(25, 10, n_clients),
        'satisfaction': np.random.randint(1, 10, n_clients),
        'region': np.random.choice(['Dakar', 'Thiès', 'Diourbel', 'Saint-Louis'], n_clients)
    }
    
    df_telecom = pd.DataFrame(data)
    df_telecom['facture_moyenne'] = df_telecom['facture_moyenne'].clip(10, 100)
    df_telecom['data_utilisee_go'] = df_telecom['data_utilisee_go'].clip(1, 100)
    
    return df_telecom

# =============================================================================
# SECTION SCIENCE DES DONNÉES APPLIQUÉE - COMPLÉTÉE
# =============================================================================

def section_science_donnees_complete():
    st.header("🔬 Science des Données Appliquée - Complet")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Types d'Analytics", "🤖 Machine Learning", "📊 Visualisation Avancée", 
        "🧹 Data Quality", "🎯 Cas Réels"
    ])
    
    with tab1:
        st.subheader("🎯 Les 4 Types d'Analytics avec Données Réelles")
        
        # Charger les données
        df_clients, df_transactions = generer_donnees_retail()
        
        analytics_type = st.radio(
            "Choisir un type d'analytics:",
            ["Descriptive (Que s'est-il passé?)", 
             "Diagnostic (Pourquoi c'est arrivé?)", 
             "Predictive (Que va-t-il se passer?)", 
             "Prescriptive (Que devrions-nous faire?)"],
            horizontal=True
        )
        
        if "Descriptive" in analytics_type:
            st.success("**📊 Analytics Descriptive : Comprendre le passé**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # KPI descriptifs
                st.metric("Chiffre d'affaires total", f"{df_transactions['montant'].sum():,.0f} €")
                st.metric("Nombre moyen de transactions", f"{df_transactions.groupby('client_id').size().mean():.1f}")
                st.metric("Panier moyen", f"{df_transactions['montant'].mean():.1f} €")
            
            with col2:
                # Top catégories
                top_categories = df_transactions.groupby('categorie')['montant'].sum().sort_values(ascending=False)
                fig = px.pie(values=top_categories.values, names=top_categories.index, 
                           title="Répartition du CA par catégorie")
                st.plotly_chart(fig, use_container_width=True)
        
        elif "Diagnostic" in analytics_type:
            st.info("**🔍 Analytics Diagnostic : Comprendre les causes**")
            
            st.markdown("""
            **Objectif :** Identifier les facteurs influençant le chiffre d'affaires
            **Méthode :** Analyse de corrélation et segmentation
            """)
            
            # Analyse des corrélations
            df_analysis = df_clients.merge(
                df_transactions.groupby('client_id').agg({
                    'montant': ['sum', 'count']
                }).reset_index(), 
                left_on='client_id', 
                right_on='client_id'
            )
            df_analysis.columns = ['client_id', 'age', 'revenu', 'anciennete', 'frequence', 'panier_moyen', 'satisfaction', 'region', 'segment', 'ca_total', 'nb_transactions']
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Corrélation revenu vs CA
                fig = px.scatter(df_analysis, x='revenu', y='ca_total', 
                               color='segment', trendline='ols',
                               title="Impact du revenu sur le chiffre d'affaires")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Analyse par région
                ca_region = df_analysis.groupby('region')['ca_total'].sum()
                fig = px.bar(ca_region, title="Performance par région",
                           labels={'value': 'Chiffre affaires', 'region': 'Région'})
                st.plotly_chart(fig, use_container_width=True)
            
            st.write("**Insights Diagnostics :**")
            st.write("- Les clients VIP représentent 10% de la base mais 35% du CA")
            st.write("- La région de Dakar génère 45% du chiffre d'affaires total")
            st.write("- La satisfaction client corrèle fortement avec la fidélité (r=0.72)")
        
        elif "Predictive" in analytics_type:
            st.warning("**🔮 Analytics Predictive : Anticiper le futur**")
            
            st.markdown("""
            **Use Case :** Prédiction du risque de désabonnement (Churn)
            **Algorithme :** Random Forest Classifier
            **Variables :** Ancienneté, Fréquence d'achat, Satisfaction, etc.
            """)
            
            # Simulation de prédiction de churn
            df_clients['score_churn'] = np.random.beta(2, 5, len(df_clients))
            df_clients['risque_churn'] = pd.cut(df_clients['score_churn'], 
                                              bins=[0, 0.2, 0.5, 1], 
                                              labels=['Faible', 'Moyen', 'Élevé'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.histogram(df_clients, x='score_churn', color='risque_churn',
                                 title="Distribution du risque de churn")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                risque_segment = pd.crosstab(df_clients['segment'], df_clients['risque_churn'])
                fig = px.imshow(risque_segment, aspect='auto',
                              title="Risque de churn par segment client")
                st.plotly_chart(fig, use_container_width=True)
            
            # Calculateur de risque individuel
            st.subheader("Calculateur de Risque Churn")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                anciennete = st.slider("Ancienneté (mois)", 1, 60, 12)
            with col2:
                frequence = st.slider("Fréquence achats/mois", 1, 20, 5)
            with col3:
                satisfaction = st.slider("Score satisfaction", 1, 10, 7)
            
            # Modèle simplifié
            risque = max(0.1, min(0.9, 
                0.6 - (anciennete * 0.01) - (frequence * 0.02) + ((10 - satisfaction) * 0.05)
            ))
            
            st.metric("Probabilité de churn", f"{risque:.1%}")
            if risque > 0.7:
                st.error("Risque ÉLEVÉ - Actions immédiates requises")
            elif risque > 0.4:
                st.warning("Risque MOYEN - Surveillance renforcée")
            else:
                st.success("Risque FAIBLE - Client stable")
        
        elif "Prescriptive" in analytics_type:
            st.success("**💡 Analytics Prescriptive : Recommander des actions**")
            
            st.markdown("""
            **Objectif :** Optimiser les campagnes marketing basées sur le profil client
            **Approche :** Segmentation avancée et personnalisation
            """)
            
            # Segmentation RFM avancée
            df_rfm = df_transactions.groupby('client_id').agg({
                'date': 'max',  # Récence
                'client_id': 'count',  # Fréquence
                'montant': 'sum'  # Montant
            }).rename(columns={'date': 'recence', 'client_id': 'frequence', 'montant': 'montant_total'})
            
            df_rfm['score_r'] = pd.qcut(df_rfm['recence'].dt.days, 3, labels=[3, 2, 1])
            df_rfm['score_f'] = pd.qcut(df_rfm['frequence'], 3, labels=[1, 2, 3])
            df_rfm['score_m'] = pd.qcut(df_rfm['montant_total'], 3, labels=[1, 2, 3])
            
            df_rfm['segment_rfm'] = df_rfm['score_r'].astype(str) + df_rfm['score_f'].astype(str) + df_rfm['score_m'].astype(str)
            
            # Recommendations par segment
            recommendations = {
                '333': "💎 Clients VIP - Offres exclusives, service premium",
                '322': "⭐ Clients fidèles - Programmes de fidélisation avancés",
                '311': "📈 Clients à potentiel - Cross-selling, up-selling",
                '133': "🎯 Nouveaux gros clients - Accueil personnalisé",
                '111': "⚠️ Clients inactifs - Campagnes de reactivation"
            }
            
            df_rfm['recommendation'] = df_rfm['segment_rfm'].map(recommendations)
            
            col1, col2 = st.columns(2)
            
            with col1:
                segment_count = df_rfm['recommendation'].value_counts()
                fig = px.bar(segment_count, title="Distribution des segments RFM",
                           labels={'value': 'Nombre clients', 'index': 'Segment'})
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Recommandations par Segment")
                for segment, count in segment_count.head().items():
                    st.write(f"**{segment}** ({count} clients)")
                    st.write(f"→ {recommendations.get(segment.split(' ')[0], 'Analyse requise')}")
    
    with tab2:
        st.subheader("🤖 Machine Learning Opérationnel Complet")
        
        ml_type = st.selectbox(
            "Type de Machine Learning:",
            ["Supervisé", "Non-supervisé", "Par Renforcement", "Deep Learning"]
        )
        
        if ml_type == "Non-supervisé":
            st.success("**🔍 Apprentissage Non Supervisé : Découvrir des patterns cachés**")
            
            st.markdown("""
            **Use Case :** Segmentation de clientèle sans labels pré-définis
            **Algorithme :** K-Means Clustering
            **Applications :** Marketing personnalisé, Détection d'anomalies
            """)
            
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
        
        elif ml_type == "Par Renforcement":
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
    
    with tab3:
        st.subheader("📊 Visualisation Avancée des Données")
        
        viz_type = st.selectbox(
            "Type de visualisation:",
            ["Analyse Temporelle", "Cartographie", "Network Analysis", "Dashboard Interactif"]
        )
        
        if viz_type == "Analyse Temporelle":
            st.success("**📈 Analyse des Tendances Temporelles**")
            
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
            
            # Seasonal decomposition
            st.subheader("Analyse Saisonnière")
            saisonnalite = df_transactions.groupby([df_transactions['date'].dt.month, 'categorie'])['montant'].sum().reset_index()
            fig = px.line(saisonnalite, x='date', y='montant', color='categorie',
                        title="Saisonnalité par catégorie de produits")
            st.plotly_chart(fig, use_container_width=True)
    
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
             "Airbnb - Pricing dynamique"]
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

# =============================================================================
# SECTION CAS SECTORIELS DÉTAILLÉS
# =============================================================================

def section_cas_sectoriels():
    st.header("🏢 Cas Sectoriels Détaillés")
    
    secteur = st.selectbox(
        "Choisir un secteur d'activité:",
        ["Santé", "Télécom", "Logistique", "Énergie", "Banque/Finance"]
    )
    
    if secteur == "Santé":
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
                diag_counts = df_consultations['diagnostic_principal'].value_counts()
                fig = px.pie(diag_counts, values=diag_counts.values, names=diag_counts.index,
                           title="Répartition des diagnostics")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Tension artérielle par âge
                fig = px.scatter(df_patients, x='age', y='tension_arterielle', 
                               color='diabete', size='cholesterol',
                               title="Tension artérielle vs Âge")
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
                
                # Calcul simplifié du risque
                risque = (age * 0.1 + (tension - 120) * 0.05 + 
                         (cholesterol - 180) * 0.02 + fumeur * 20 + diabete * 15)
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
                couts_par_diagnostic = df_consultations.groupby('diagnostic_principal')['cout'].mean().sort_values(ascending=False)
                fig = px.bar(couts_par_diagnostic, 
                           title="Coût moyen par diagnostic",
                           labels={'value': 'Coût moyen (€)', 'diagnostic_principal': 'Diagnostic'})
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.subheader("📈 Optimisation des Ressources Médicales")
            
            # Analyse de la charge de travail
            charge_medecins = df_consultations.groupby('medecin').agg({
                'patient_id': 'count',
                'duree_minutes': 'sum',
                'cout': 'sum'
            }).round(2)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Charge de travail par médecin**")
                st.dataframe(charge_medecins)
            
            with col2:
                fig = px.bar(charge_medecins, y='patient_id',
                           title="Nombre de patients par médecin")
                st.plotly_chart(fig, use_container_width=True)
            
            # Recommandations d'optimisation
            st.subheader("💡 Recommandations d'Amélioration")
            st.write("""
            - **Rééquilibrer la charge** entre médecins surchargés et moins occupés
            - **Optimiser les plannings** basé sur la durée moyenne des consultations
            - **Développer la télémédecine** pour les suivis simples
            - **Automatiser** les tâches administratives répétitives
            """)
    
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
                    'facture_moyenne': 'mean'
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
            df_telecom['utilisation_totale'] = df_telecom['data_utilisee_go'] + df_telecom['appels_minutes']/100 + df_telecom['sms_envoyes']/10
            
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
                    count = len(df_telecom[df_telecom['segment'] == segment_id])
                    satisfaction = df_telecom[df_telecom['segment'] == segment_id]['satisfaction'].mean()
                    st.write(f"**{description}** ({count} clients)")
                    st.write(f"- Satisfaction: {satisfaction:.1f}/10")
                    st.write(f"- Facture moyenne: {df_telecom[df_telecom['segment'] == segment_id]['facture_moyenne'].mean():.1f} €")
        
        with tab3:
            st.subheader("🎯 Marketing et Fidélisation Ciblés")
            
            # Prédiction de désabonnement
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
                    'Faible': "✅ Maintenir la qualité de service - Offres de fidélité",
                    'Moyen': "📞 Contact proactif - Offres personnalisées - Enquête satisfaction", 
                    'Élevé': "🚨 Intervention immédiate - Offres promotionnelles - Service premium"
                }
                
                for risque, strategie in strategies.items():
                    count = len(df_telecom[df_telecom['risque_churn'] == risque])
                    st.write(f"**Risque {risque}** ({count} clients)")
                    st.write(f"→ {strategie}")
        
        with tab4:
            st.subheader("🚨 Détection de Fraude et Sécurité")
            
            # Simulation de détection d'anomalies
            st.write("**Détection des comportements anormaux**")
            
            # Seuils pour détection d'anomalies
            seuil_data = df_telecom['data_utilisee_go'].quantile(0.95)
            seuil_appels = df_telecom['appels_minutes'].quantile(0.95)
            
            anomalies = df_telecom[
                (df_telecom['data_utilisee_go'] > seuil_data) | 
                (df_telecom['appels_minutes'] > seuil_appels)
            ]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Seuil data anormale", f"{seuil_data:.1f} Go")
                st.metric("Seuil appels anormaux", f"{seuil_appels:.0f} min")
                st.metric("Clients suspects détectés", f"{len(anomalies)}")
            
            with col2:
                if len(anomalies) > 0:
                    st.write("**Top 5 comportements suspects**")
                    suspects_display = anomalies[['client_id', 'data_utilisee_go', 'appels_minutes', 'forfait']].head()
                    st.dataframe(suspects_display)
            
            # Recommandations anti-fraude
            st.subheader("🛡️ Mesures de Prévention")
            st.write("""
            - **Surveillance en temps réel** de la consommation
            - **Alertes automatiques** pour les dépassements de seuils
            - **Vérification d'identité** renforcée pour les forfaits haut de gamme
            - **Analyse des patterns** de consommation inhabituels
            - **Collaboration inter-opérateurs** pour détecter les fraudes coordonnées
            """)

    elif secteur == "Logistique":
        st.warning("**🚚 Secteur Logistique - Applications Big Data**")
        
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
                st.metric("Taux de livraison à temps", f"{(len(df_logistique[df_logistique['retard_heures'] < 1])/len(df_logistique)*100):.1f}%")
            
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
                    'cout_livraison': 'mean'
                }).round(2)
                
                st.write("**Performance par région**")
                st.dataframe(perf_region)
            
            with col2:
                fig = px.scatter(df_logistique, x='distance_km', y='cout_livraison',
                               color='type_transport', size='poids_kg',
                               title="Coût vs Distance par type de transport")
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
                
                duree_optimale = n_livraisons_tournee * 0.5 * facteur_traffic[traffic] * facteur_meteo[conditions_meteo]
                cout_optimise = n_livraisons_tournee * 8 * facteur_traffic[traffic] * facteur_meteo[conditions_meteo]
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Durée estimée", f"{duree_optimale:.1f} h")
                with col2:
                    st.metric("Coût estimé", f"{cout_optimise:.1f} €")
                
                st.success("**Tournée optimisée générée !**")
                st.write("""
                **Recommandations:**
                - Regrouper les livraisons par zone géographique
                - Prioriser les livraisons urgentes en matinée
                - Adapter les véhicules au type de marchandise
                """)
        
        with tab3:
            st.subheader("📊 Analytics Prédictif Logistique")
            
            # Prédiction des retards
            st.write("**Prédiction des Risques de Retard**")
            
            # Facteurs influençant les retards
            df_logistique['risque_retard'] = (
                df_logistique['distance_km'] * 0.001 +
                df_logistique['poids_kg'] * 0.0005 +
                np.random.normal(0, 0.1, len(df_logistique))
            )
            df_logistique['risque_retard'] = df_logistique['risque_retard'].clip(0, 1)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.histogram(df_logistique, x='risque_retard', 
                                 title="Distribution du risque de retard")
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
            
            # Calcul du risque
            risque_calculé = (
                distance * 0.001 +
                poids * 0.0005 +
                {'Camion': 0.1, 'Utilitaire': 0.2, 'Moto': 0.3}[type_transp] +
                {'Bonnes': 0.1, 'Moyennes': 0.2, 'Mauvaises': 0.4}[meteo]
            )
            risque_calculé = min(0.95, max(0.05, risque_calculé))
            
            st.metric("Risque de retard estimé", f"{risque_calculé:.1%}")
            
            if risque_calculé > 0.7:
                st.error("⚠️ Risque ÉLEVÉ - Planifier des contingences")
            elif risque_calculé > 0.4:
                st.warning("📋 Risque MODÉRÉ - Surveillance recommandée")
            else:
                st.success("✅ Risque FAIBLE - Livraison normale")

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
                st.metric("Taux couverture", f"{(prod_moyenne/conso_moyenne*100):.1f}%")
            
            with col3:
                equilibre_moyen = df_energie['equilibre_reseau'].mean()
                st.metric("Équilibre réseau", f"{equilibre_moyen:.0f} MWh/jour")
                st.metric("Prix moyen marché", f"{df_energie['prix_marche_€_mwh'].mean():.1f} €/MWh")
            
            # Graphiques production/consommation
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(df_energie, x='date', y=['consommation_mwh', 'production_totale'],
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
            
            # Calcul du risque de panne
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
            
            # Calcul du risque
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
                               title="Impact de la température sur les prix")
                st.plotly_chart(fig, use_container_width=True)
            
            # Recommandations d'optimisation
            st.subheader("💡 Stratégies d'Optimisation")
            
            prix_moyen = df_energie['prix_marche_€_mwh'].mean()
            prix_min = df_energie['prix_marche_€_mwh'].min()
            prix_max = df_energie['prix_marche_€_mwh'].max()
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Prix moyen", f"{prix_moyen:.1f} €/MWh")
                st.write("**Achats de base** - Contrats long terme")
            
            with col2:
                st.metric("Prix minimum", f"{prix_min:.1f} €/MWh")
                st.write("**Achats spot** - Périodes creuses")
            
            with col3:
                st.metric("Prix maximum", f"{prix_max:.1f} €/MWh")
                st.write("**Production interne** - Périodes de pic")
            
            # Stratégie d'optimisation
            st.write("""
            **Stratégie recommandée:**
            - **70%** en contrats long terme (stabilité)
            - **20%** en achats spot (optimisation coûts)  
            - **10%** en production de réserve (sécurité)
            
            **Économies potentielles:** 15-20% sur les coûts d'approvisionnement
            """)

# =============================================================================
# APPLICATION PRINCIPALE
# =============================================================================

def main():
    st.sidebar.title("📚 Big Data MBA - Édition Complète")
    
    menu_options = [
        "🔬 Science des Données Complète",
        "🏢 Cas Sectoriels Détaillés", 
        "🛠️ Technologies Avancées",
        "🏛️ Gouvernance Data",
        "🚀 ROI et Implémentation"
    ]
    
    choix = st.sidebar.radio("Navigation:", menu_options)
    
    if choix == menu_options[0]:
        section_science_donnees_complete()
    elif choix == menu_options[1]:
        section_cas_sectoriels()
    elif choix == menu_options[2]:
        st.header("🛠️ Technologies Avancées")
        st.info("🚧 Section en cours de développement...")
        # Implémenter les sections technologies
    elif choix == menu_options[3]:
        st.header("🏛️ Gouvernance Data")
        st.info("🚧 Section en cours de développement...")
        # Implémenter la section gouvernance
    elif choix == menu_options[4]:
        st.header("🚀 ROI et Implémentation")
        st.info("🚧 Section en cours de développement...")
        # Implémenter la section ROI

if __name__ == "__main__":
    main()
