import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Cadre Méthodologique - Études de Cas Big Data",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour la structure pédagogique
st.markdown("""
<style>
    .methodology-step {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .step-number {
        background: white;
        color: #667eea;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 20px;
        margin-right: 15px;
    }
    .concept-card {
        background: #f8f9fa;
        border-left: 5px solid #28a745;
        padding: 20px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .tool-card {
        background: #e3f2fd;
        border: 1px solid #2196f3;
        padding: 15px;
        border-radius: 8px;
        margin: 5px;
    }
    .deliverable-card {
        background: #fff3cd;
        border: 1px solid #ffc107;
        padding: 15px;
        border-radius: 8px;
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🎓 Cadre Méthodologique pour Études de Cas Big Data")
    st.markdown("### Structure Pédagogique Complète - De la Problématique à la Solution")
    
    # Sélection du secteur et du cas
    col1, col2 = st.columns([1, 2])
    
    with col1:
        secteur = st.selectbox(
            "**1. Choix du Secteur**",
            [
                "🏥 Santé & Médical",
                "🏦 Finance & Banque", 
                "🛒 Retail & Commerce",
                "📞 Télécommunications",
                "🚚 Transport & Logistique",
                "⚡ Énergie & Utilities"
            ]
        )
        
        cas_etude = st.selectbox(
            "**2. Sélection du Cas d'Étude**",
            get_cas_etudes(secteur)
        )
    
    with col2:
        st.info(f"""
        **Secteur sélectionné:** {secteur}
        **Cas d'étude:** {cas_etude}
        """)
    
    # Affichage du cadre méthodologique
    afficher_cadre_methodologique(secteur, cas_etude)

def get_cas_etudes(secteur):
    """Retourne les cas d'étude disponibles par secteur"""
    cas_par_secteur = {
        "🏥 Santé & Médical": [
            "🔮 Système de Prédiction du Risque Cardio-Vasculaire",
            "🏥 Optimisation des Parcours Patients",
            "💊 Gestion Prédictive des Stocks Médicaments",
            "🩺 Diagnostic Assisté par IA"
        ],
        "🏦 Finance & Banque": [
            "🔍 Détection de Fraude en Temps Réel",
            "📊 Scoring Crédit avec Données Alternatives", 
            "📋 Conformité Réglementaire Automatisée",
            "⚠️ Gestion des Risques de Marché"
        ],
        "🛒 Retail & Commerce": [
            "🎯 Système de Recommandation Personnalisée",
            "📦 Optimisation de la Chaîne d'Approvisionnement",
            "💰 Pricing Dynamique Intelligent",
            "🗺️ Analyse du Parcours Client Multi-Canal"
        ],
        "📞 Télécommunications": [
            "📱 Segmentation Avancée de la Clientèle",
            "🎯 Marketing Prédictif et Fidélisation",
            "🚨 Détection de Fraude Réseau",
            "📊 Optimisation des Performances Réseau"
        ],
        "🚚 Transport & Logistique": [
            "🚛 Optimisation des Tournées de Livraison",
            "📦 Gestion Prédictive de la Flotte",
            "🔮 Prévision de la Demande Logistique",
            "🌱 Logistique Durable et Optimisée"
        ],
        "⚡ Énergie & Utilities": [
            "🔧 Maintenance Prédictive des Infrastructures",
            "💰 Optimisation des Achats d'Énergie",
            "🌞 Gestion des Smart Grids",
            "📈 Prévision de la Demande Énergétique"
        ]
    }
    return cas_par_secteur.get(secteur, [])

def afficher_cadre_methodologique(secteur, cas_etude):
    """Affiche le cadre méthodologique complet"""
    
    st.markdown("---")
    st.header(f"📋 Cadre Méthodologique: {cas_etude}")
    
    # Navigation through methodology steps
    steps = st.radio(
        "**Étapes de la Méthodologie**",
        [
            "1. 🎯 Contexte & Problématique", 
            "2. 📊 Analyse des Données",
            "3. 🛠️ Conception Solution",
            "4. 🔧 Implémentation Technique", 
            "5. 📈 Validation & Résultats",
            "6. 🚀 Déploiement & Monitoring"
        ],
        horizontal=True
    )
    
    if "1. 🎯 Contexte & Problématique" in steps:
        afficher_etape_1(secteur, cas_etude)
    elif "2. 📊 Analyse des Données" in steps:
        afficher_etape_2(secteur, cas_etude)
    elif "3. 🛠️ Conception Solution" in steps:
        afficher_etape_3(secteur, cas_etude)
    elif "4. 🔧 Implémentation Technique" in steps:
        afficher_etape_4(secteur, cas_etude)
    elif "5. 📈 Validation & Résultats" in steps:
        afficher_etape_5(secteur, cas_etude)
    elif "6. 🚀 Déploiement & Monitoring" in steps:
        afficher_etape_6(secteur, cas_etude)

def afficher_etape_1(secteur, cas_etude):
    """Étape 1: Contexte et Problématique"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">1</div>', unsafe_allow_html=True)
    with col2:
        st.header("🎯 Étape 1: Contexte & Problématique Business")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contexte sectoriel
    st.subheader("📖 Contexte Sectoriel")
    contexte = get_contexte_sectoriel(secteur)
    st.markdown(contexte)
    
    # Problématique business détaillée
    st.subheader("💡 Problématique Business")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎯 Objectifs Business:**")
        objectifs = get_objectifs_business(cas_etude)
        for obj in objectifs:
            st.markdown(f"- {obj}")
        
        st.markdown("**📊 Métriques d'Impact:**")
        metriques = get_metriques_impact(cas_etude)
        for metrique in metriques:
            st.markdown(f"- {metrique}")
    
    with col2:
        st.markdown("**⚠️ Défis et Contraintes:**")
        defis = get_defis_contraintes(cas_etude)
        for defi in defis:
            st.markdown(f"- {defi}")
        
        st.markdown("**🎯 Public Cible:**")
        public = get_public_cible(cas_etude)
        st.markdown(f"- {public}")
    
    # Étude de cas réelle
    st.subheader("🏢 Étude de Cas Réelle")
    cas_reel = get_cas_reel(secteur, cas_etude)
    st.success(cas_reel)
    
    # Questions clés pour l'analyse
    st.subheader("🔍 Questions Clés pour l'Analyse")
    questions = get_questions_cles(cas_etude)
    for i, question in enumerate(questions, 1):
        st.markdown(f"**{i}. {question}**")

def afficher_etape_2(secteur, cas_etude):
    """Étape 2: Analyse des Données"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">2</div>', unsafe_allow_html=True)
    with col2:
        st.header("📊 Étape 2: Analyse Exploratoire des Données")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sources de données
    st.subheader("🗃️ Inventaire des Sources de Données")
    sources = get_sources_donnees(cas_etude)
    
    for source_type, source_list in sources.items():
        with st.expander(f"**{source_type}**"):
            for source in source_list:
                st.markdown(f"- {source}")
    
    # Analyse de qualité des données
    st.subheader("🔍 Analyse de Qualité des Données")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📏 Dimensions de Qualité:**")
        dimensions = [
            "Exactitude et précision",
            "Complétude des données", 
            "Cohérence temporelle",
            "Validité des formats",
            "Unicité des enregistrements"
        ]
        for dimension in dimensions:
            st.markdown(f"- {dimension}")
    
    with col2:
        st.markdown("**🛠️ Outils d'Analyse:**")
        outils = [
            "Profiling automatique (Pandas Profiling)",
            "Détection d'anomalies (Great Expectations)",
            "Validation de schémas (Pydantic)",
            "Monitoring de drift (Evidently AI)"
        ]
        for outil in outils:
            st.markdown(f"- {outil}")
    
    # Feature Engineering
    st.subheader("⚙️ Feature Engineering")
    features = get_features_engineering(cas_etude)
    
    for feature_type, feature_list in features.items():
        with st.expander(f"**{feature_type}**"):
            for feature in feature_list:
                st.markdown(f"- {feature}")
    
    # Visualisation exploratoire
    st.subheader("📈 Analyse Visuelle Exploratoire")
    if st.button("🎨 Générer des Visualisations Types"):
        generer_visualisations_exploratoires(cas_etude)

def afficher_etape_3(secteur, cas_etude):
    """Étape 3: Conception de la Solution"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">3</div>', unsafe_allow_html=True)
    with col2:
        st.header("🛠️ Étape 3: Conception de la Solution Data-Driven")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Architecture solution
    st.subheader("🏗️ Architecture de la Solution")
    architecture = get_architecture_solution(cas_etude)
    st.markdown(architecture)
    
    # Sélection algorithmique
    st.subheader("🤖 Sélection des Algorithmes")
    algorithmes = get_algorithmes_recommandes(cas_etude)
    
    for algo_type, algo_list in algorithmes.items():
        with st.expander(f"**{algo_type}**"):
            for algo in algo_list:
                st.markdown(f"- **{algo['nom']}**: {algo['description']}")
                st.markdown(f"  *Avantages*: {algo['avantages']}")
                st.markdown(f"  *Cas d'usage*: {algo['usage']}")
    
    # Métriques d'évaluation
    st.subheader("📊 Métriques d'Évaluation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎯 Métriques Techniques:**")
        metriques_tech = get_metriques_techniques(cas_etude)
        for metrique in metriques_tech:
            st.markdown(f"- {metrique}")
    
    with col2:
        st.markdown("**💼 Métriques Business:**")
        metriques_business = get_metriques_business(cas_etude)
        for metrique in metriques_business:
            st.markdown(f"- {metrique}")
    
    # Plan de validation
    st.subheader("🔬 Plan de Validation")
    st.markdown("""
    **1. Validation Technique:**
    - Split train/test/validation
    - Cross-validation stratifiée
    - Tests statistiques d'hypothèses
    
    **2. Validation Business:**
    - A/B testing en environnement contrôlé
    - Analyse coût-bénéfice
    - Étude d'impact opérationnel
    """)

def afficher_etape_4(secteur, cas_etude):
    """Étape 4: Implémentation Technique"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">4</div>', unsafe_allow_html=True)
    with col2:
        st.header("🔧 Étape 4: Implémentation Technique Détaillée")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Stack technologique
    st.subheader("🛠️ Stack Technologique Recommandée")
    stack = get_stack_technologique(cas_etude)
    
    for layer, technologies in stack.items():
        with st.expander(f"**{layer}**"):
            for tech in technologies:
                st.markdown(f"- **{tech['nom']}**: {tech['description']}")
    
    # Code exemple
    st.subheader("💻 Extrait de Code Illustratif")
    code_exemple = get_code_exemple(cas_etude)
    st.code(code_exemple, language='python')
    
    # Pipeline de données
    st.subheader("⚡ Pipeline de Données")
    st.markdown("""
    **1. Ingestion des Données:**
    ```python
    # Workflow d'ingestion
    sources → validation → stockage → processing
    ```
    
    **2. Feature Store:**
    ```python
    # Gestion des features
    features → versioning → serving → monitoring
    ```
    
    **3. Serving des Modèles:**
    ```python
    # MLOps pipeline
    training → validation → deployment → monitoring
    ```
    """)
    
    # Bonnes pratiques
    st.subheader("📝 Bonnes Pratiques d'Implémentation")
    pratiques = [
        "Versioning du code (Git) et des données (DVC)",
        "Tests unitaires et d'intégration automatisés",
        "Documentation technique complète",
        "Monitoring des performances en temps réel",
        "Gestion des erreurs et reprise sur incident"
    ]
    
    for pratique in pratiques:
        st.markdown(f"- {pratique}")

def afficher_etape_5(secteur, cas_etude):
    """Étape 5: Validation et Résultats"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">5</div>', unsafe_allow_html=True)
    with col2:
        st.header("📈 Étape 5: Validation des Résultats et Impact Business")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Résultats techniques
    st.subheader("🎯 Résultats Techniques")
    resultats_tech = get_resultats_techniques(cas_etude)
    
    for metrique, valeur in resultats_tech.items():
        st.metric(metrique, valeur['valeur'], valeur.get('evolution', ''))
    
    # Impact business
    st.subheader("💼 Impact Business Mesuré")
    impact_business = get_impact_business(cas_etude)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📊 Avant la Solution:**")
        for point in impact_business['avant']:
            st.markdown(f"- {point}")
    
    with col2:
        st.markdown("**🚀 Après la Solution:**")
        for point in impact_business['apres']:
            st.markdown(f"- {point}")
    
    # ROI calculé
    st.subheader("💰 Analyse ROI")
    roi_data = get_analyse_roi(cas_etude)
    
    st.plotly_chart(create_roi_chart(roi_data), use_container_width=True)
    
    # Leçons apprises
    st.subheader("🎓 Leçons Apprises et Best Practices")
    lecons = get_lecons_apprises(cas_etude)
    
    for lecon in lecons:
        st.markdown(f"- **{lecon['categorie']}**: {lecon['description']}")

def afficher_etape_6(secteur, cas_etude):
    """Étape 6: Déploiement et Monitoring"""
    
    st.markdown('<div class="methodology-step">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown('<div class="step-number">6</div>', unsafe_allow_html=True)
    with col2:
        st.header("🚀 Étape 6: Déploiement en Production et Monitoring")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Stratégie de déploiement
    st.subheader("📦 Stratégie de Déploiement")
    st.markdown("""
    **1. Déploiement Progressif:**
    - Phase 1: Environnement de test (5% du trafic)
    - Phase 2: Rollout progressif (25% → 50% → 100%)
    - Phase 3: Déploiement complet avec fallback
    
    **2. Canary Deployment:**
    ```python
    # Workflow de déploiement
    new_version → A/B testing → metrics analysis → full rollout
    ```
    """)
    
    # Monitoring et alerting
    st.subheader("📊 Monitoring en Production")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔍 Métriques à Surveiller:**")
        metriques_monitoring = [
            "Performance modèle (latence, throughput)",
            "Qualité prédictions (drift detection)",
            "Utilisation ressources infrastructure",
            "Erreurs et exceptions"
        ]
        for metrique in metriques_monitoring:
            st.markdown(f"- {metrique}")
    
    with col2:
        st.markdown("**🚨 Système d'Alerte:**")
        alertes = [
            "Alertes performance (seuils configurés)",
            "Alertes qualité données (anomalies)",
            "Alertes business (KPI dégradés)",
            "Alertes technique (erreurs système)"
        ]
        for alerte in alertes:
            st.markdown(f"- {alerte}")
    
    # Maintenance et évolution
    st.subheader("🔄 Maintenance et Amélioration Continue")
    st.markdown("""
    **1. Re-entraînement des Modèles:**
    - Planifié (hebdomadaire/mensuel)
    - Déclenché (drift detection)
    - Manuel (nouvelles données disponibles)
    
    **2. Évolution de la Solution:**
    - Ajout nouvelles features
    - Optimisation performance
    - Adaptation changements métier
    """)
    
    # Checklist de déploiement
    st.subheader("✅ Checklist Pré-Déploiement")
    checklist = [
        "Tests de charge et performance validés",
        "Plan de rollback préparé",
        "Documentation utilisateur complète",
        "Équipe support formée",
        "Monitoring configuré et testé"
    ]
    
    for item in checklist:
        st.checkbox(item)

# =============================================================================
# FONCTIONS DE DONNÉES PÉDAGOGIQUES (À COMPLÉTER)
# =============================================================================

def get_contexte_sectoriel(secteur):
    """Retourne le contexte sectoriel"""
    contextes = {
        "🏥 Santé & Médical": """
        **Enjeux du secteur santé:**
        - Augmentation des coûts de santé
        - Vieillissement de la population  
        - Pénurie de personnel soignant
        - Digitalisation des parcours patients
        - Explosion des données médicales
        
        **Opportunités Big Data:**
        - Médecine personnalisée et prédictive
        - Optimisation des ressources médicales
        - Amélioration de la qualité des soins
        - Réduction des erreurs médicales
        """,
        "🏦 Finance & Banque": """
        **Enjeux du secteur financier:**
        - Réglementation croissante (AML/KYC)
        - Concurrence des fintechs
        - Attentes clients en temps réel
        - Cybercriminalité sophistiquée
        
        **Opportunités Big Data:**
        - Détection de fraude avancée
        - Expérience client personnalisée
        - Optimisation des risques
        - Automatisation des processus
        """
    }
    return contextes.get(secteur, "Contexte sectoriel en cours de développement...")

def get_objectifs_business(cas_etude):
    """Retourne les objectifs business"""
    objectifs = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": [
            "Réduction de 30% des événements cardiaques non détectés",
            "Détection précoce 6 mois avant manifestation clinique",
            "Personnalisation des plans de prévention",
            "Optimisation des coûts de prise en charge"
        ],
        "🔍 Détection de Fraude en Temps Réel": [
            "Réduction de 60% des pertes liées à la fraude",
            "Temps de détection inférieur à 50ms",
            "Réduction des faux positifs de 40%",
            "Amélioration de l'expérience client légitime"
        ]
    }
    return objectifs.get(cas_etude, ["Objectifs en cours de définition..."])

def get_metriques_impact(cas_etude):
    """Retourne les métriques d'impact"""
    metriques = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": [
            "Sensibilité: >90%",
            "Spécificité: >85%", 
            "AUC-ROC: >0.90",
            "Valeur prédictive positive: >80%"
        ],
        "🔍 Détection de Fraude en Temps Réel": [
            "Precision: >95%",
            "Recall: >90%",
            "F1-Score: >92%",
            "Taux faux positifs: <2%"
        ]
    }
    return metriques.get(cas_etude, ["Métriques en cours de définition..."])

