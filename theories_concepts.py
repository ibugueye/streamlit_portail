import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="📚 Documentation Complète - Théories Big Data par Secteur",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour la documentation
st.markdown("""
<style>
    .doc-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
    }
    .theory-section {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 15px 0;
    }
    .sector-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
        border: 1px solid #e9ecef;
    }
    .algorithm-card {
        background: #e3f2fd;
        border: 1px solid #2196f3;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .tech-stack {
        background: #fff3cd;
        border: 1px solid #ffc107;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .case-study {
        background: #d1ecf1;
        border: 1px solid #17a2b8;
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<div class="doc-header"><h1>📚 Documentation Complète - Théories Big Data par Secteur</h1></div>', unsafe_allow_html=True)
    
    # Navigation principale
    section = st.sidebar.selectbox(
        "**📖 Sections de Documentation**",
        [
            "🏠 Introduction Générale",
            "🎯 Méthodologie Big Data",
            "🏥 Théories Santé & Médical", 
            "🏦 Théories Finance & Banque",
            "🛒 Théories Retail & Commerce",
            "📞 Théories Télécommunications",
            "🚚 Théories Transport & Logistique",
            "⚡ Théories Énergie & Utilities",
            "🤖 Algorithmes & ML Avancés",
            "🛠️ Stack Technologique",
            "📈 Métriques & ROI"
        ]
    )
    
    if section == "🏠 Introduction Générale":
        documentation_introduction()
    elif section == "🎯 Méthodologie Big Data":
        documentation_methodologie()
    elif section == "🏥 Théories Santé & Médical":
        documentation_sante()
    elif section == "🏦 Théories Finance & Banque":
        documentation_finance()
    elif section == "🛒 Théories Retail & Commerce":
        documentation_retail()
    elif section == "📞 Théories Télécommunications":
        documentation_telecom()
    elif section == "🚚 Théories Transport & Logistique":
        documentation_transport()
    elif section == "⚡ Théories Énergie & Utilities":
        documentation_energie()
    elif section == "🤖 Algorithmes & ML Avancés":
        documentation_algorithmes()
    elif section == "🛠️ Stack Technologique":
        documentation_technologie()
    elif section == "📈 Métriques & ROI":
        documentation_metriques()

# =============================================================================
# INTRODUCTION GÉNÉRALE
# =============================================================================

def documentation_introduction():
    st.header("🏠 Introduction Générale aux Systèmes Big Data")
    
    st.markdown("""
    ## 🌟 Fondements du Big Data
    
    ### Définition et Évolution
    
    Le **Big Data** représente l'ensemble des technologies et méthodologies permettant de traiter des volumes massifs de données 
    dont les caractéristiques dépassent les capacités des systèmes traditionnels. Son émergence s'inscrit dans la continuité 
    de plusieurs révolutions technologiques.
    
    #### Évolution Historique:
    """)
    
    # Timeline de l'évolution Big Data
    evolution_data = {
        'Période': ['Années 1960-1980', 'Années 1990-2000', 'Années 2000-2010', '2010-2020', '2020+'],
        'Événement': ['Bases de données relationnelles', 'Data Warehousing', 'Web 2.0 et données non-structurées', 
                     'Hadoop et écosystème Big Data', 'IA et Cloud Computing'],
        'Volume Données': ['Go', 'To', 'Po', 'Eo', 'Zo'],
        'Technologies': ['SQL, Oracle', 'ETL, OLAP', 'XML, Web Services', 'Hadoop, Spark', 'TensorFlow, Kubernetes']
    }
    
    df_evolution = pd.DataFrame(evolution_data)
    st.dataframe(df_evolution, use_container_width=True)
    
    st.markdown("""
    ### 📊 Les 5V du Big Data - Cadre Théorique Fondamental
    
    Le modèle des **5V** constitue le cadre conceptuel de référence pour caractériser les systèmes Big Data:
    """)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        #### 📦 Volume
        **Théorie:** Loi de Moore appliquée aux données
        - Croissance exponentielle des données (double tous les 2 ans)
        - Coût stockage divisé par 2 tous les 18 mois
        - Passage du To au Eo puis Zo
        """)
    
    with col2:
        st.markdown("""
        #### ⚡ Vélocité  
        **Théorie:** Loi de Metcalfe sur la valeur réseau
        - Vitesse génération données > capacité traitement
        - Streaming vs Batch processing
        - Latence critique pour décisions temps réel
        """)
    
    with col3:
        st.markdown("""
        #### 🎭 Variété
        **Théorie:** Théorie de l'information de Shannon
        - Données structurées vs non-structurées
        - Multi-modalité (texte, image, vidéo, capteurs)
        - Schémas flexibles et dynamiques
        """)
    
    with col4:
        st.markdown("""
        #### ✅ Véracité
        **Théorie:** Théorie de la décision bayésienne
        - Qualité, fiabilité, confiance données
        - Gestion incertitude et bruits
        - Data governance et lineage
        """)
    
    with col5:
        st.markdown("""
        #### 💰 Valeur
        **Théorie:** Économie de l'information
        - ROI des initiatives data
        - Transformation données → insights → valeur
        - Métriques impact business
        """)
    
    st.markdown("""
    ### 🏢 Impact Sectoriel du Big Data
    
    L'adoption du Big Data transforme fondamentalement tous les secteurs économiques selon des patterns spécifiques:
    """)
    
    # Impact par secteur
    impact_data = {
        'Secteur': ['Santé', 'Finance', 'Retail', 'Télécom', 'Transport', 'Énergie'],
        'Transformation': ['Médecine 4.0', 'Finance digitale', 'Commerce omnicanal', 'Réseaux intelligents', 'Logistique prédictive', 'Smart grids'],
        'Données Clés': ['Dossiers patients, génomique', 'Transactions, comportements', 'Interactions clients, ventes', 'Usage réseau, géolocalisation', 'GPS, capteurs, trafic', 'Capteurs IoT, consommation'],
        'Valeur Business': ['+30% efficacité soins', '+25% détection fraude', '+35% conversion', '+40% rétention clients', '+20% optimisation flotte', '+15% efficacité énergétique']
    }
    
    st.dataframe(pd.DataFrame(impact_data), use_container_width=True)

