import streamlit as st
import json
from pathlib import Path
import os

# --- GESTION SÉCURISÉE DU PDF ---
def load_pdf():
    """Charge le fichier PDF de manière sécurisée"""
    try:
        # Essayer plusieurs chemins possibles
        possible_paths = [
            "assets/portfolio.pdf",
            "../assets/portfolio.pdf",
            "./portfolio.pdf",
            "portfolio.pdf"
        ]
        
        for pdf_path in possible_paths:
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:
                    return f.read()
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement du PDF: {e}")
        return None

# Chargement du PDF
pdf_data = load_pdf()

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Portail Streamlit - Ibrahima Gueye",
    page_icon="🚀",
    layout="wide"
)

# --- MENU LATÉRAL ---
# Gestion sécurisée du logo
try:
    st.sidebar.image("assets/logo.png", use_column_width=True)
except:
    st.sidebar.markdown("### 🎯 Mon Portfolio")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["🏠 À propos", "💻 Applications", "📬 Contact"])

# --- PAGE 1 : À PROPOS ---
if page == "🏠 À propos":
    st.markdown(
        """
        <div style='background:linear-gradient(90deg, #004aad, #0078ff); padding:40px; border-radius:10px; text-align:center; color:white'>
            <h1>🚀 Ibrahima Gueye</h1>
            <p style='font-size:20px;'>Data Scientist & Contrôleur de Gestion</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    
    # Navigation interne pour la page À propos
    about_menu = st.radio("Navigation du profil", 
                         ["🎯 Vision & Positionnement", "📚 Formations", "💼 Expériences", "🛠️ Compétences", "📖 Mon Parcours", "🚀 Réalisations"], 
                         horizontal=True)
    
    st.markdown("---")

    if about_menu == "🎯 Vision & Positionnement":
        st.header("🎯 Vision & Positionnement")
        st.write("""
        **« Du contrôle de gestion à la data science, en passant par les réseaux et télécoms, 
        j'ai construit un parcours riche et transversal qui relie finance, informatique et innovation. »**
        
        Je crois en une **synergie entre la Data Science et le Contrôle de Gestion** pour transformer la performance
        des entreprises. Mon objectif est d'aider les dirigeants, les étudiants et les entrepreneurs à exploiter 
        le **pouvoir des données** pour **décider mieux, plus vite et plus juste**.
        
        ### 🎯 Mon Positioning Actuel
        
        **« Data Scientist et Contrôleur de Gestion, capable de combiner vision business, 
        expertise technique et maîtrise analytique pour créer de la valeur. »**
        """)

    elif about_menu == "📚 Formations":
        st.header("🎓 Parcours de Formation")
        
        formations = [
            "**Data Analyst & Data Scientist** – OpenClassrooms / Centrale Supélec",
            "**Master Réseaux et Télécommunications (VAE)**",
            "**Formation Administration Réseaux** – UPMC",
            "**Chef de projet** – Conception & Développement d'applications informatiques",
            "**DUT Gestion**",
            "**BTS Comptabilité**",
            "**Comptabilité A, B1, B2** – CNAM",
            "**Cours de mathématiques** – CNAM",
            "**Contrôle de gestion** – École des Cadres",
            "**Gestion de la paie**",
            "**Formation micro-réseaux** – GRETA de Paris",
            "**Maintenance informatique, sécurité réseau, hotline**"
        ]
        
        for formation in formations:
            st.markdown(f"• {formation}")

    elif about_menu == "💼 Expériences":
        st.header("💼 Expériences Professionnelles")
        
        experiences = [
            "**Analyste principal** – Backbone France Télécom",
            "**Supervision Réseaux Télécom**",
            "**Support Technique Informatique**",
            "**Ingénieur Commercial Informatique**",
            "**Technicien Réseaux & Télécom**",
            "**Night Audit** – Hôtellerie",
            "**Serveur Restaurant & Bar**"
        ]
        
        st.subheader("Parcours Évolutif")
        for exp in experiences:
            st.markdown(f"• {exp}")

    elif about_menu == "🛠️ Compétences":
        st.header("🛠️ Compétences Techniques et Professionnelles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💻 Techniques")
            competences_tech = [
                "Réseaux & Télécoms",
                "Sécurité Informatique", 
                "Supervision Réseaux",
                "Data Science (Python, ML, Streamlit)",
                "SQL",
                "Administration Systèmes"
            ]
            for comp in competences_tech:
                st.markdown(f"• {comp}")
        
        with col2:
            st.subheader("📊 Gestion & Finance")
            competences_gest = [
                "Comptabilité",
                "Contrôle de Gestion",
                "Gestion de la Paie",
                "Analyse Financière"
            ]
            for comp in competences_gest:
                st.markdown(f"• {comp}")
        
        st.subheader("🌟 Soft Skills")
        soft_skills = [
            "Relation client", 
            "Gestion de projet", 
            "Résolution de problèmes", 
            "Adaptabilité",
            "Rigueur analytique",
            "Sens du service"
        ]
        for skill in soft_skills:
            st.markdown(f"• {skill}")

    elif about_menu == "📖 Mon Parcours":
        st.header("📖 Mon Histoire Professionnelle")
        
        st.markdown("""
        ### 🔄 Mon Parcours en 3 Actes
        
        **1. 🏨 Hôtellerie & Restauration** 
        *Night Auditor & Serveur*
        - Rigueur et sens du service
        - Attention aux détails
        - Relation client
        
        **2. 📊 Comptabilité & Contrôle de Gestion** 
        *Formation et expertise métier*
        - Discipline analytique
        - Structuration des données financières
        - Donner du sens aux chiffres
        
        **3. 🌐 Réseaux & Télécoms → Data Science**
        *Évolution technique*
        - Infrastructure critiques et supervision
        - Analyste principal sur backbone France Télécom
        - Transformation vers la data science pour comprendre, prédire, anticiper
        
        ---
        
        ### 🧭 Mon Fil Rouge
        
        *« L'apprentissage continu et la capacité à relier des univers différents pour créer une valeur unique. »*
        
        **Depuis mes premières expériences comme night auditor et serveur**, j'ai découvert l'importance du détail, 
        de la rigueur et de la relation client.
        
        **Avec mes études en comptabilité et contrôle de gestion**, j'ai appris à structurer, analyser et donner du sens aux chiffres.
        
        **Cette curiosité m'a naturellement conduit vers les réseaux et télécoms** : administration, sécurité, supervision... 
        jusqu'à devenir analyste principal sur le backbone France Télécom.
        
        **Mais je voulais aller plus loin** : comprendre, prédire, anticiper. C'est ce qui m'a ouvert la voie de la data science. 
        
        **Aujourd'hui, je suis capable d'assembler ces trois mondes** – finance, informatique et data – pour apporter des solutions innovantes.
        """)

    elif about_menu == "🚀 Réalisations":
        st.header("🚀 Mes Réalisations & Projets")
        
        st.markdown("""
        ### 🎯 Vision Stratégique
        
        Diplômé en **Data Science et Management**, j'ai conçu plusieurs applications pédagogiques et professionnelles
        pour la **formation**, la **finance**, la **gestion hôtelière** et le **scoring de crédit**, **initiation en Data Science
        et Machine Learning**, et **analyse financière avancée**, entre autres.
        """)
        
        # Section Applications et Projets
        st.subheader("💻 Domaines d'Expertise & Réalisations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ##### 📊 Data Science & Analyse
            - **Analyse Financière Avancée** - Modélisation Excel/Python
            - **Machine Learning et IA appliquée** 
            - **Dashboards Interactifs** (Streamlit, Power BI)
            - **Scoring de Crédit Automatisé**
            - **Outils de Prédiction Business**
            """)
            
            st.markdown("""
            ##### 🌐 Réseaux & Télécoms
            - **Systèmes de Supervision Réseau**
            - **Outils d'Analyse de Performance**
            - **Solutions de Sécurité Informatique**
            - **Monitoring d'Infrastructures Critiques**
            """)
        
        with col2:
            st.markdown("""
            ##### 🏨 Gestion & Finance
            - **Systèmes de Gestion Hôtelière**
            - **Outils de Contrôle de Gestion**
            - **Applications Comptables Automatisées**
            - **Solutions de Gestion de Paie**
            """)
            
            st.markdown("""
            ##### 🎓 Pédagogie & Formation
            - **Plateformes de Formation Data Science**
            - **Outils d'Apprentissage Machine Learning**
            - **Applications d'Initiation à la Programmation**
            - **Dashboard Éducatifs Interactifs**
            """)
        
        # Section Déploiement
        st.subheader("🛠️ Technologies Maîtrisées")
        st.markdown("""
        - **Déploiement d'Apps** via MLflow, Docker & Render
        - **Architecture Cloud** et solutions scalables
        - **Intégration Continue** et déploiement automatique
        - **Bases de données** SQL et NoSQL
        - **APIs RESTful** et microservices
        - **Streamlit, Python, Machine Learning**
        - **Power BI, Excel avancé, VBA**
        """)
    
    # Bouton de téléchargement du PDF (toujours visible)
    st.markdown("---")
    if pdf_data:
        st.download_button(
            "📄 Télécharger mon Portfolio (PDF)",
            data=pdf_data,
            file_name="Portfolio_Ibrahima_Gueye.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("📄 Portfolio PDF non disponible pour le moment")

# --- PAGE 2 : APPLICATIONS ---
elif page == "💻 Applications":
    st.markdown(
        """
        <div style='background:linear-gradient(90deg, #004aad, #0078ff); padding:25px; border-radius:10px; text-align:center; color:white'>
            <h2>💻 Mes Applications Streamlit</h2>
            <p>Explorez mes projets en Finance, IA, Éducation et Marketing</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gestion sécurisée du fichier apps.json
    try:
        with open("apps.json", "r", encoding="utf-8") as f:
            apps = json.load(f)
    except FileNotFoundError:
        st.error("Fichier apps.json non trouvé")
        apps = []
    except json.JSONDecodeError:
        st.error("Erreur de lecture du fichier apps.json")
        apps = []

    if apps:
        categories = sorted(set(app.get("category", "Non catégorisé") for app in apps))
        selected_category = st.radio("🗂️ Filtrer par catégorie :", ["Toutes"] + categories, horizontal=True)

        if selected_category != "Toutes":
            apps = [app for app in apps if app.get("category") == selected_category]

        cols = st.columns(2)
        for i, app in enumerate(apps):
            col = cols[i % 2]
            with col:
                st.markdown(f"""
                <div style='background-color:#f9f9f9; border:1px solid #ddd; border-radius:12px; padding:20px; margin-bottom:15px;'>
                    <h3>{app.get('name', 'Application sans nom')}</h3>
                    <p style='color:#333;'>{app.get('description', 'Description non disponible')}</p>
                    <a href='{app.get('url', '#')}' target='_blank'>
                        <button style='background-color:#0078ff; color:white; border:none; border-radius:8px; padding:10px 20px; cursor:pointer;'>🌐 Ouvrir</button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Aucune application disponible pour le moment")

# --- PAGE 3 : CONTACT ---
elif page == "📬 Contact":
    st.markdown(
        """
        <div style='background:linear-gradient(90deg, #0078ff, #00b4d8); padding:30px; border-radius:10px; text-align:center; color:white'>
            <h2>📬 Contact</h2>
            <p>Restons connectés !</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📞 Coordonnées")
        st.markdown("""
        **📧 Email :** [ibugueye@gmail.com](mailto:ibugueye@gmail.com)  
        **💼 LinkedIn :** [linkedin.com/in/ibrahima-gueye](https://www.linkedin.com/)  
        **🐙 GitHub :** [github.com/ibrahimagueye](https://github.com/)  
        **📱 Téléphone :** +33 7 83 51 62 33  
        """)
    
    with col2:
        st.subheader("🎯 Domaines d'Expertise")
        st.markdown("""
        - Data Science & Analyse
        - Contrôle de Gestion
        - Réseaux & Télécoms
        - Développement d'Applications
        - Supervision Technique
        - Formation & Pédagogie
        """)

    st.divider()
    
    # Résumé LinkedIn
    st.subheader("👨‍💻 Profil Professionnel")
    st.markdown("""
    **« Data Scientist et Contrôleur de Gestion, capable de combiner vision business, 
    expertise technique et maîtrise analytique pour créer de la valeur. »**
    
    Mon expérience m'a permis de naviguer entre différents univers :
    - **🏨 Hôtellerie & restauration** : rigueur et sens du service
    - **📊 Comptabilité & contrôle de gestion** : discipline analytique  
    - **🌐 Réseaux & télécoms** : infrastructures critiques et supervision technique
    - **🤖 Data Science & analyse de données** : transformation de données complexes en leviers stratégiques
    """)
    
    st.markdown("---")
    st.markdown("Merci de visiter mon portail professionnel 🙏")

# --- SIDEBAR AMÉLIORÉE ---
with st.sidebar:
    st.markdown("---")
    st.header("📞 Contact Rapide")
    st.markdown("""
    **Email:** ibugueye@gmail.com  
    **Tél:** +33 7 83 51 62 33
    **LinkedIn:** [Ibrahima Gueye](https://linkedin.com/in/ibucoumba/)  
    **GitHub:** [ibugueye](https://github.com/ibugueye/)
    """)
    
    st.header("🎯 Expertises")
    st.markdown("""
    - Data Science & Analyse
    - Contrôle de Gestion
    - Réseaux & Télécoms
    - Développement d'Apps
    - Formation & Pédagogie
    """)
    
    # Indicateur de statut PDF
    st.markdown("---")
    if pdf_data:
        st.success("✅ Portfolio disponible")
    else:
        st.warning("📄 Portfolio en cours")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
    Construit avec Streamlit 🚀<br>
    © 2024 - Ibrahima Gueye
    </div>
    """, unsafe_allow_html=True)

# Footer pour toutes les pages
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2024 - Tous droits réservés | Ibrahima Gueye | Construit avec Streamlit 🚀"
    "</div>", 
    unsafe_allow_html=True
)