def get_defis_contraintes(cas_etude):
    """Retourne les défis et contraintes"""
    defis = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": [
            "Qualité variable des données médicales",
            "Conformité RGPD et secret médical",
            "Interprétabilité des modèles pour les médecins",
            "Intégration avec les systèmes existants"
        ],
        "🔍 Détection de Fraude en Temps Réel": [
            "Latence extrême requise (<100ms)",
            "Évolution constante des techniques de fraude",
            "Équilibre sécurité/expérience utilisateur",
            "Volume de données à traiter en temps réel"
        ]
    }
    return defis.get(cas_etude, ["Défis en cours d'identification..."])

def get_public_cible(cas_etude):
    """Retourne le public cible"""
    publics = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": "Médecins généralistes, cardiologues, assureurs santé, patients à risque",
        "🔍 Détection de Fraude en Temps Réel": "Équipes fraude, compliance, relation client, direction des risques"
    }
    return publics.get(cas_etude, "Public cible en cours de définition...")

def get_cas_reel(secteur, cas_etude):
    """Retourne un cas réel"""
    cas_reels = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": "**American Heart Association** - Réduction de 35% des infarctus grâce au score ASCVD basé sur l'analyse de 25,000 patients sur 10 ans",
        "🔍 Détection de Fraude en Temps Réel": "**PayPal** - Traitement de 2+ pétaoctets de données, détection de fraude en 50ms, réduction des pertes de 60%"
    }
    return cas_reels.get(cas_etude, "Cas réel en cours de documentation...")

