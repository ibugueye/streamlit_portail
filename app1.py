import streamlit as st
import os
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Mon Portail Professionnel",
    page_icon="🚀",
    layout="wide"
)

# Gestion sécurisée du fichier PDF
def load_pdf():
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
        
        # Si aucun fichier n'est trouvé
        st.warning("📄 Portfolio PDF non trouvé. Le fichier sera affiché une fois disponible.")
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement du PDF: {e}")
        return None

# Chargement du PDF
pdf_data = load_pdf()

# Header avec photo de profil
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/200x200/4B8BBE/FFFFFF?text=Photo+Profil", 
             width=200, caption="Votre Photo de Profil")

with col2:
    st.title("👋 Bienvenue sur mon Portail Professionnel")
    st.markdown("""
    **Data Scientist | Contrôleur de Gestion | Expert Réseaux & Télécoms**
    
    *Du contrôle de gestion à la data science, en passant par les réseaux et télécoms, 
    j'ai construit un parcours riche et transversal qui relie finance, informatique et innovation.*
    """)

# Navigation
st.markdown("---")
menu = st.radio("Navigation", ["📚 Formations", "💼 Expériences", "🛠️ Compétences", "📖 Mon Parcours", "📄 Portfolio"], horizontal=True)

st.markdown("---")

if menu == "📚 Formations":
    st.header("🎓 Formations Académiques")
    
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

elif menu == "💼 Expériences":
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

elif menu == "🛠️ Compétences":
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

elif menu == "📖 Mon Parcours":
    st.header("📖 Mon Histoire Professionnelle")
    
    st.markdown("""
    ### 🎯 Mon Positioning Actuel
    
    **« Data Scientist et Contrôleur de Gestion, capable de combiner vision business, 
    expertise technique et maîtrise analytique pour créer de la valeur. »**
    
    ---
    
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
    
    Aujourd'hui, je rassemble ces trois mondes - **finance, informatique et data** - 
    pour apporter des solutions innovantes et créer des ponts entre la technique et le business.
    """)

elif menu == "📄 Portfolio":
    st.header("📄 Mon Portfolio")
    
    if pdf_data:
        st.download_button(
            label="📥 Télécharger mon Portfolio PDF",
            data=pdf_data,
            file_name="portfolio.pdf",
            mime="application/pdf"
        )
        
        st.markdown("""
        ### 📋 Contenu du Portfolio
        
        Mon portfolio présente mes projets récents dans les domaines :
        - **Data Science & Analyse de données**
        - **Développement d'applications** 
        - **Supervision réseau et télécoms**
        - **Outils de gestion et analyse financière**
        
        *Téléchargez le PDF pour découvrir mes réalisations détaillées.*
        """)
    else:
        st.info("""
        ### 📄 Portfolio en préparation
        
        Mon portfolio complet est actuellement en cours de finalisation.
        Il présentera mes projets en :
        - Data Science & Machine Learning
        - Développement d'applications Streamlit
        - Analyse de données business
        - Solutions techniques innovantes
        
        **Disponible prochainement !**
        """)

# Sidebar avec informations de contact
with st.sidebar:
    st.header("📞 Contact")
    st.markdown("""
    **Email:** ibugueye@ngorweb.com  
    **Téléphone:** +33 783 51 62 33 
    **LinkedIn:** [Votre Profil](https://linkedin.com/in/ibucoumba/)  
    **GitHub:** [Votre GitHub](https://github.com/ibugueye/)
    """)
    
    st.header("🎯 Domaines d'Expertise")
    st.markdown("""
    - Data Science & Analyse
    - Contrôle de Gestion
    - Réseaux & Télécoms
    - Développement d'Applications
    - Supervision Technique
    """)
    
    # Indicateur de statut PDF
    if pdf_data:
        st.success("✅ Portfolio disponible")
    else:
        st.warning("📄 Portfolio en cours")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2024 - Tous droits réservés | Construit avec Streamlit 🚀"
    "</div>", 
    unsafe_allow_html=True
)