# =============================================================================
# MÉTHODOLOGIE BIG DATA
# =============================================================================

def documentation_methodologie():
    st.header("🎯 Méthodologie Complète des Projets Big Data")
    
    st.markdown("""
    ## 🏗️ Cadre Méthodologique CRISP-DM Étendu
    
    La méthodologie **CRISP-DM** (Cross Industry Standard Process for Data Mining) constitue le standard industriel, 
    étendu pour les spécificités Big Data:
    """)
    
    # Diagramme méthodologique
    phases = [
        {"Phase": "1. Compréhension Business", "Activités": ["Définition objectifs", "Analyse contraintes", "Évaluation faisabilité"]},
        {"Phase": "2. Compréhension Données", "Activités": ["Collection données", "Qualité données", "Exploration données"]},
        {"Phase": "3. Préparation Données", "Activités": ["Nettoyage", "Transformation", "Feature engineering"]},
        {"Phase": "4. Modélisation", "Activités": ["Sélection algorithmes", "Entraînement modèles", "Validation"]},
        {"Phase": "5. Évaluation", "Activités": ["Validation business", "Analyse ROI", "Décision déploiement"]},
        {"Phase": "6. Déploiement", "Activités": ["Intégration systèmes", "Monitoring", "Maintenance"]}
    ]
    
    for phase in phases:
        with st.expander(f"**{phase['Phase']}**", expanded=True):
            for activite in phase['Activités']:
                st.markdown(f"- {activite}")
    
    st.markdown("""
    ### 📊 Méthodes d'Évaluation et Validation
    
    #### Validation Technique
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Métriques de Performance:**
        - **Accuracy:** (TP + TN) / Total
        - **Precision:** TP / (TP + FP)
        - **Recall:** TP / (TP + FN) 
        - **F1-Score:** 2 * (Precision * Recall) / (Precision + Recall)
        - **AUC-ROC:** Area Under Curve
        """)
        
        st.latex(r"F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}")
    
    with col2:
        st.markdown("""
        **📈 Techniques de Validation:**
        - **Train-Test Split:** 70-30% ou 80-20%
        - **Cross-Validation:** k-fold (k=5 ou 10)
        - **Stratified Sampling:** Préservation distribution
        - **Time Series Split:** Données temporelles
        - **Bootstrapping:** Échantillonnage avec remise
        """)
    
    st.markdown("""
    ### 🎯 Gestion de Projet Agile Data
    
    Adaptation des méthodologies agiles aux spécificités data:
    """)
    
    agile_data = {
        'Cérémonie': ['Sprint Planning', 'Daily Standup', 'Sprint Review', 'Sprint Retrospective'],
        'Objectif Data': ['Définition objectifs métier et métriques', 'Suivi qualité données et modèles', 'Validation résultats avec stakeholders', 'Amélioration processus data'],
        'Artéfacts': ['Product Backlog Data', 'Burndown Chart qualité', 'Dashboard métriques', 'Plan amélioration continue']
    }
    
    st.dataframe(pd.DataFrame(agile_data), use_container_width=True)