def get_questions_cles(cas_etude):
    """Retourne les questions clés"""
    questions = {
        "🔮 Système de Prédiction du Risque Cardio-Vasculaire": [
            "Quelles variables ont le plus d'impact sur le risque cardio-vasculaire?",
            "Comment équilibrer sensibilité et spécificité selon la population cible?",
            "Quel est le meilleur horizon temporel pour la prédiction?",
            "Comment intégrer les nouvelles données en temps réel?"
        ],
        "🔍 Détection de Fraude en Temps Réel": [
            "Quels patterns comportementaux indiquent une activité frauduleuse?",
            "Comment adapter le modèle à l'évolution des techniques de fraude?",
            "Quel niveau de faux positifs est acceptable business?",
            "Comment optimiser le trade-off entre précision et latence?"
        ]
    }
    return questions.get(cas_etude, ["Questions en cours de formulation..."])

# Les autres fonctions (get_sources_donnees, get_features_engineering, etc.) suivent le même pattern...

def get_sources_donnees(cas_etude):
    """Retourne les sources de données"""
    # Implémentation similaire aux fonctions précédentes
    return {"Source 1": ["Donnée A", "Donnée B"]}

def get_features_engineering(cas_etude):
    """Retourne le feature engineering"""
    return {"Type 1": ["Feature A", "Feature B"]}