# =============================================================================
# THÉORIES SANTÉ & MÉDICAL
# =============================================================================

def documentation_sante():
    st.header("🏥 Théories et Cadres Conceptuels - Secteur Santé")
    
    st.markdown("""
    ## 🎯 Fondements de la Santé Digitale
    
    ### Théorie de la Médecine 4.0 (P4 Medicine)
    
    Conceptualisée par **Leroy Hood** (2012), la médecine P4 représente une transformation fondamentale:
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        #### 🔮 Prédictive
        **Théorie:** Modèles prédictifs basés données longitudinales
        - Analyse risque individuel
        - Détection pré-symptomatique
        - Médecine anticipative
        """)
    
    with col2:
        st.markdown("""
        #### 🛡️ Préventive  
        **Théorie:** Intervention précoce basée risque prédit
        - Personnalisation prévention
        - Réduction incidence maladies
        - Optimisation ressources
        """)
    
    with col3:
        st.markdown("""
        #### 🎯 Personnalisée
        **Théorie:** Traitements sur-mesure basés profil
        - Pharmacogénomique
        - Adaptation posologie
        - Minimisation effets secondaires
        """)
    
    with col4:
        st.markdown("""
        #### 🤝 Participative
        **Théorie:** Engagement patient actif
        - Données patient-generated
        - Co-décision thérapeutique
        - Autogestion santé
        """)
    
    st.markdown("""
    ### 📊 Économie de la Santé Digitale
    
    #### Théorie des Coûts de Transaction (Williamson, 1985)
    
    Application au secteur santé:
    """)
    
    st.markdown("""
    **Réduction des coûts de transaction via la digitalisation:**
    - **Coûts de recherche:** Accès instantané informations médicales
    - **Coûts de coordination:** Optimisation rendez-vous et ressources
    - **Coûts de surveillance:** Monitoring continu patients
    - **Coûts d'opportunité:** Détection précoce économisant traitements coûteux
    """)
    
    st.markdown("""
    #### Modèle ROI Santé Digitale
    
    Équation fondamentale du retour sur investissement:
    """)
    
    st.latex(r"""
    ROI_{santé} = \frac{\sum (Économies_{prévention} + Gains_{efficacité} + Réduction_{erreurs}) - Coûts_{technologie}}{Coûts_{technologie}}
    """)
    
    st.markdown("""
    Où:
    - **Économies prévention:** Coûts évités via détection précoce
    - **Gains efficacité:** Productivité améliorée personnel soignant  
    - **Réduction erreurs:** Coûts litiges et ré-interventions évités
    - **Coûts technologie:** Infrastructure, développement, maintenance
    """)
    
    st.markdown("""
    ### 🧬 Sciences des Données Médicales
    
    #### Intégration Multi-Omique
    
    Fusion de différentes couches de données biologiques:
    """)
    
    omics_data = {
        'Couche': ['Génomique', 'Transcriptomique', 'Protéomique', 'Métabolomique', 'Microbiomique'],
        'Données': ['Séquences ADN', 'Expression gènes', 'Protéines', 'Métabolites', 'Micro-organismes'],
        'Technologies': ['NGS, WGS', 'RNA-Seq', 'Mass spectrometry', 'NMR, LC-MS', '16S rRNA sequencing'],
        'Applications': ['Risque maladies', 'Réponse traitement', 'Biomarqueurs', 'État physiologique', 'Santé digestive']
    }
    
    st.dataframe(pd.DataFrame(omics_data), use_container_width=True)
    
    st.markdown("""
    #### Théorie des Réseaux Biologiques (Barabási, 2004)
    
    Application des réseaux complexes à la biologie:
    """)
    
    st.latex(r"""
    P(k) \sim k^{-\gamma}
    """)
    
    st.markdown("""
    Où:
    - **P(k):** Probabilité qu'un nœud ait k connexions
    - **γ:** Exposant caractéristique (~2-3 réseaux biologiques)
    - **Applications:** Identification cibles thérapeutiques, compréhension maladies complexes
    """)