def get_architecture_solution(cas_etude):
    """Retourne l'architecture de solution"""
    return "Architecture en cours de développement..."

def get_algorithmes_recommandes(cas_etude):
    """Retourne les algorithmes recommandés"""
    return {"Catégorie": [{"nom": "Algo", "description": "desc", "avantages": "av", "usage": "us"}]}

def get_metriques_techniques(cas_etude):
    """Retourne les métriques techniques"""
    return ["Métrique 1", "Métrique 2"]

def get_metriques_business(cas_etude):
    """Retourne les métriques business"""
    return ["Métrique business 1", "Métrique business 2"]

def get_stack_technologique(cas_etude):
    """Retourne la stack technologique"""
    return {"Couche": [{"nom": "Tech", "description": "desc"}]}

def get_code_exemple(cas_etude):
    """Retourne un exemple de code"""
    return "# Code exemple en cours de développement..."

def get_resultats_techniques(cas_etude):
    """Retourne les résultats techniques"""
    return {"Métrique": {"valeur": "X", "evolution": "+Y%"}}

def get_impact_business(cas_etude):
    """Retourne l'impact business"""
    return {"avant": ["Point 1"], "apres": ["Point 2"]}

def get_analyse_roi(cas_etude):
    """Retourne l'analyse ROI"""
    return {"data": []}