# =============================================================================
# THÉORIES FINANCE & BANQUE
# =============================================================================

def documentation_finance():
    st.header("🏦 Théories Économiques et Financières")
    
    st.markdown("""
    ## 📈 Fondements de la Finance Digitale
    
    ### Théorie de l'Asymétrie d'Information (Akerlof, 1970)
    
    Application aux systèmes de scoring crédit:
    """)
    
    st.markdown("""
    **Problème des "lemons" (voitures d'occasion) appliqué au crédit:**
    - **Asymétrie pré-contractuelle:** Emprunteurs connaissent mieux leur risque que prêteurs
    - **Sélection adverse:** Seuls les emprunteurs risqués demandent du crédit
    - **Solution Big Data:** Réduction asymétrie via données alternatives
    """)
    
    st.latex(r"""
    E[R] = \sum_{i=1}^{n} p_i \times r_i
    """)
    
    st.markdown("""
    Où:
    - **E[R]:** Espérance de rendement
    - **p_i:** Probabilité défaut catégorie i
    - **r_i:** Rendement catégorie i
    """)
    
    st.markdown("""
    ### Théorie du Signal (Spence, 1973)
    
    Application au scoring comportemental:
    """)
    
    st.markdown("""
    **Les données alternatives comme signaux de qualité:**
    - **Signaux forts:** Historique paiements, stabilité résidentielle
    - **Signaux faibles:** Activité réseaux sociaux, patterns dépenses
    - **Équilibre séparateur:** Différenciation emprunteurs par signaux
    """)
    
    st.markdown("""
    ### 📊 Théorie du Portefeuille (Markowitz, 1952) - Extension Big Data
    
    Modernisation avec données alternatives et ML:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Optimisation Portefeuille Traditionnelle:**
        """)
        st.latex(r"""
        \min_w \left( w^T \Sigma w \right)
        """)
        st.latex(r"""
        \text{s.t. } w^T \mu = \mu_p, \quad \sum w_i = 1
        """)
    
    with col2:
        st.markdown("""
        **Extension Big Data:**
        """)
        st.latex(r"""
        \min_w \left( w^T \hat{\Sigma} w + \lambda \|w\|_1 \right)
        """)
        st.latex(r"""
        \hat{\Sigma} = f(\text{sentiment}, \text{news}, \text{réseaux sociaux})
        """)
    
    st.markdown("""
    ### 🚨 Théorie de la Détection de Fraude
    
    #### Cadre Neyman-Pearson (1933)
    
    Optimisation compromis faux positifs/faux négatifs:
    """)
    
    st.latex(r"""
    \min_{\delta} P(\text{FA}) \quad \text{s.t.} \quad P(\text{D}) \geq 1-\beta
    """)
    
    st.markdown("""
    Où:
    - **P(FA):** Probabilité fausse alerte
    - **P(D):** Probabilité détection
    - **β:** Niveau risque accepté
    """)
    
    st.markdown("""
    #### Application Réseaux de Fraude
    
    Théorie des graphes appliquée aux fraudes organisées:
    """)
    
    st.latex(r"""
    \text{Fraud Score} = \alpha \cdot \text{Node Features} + \beta \cdot \text{Graph Features}
    """)
    
    st.markdown("""
    **Features de graphe:**
    - **Centralité:** Importance nœud dans réseau
    - **Clustering coefficient:** Densité connexions locales
    - **PageRank:** Influence dans réseau
    - **Community detection:** Groupes suspects
    """)

# =============================================================================
# THÉORIES RETAIL & COMMERCE
# =============================================================================