def get_lecons_apprises(cas_etude):
    """Retourne les leçons apprises"""
    return [{"categorie": "Cat", "description": "Desc"}]

def generer_visualisations_exploratoires(cas_etude):
    """Génère des visualisations exploratoires"""
    # Implémentation des visualisations
    st.plotly_chart(px.bar(x=[1,2,3], y=[1,2,3]), use_container_width=True)

def create_roi_chart(roi_data):
    """Crée un graphique ROI"""
    return px.line(x=[1,2,3], y=[1,2,3])

if __name__ == "__main__":
    main()

# Section documentation pédagogique
st.sidebar.markdown("---")
st.sidebar.header("🎓 Documentation Pédagogique")

st.sidebar.markdown("""
**📚 Objectifs Pédagogiques:**
- Comprendre la méthodologie complète d'un projet Big Data
- Maîtriser les étapes de conception à déploiement
- Appliquer les bonnes pratiques sectorielles
- Développer une pensée critique data-driven

**🔄 Comment Utiliser ce Framework:**
1. Sélectionnez votre secteur et cas d'étude
2. Suivez les 6 étapes méthodologiques
3. Prenez notes des concepts clés
4. Appliquez à vos propres projets

**⏱️ Temps d'Apprentissage Estimé:**
- Par cas d'étude: 2-3 heures
- Par secteur: 8-12 heures  
- Maîtrise complète: 40-60 heures
""")