def documentation_retail():
    st.header("🛒 Théories Économiques du Commerce Digital")
    
    st.markdown("""
    ## 🎯 Économie du Commerce Digital
    
    ### Théorie de la Long Tail (Anderson, 2004)
    
    Transformation fondamentalement par le Big Data:
    """)
    
    st.markdown("""
    **Équation de la Long Tail:**
    """)
    
    st.latex(r"""
    R = \int_{0}^{h} r(h) \, dh + \int_{h}^{\infty} r(h) \, dh
    """)
    
    st.markdown("""
    Où:
    - **R:** Revenu total
    - **r(h):** Fonction revenu par produit
    - **h:** Seuil entre hits et niche
    """)
    
    st.markdown("""
    **Impact Big Data:**
    - **Découverte niches:** Algorithmes recommandation
    - **Personnalisation:** Adaptation offre individuelle
    - **Optimisation inventaire:** Stocks dynamiques
    """)
    
    st.markdown("""
    ### Théorie du Consumer Surplus (Marshall, 1890) - Extension Digitale
    
    Mesure valeur créée pour consommateurs:
    """)
    
    st.latex(r"""
    CS = \int_{p}^{\infty} D(p) \, dp
    """)
    
    st.markdown("""
    **Amélioration via personnalisation:**
    """)
    
    st.latex(r"""
    CS_{personalized} = \sum_{i=1}^{n} \int_{p_i}^{\infty} D_i(p) \, dp
    """)
    
    st.markdown("""
    Où **D_i(p)** représente la demande individualisée du consommateur i.
    """)
    
    st.markdown("""
    ### 📊 Théorie des Systèmes de Recommandation
    
    #### Filtrage Collaboratif - Fondements Mathématiques
    
    **Décomposition Matricielle:**
    """)
    
    st.latex(r"""
    \min_{P,Q} \sum_{(i,j) \in \Omega} (r_{ij} - p_i^T q_j)^2 + \lambda(\|P\|_F^2 + \|Q\|_F^2)
    """)
    
    st.markdown("""
    Où:
    - **r_ij:** Rating utilisateur i sur item j
    - **p_i:** Vecteur latent utilisateur i
    - **q_j:** Vecteur latent item j
    - **Ω:** Ensemble observations disponibles
    """)
    
    st.markdown("""
    #### Deep Learning pour Recommandation
    
    **Architecture NeuCF (Neural Collaborative Filtering):**
    """)
    
    st.latex(r"""
    \hat{r}_{ij} = f(p_i, q_j | \Theta)
    """)
    
    st.markdown("""
    Où **f** est une fonction non-linéaire apprise par réseau neuronal.
    """)
    
    st.markdown("""
    ### 💰 Théorie du Pricing Dynamique
    
    #### Revenue Management (Talluri & van Ryzin, 2004)
    
    Optimisation revenus avec contraintes capacité:
    """)
    
    st.latex(r"""
    \max \sum_{t=1}^{T} \sum_{k=1}^{K} p_{kt} \cdot x_{kt}
    """)
    
    st.latex(r"""
    \text{s.t. } \sum_{t=1}^{T} \sum_{k=1}^{K} a_{ik} x_{kt} \leq C_i \quad \forall i
    """)
    
    st.markdown("""
    **Extension Reinforcement Learning:**
    """)
    
    st.latex(r"""
    Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]
    """)

# =============================================================================
# DOCUMENTATION COMPLÈTE (suite)
# =============================================================================

def documentation_telecom():
    st.header("📞 Théories des Télécommunications et Réseaux")
    
    st.markdown("""
    ## 🌐 Fondements des Réseaux Intelligents
    
    ### Théorie des Files d'Attente (Kendall, 1953)
    
    Application à l'optimisation des réseaux télécom:
    """)
    
    st.latex(r"""
    L = \lambda W
    """)
    
    st.markdown("""
    **Loi de Little - Applications réseaux:**
    - **L:** Nombre moyen clients dans système
    - **λ:** Taux d'arrivée moyen  
    - **W:** Temps moyen dans système
    """)
    
    st.markdown("""
    #### Files d'Attente M/M/1
    """)
    
    st.latex(r"""
    P_n = (1-\rho)\rho^n \quad \text{où} \quad \rho = \frac{\lambda}{\mu}
    """)
    
    st.markdown("""
    ### Théorie de l'Information (Shannon, 1948)
    
    Fondements mathématiques des communications:
    """)
    
    st.latex(r"""
    C = B \log_2(1 + \frac{S}{N})
    """)
    
    st.markdown("""
    **Capacité de canal - Applications 5G:**
    - **C:** Capacité maximale (bps)
    - **B:** Bande passante (Hz)
    - **S/N:** Rapport signal/bruit
    """)

def documentation_transport():
    st.header("🚚 Théories de la Logistique et Transport")
    
    st.markdown("""
    ## 🏗️ Optimisation des Systèmes Logistiques
    
    ### Problème du Voyageur de Commerce (TSP)
    
    Formulation mathématique classique:
    """)
    
    st.latex(r"""
    \min \sum_{i=1}^{n} \sum_{j=1}^{n} c_{ij} x_{ij}
    """)
    
    st.latex(r"""
    \text{s.t. } \sum_{j=1}^{n} x_{ij} = 1 \quad \forall i, \quad \sum_{i=1}^{n} x_{ij} = 1 \quad \forall j
    """)

def documentation_energie():
    st.header("⚡ Théories du Secteur Énergétique")
    
    st.markdown("""
    ## 🔋 Économie de l'Énergie et Smart Grids
    
    ### Théorie de la Tarification Dynamique
    
    Optimisation prix électricité en temps réel:
    """)
    
    st.latex(r"""
    p_t = MC_t + \lambda \cdot \frac{\partial D}{\partial p}
    """)

def documentation_algorithmes():
    st.header("🤖 Théories des Algorithmes et Machine Learning")
    
    st.markdown("""
    ## 🧠 Fondements Mathématiques du Machine Learning
    
    ### Théorie de l'Apprentissage Statistique (Vapnik, 1995)
    
    #### Risque Structurel (SRM):
    """)
    
    st.latex(r"""
    R(\alpha) \leq R_{emp}(\alpha) + \Phi(\frac{h}{n})
    """)
    
    st.markdown("""
    **Théorie VC-dimension:**
    """)
    
    st.latex(r"""
    \Phi(\frac{h}{n}) = \sqrt{\frac{h(\log\frac{2n}{h} + 1) - \log(\frac{\eta}{4})}{n}}
    """)

def documentation_technologie():
    st.header("🛠️ Théories des Systèmes Distribués")
    
    st.markdown("""
    ## 🏗️ Architecture des Systèmes Big Data
    
    ### Théorème CAP (Brewer, 2000)
    
    Fondement des bases de données distribuées:
    """)
    
    st.markdown("""
    **Un système distribué ne peut garantir simultanément:**
    - **C:** Cohérence (Consistency)
    - **A:** Disponibilité (Availability)  
    - **P:** Tolérance partition (Partition tolerance)
    """)

def documentation_metriques():
    st.header("📈 Théories de la Mesure et Métriques")
    
    st.markdown("""
    ## 📊 Métrologie Data-Driven
    
    ### Théorie de la Mesure (Lebesgue, 1902)
    
    Extension aux données complexes:
    """)
    
    st.latex(r"""
    \mu(E) = \inf \left\{ \sum_{k=1}^\infty \ell(I_k) : E \subseteq \bigcup_{k=1}^\infty I_k \right\}
    """)

# Fonctions auxiliaires pour données et visualisations
def create_technology_evolution_chart():
    """Crée un graphique d'évolution technologique"""
    years = list(range(2000, 2024))
    hadoop = [0, 0, 0, 1, 3, 8, 15, 25, 35, 45, 55, 65, 70, 75, 78, 80, 82, 84, 85, 86, 87, 88, 89, 90]
    spark = [0, 0, 0, 0, 0, 0, 0, 1, 5, 15, 30, 45, 60, 70, 75, 78, 80, 82, 84, 85, 86, 87, 88, 89]
    tensorflow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 25, 45, 60, 70, 75, 78, 80, 82, 84, 85]
    
    df = pd.DataFrame({
        'Year': years,
        'Hadoop': hadoop,
        'Spark': spark,
        'TensorFlow': tensorflow
    })
    
    fig = px.line(df, x='Year', y=['Hadoop', 'Spark', 'TensorFlow'], 
                 title="Évolution de l'Adoption des Technologies Big Data")
    return fig

if __name__ == "__main__":
    main()

# Footer avec références académiques
st.sidebar.markdown("---")
st.sidebar.header("📚 Références Académiques")

st.sidebar.markdown("""
**Ouvrages Fondamentaux:**
- 📖 "Big Data: A Revolution" - Mayer-Schönberger & Cukier
- 📖 "The Master Algorithm" - Pedro Domingos  
- 📖 "An Introduction to Statistical Learning" - James et al.

**Articles Scientifiques:**
- 🎓 "5V Big Data Framework" - Laney (2001)
- 🎓 "CRISP-DM Methodology" - Chapman et al. (2000)
- 🎓 "P4 Medicine" - Hood & Flores (2012)

**Théories Économiques:**
- 💰 "Market for Lemons" - Akerlof (1970)
- 💰 "Job Market Signaling" - Spence (1973)
- 💰 "Long Tail" - Anderson (2004)
""")