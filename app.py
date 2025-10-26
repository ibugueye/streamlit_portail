import streamlit as st
import json
from pathlib import Path
import os
import streamlit as st

# Get the directory of the current script
current_dir = os.path.dirname(__file__)
pdf_path = os.path.join(current_dir, "assets", "portfolio.pdf")

try:
    with open(pdf_path, "rb") as f:
        data = f.read()
except FileNotFoundError:
    st.error("PDF file not found. Please check the file path.")

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Portail Streamlit - Ibrahima Gueye",
    page_icon="🚀",
    layout="wide"
)

# --- MENU LATÉRAL ---
st.sidebar.image("assets/logo.png", use_column_width=True)
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
    st.header("🎯 Vision")
    st.write("""
    Je crois en une **synergie entre la Data Science et le Contrôle de Gestion** pour transformer la performance
    des entreprises africaines.  
    Mon objectif est d’aider les dirigeants, les étudiants et les entrepreneurs à exploiter le **pouvoir des données**
    pour **décider mieux, plus vite et plus juste**.
    """)

    st.header("💼 Compétences clés")
    st.markdown("""
    - 📊 **Analyse Financière & Modélisation Excel/Python**
    - 🤖 **Machine Learning et IA appliquée**
    - 🧠 **Contrôle de Gestion et Pilotage de la Performance**
    - 🌍 **Création de Dashboards Interactifs (Streamlit, Power BI)**
    - 🧩 **Déploiement d’Apps via MLflow, Docker & Render**
    """)

    st.header("📘 Parcours & Réalisations")
    st.write("""
    Diplômé en **Data Science et Management**, j’ai conçu plusieurs applications pédagogiques et professionnelles
    pour la **formation**, la **finance**, la **gestion hôtelière** et le **scoring de crédit**., **initiation en Datascience
 et Machine Learning**., et **analyse financière avancée**., entre autres""")

    st.download_button(
        "📄 Télécharger mon Portfolio (PDF)",
        data=open("assets/portfolio.pdf", "rb").read(),
        file_name="Portfolio_Ibrahima_Gueye.pdf",
        mime="application/pdf"
    )

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

    with open("apps.json", "r", encoding="utf-8") as f:
        apps = json.load(f)

    categories = sorted(set(app["category"] for app in apps))
    selected_category = st.radio("🗂️ Filtrer par catégorie :", ["Toutes"] + categories, horizontal=True)

    if selected_category != "Toutes":
        apps = [app for app in apps if app["category"] == selected_category]

    cols = st.columns(2)
    for i, app in enumerate(apps):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div style='background-color:#f9f9f9; border:1px solid #ddd; border-radius:12px; padding:20px; margin-bottom:15px;'>
                <h3>{app['name']}</h3>
                <p style='color:#333;'>{app['description']}</p>
                <a href='{app['url']}' target='_blank'>
                    <button style='background-color:#0078ff; color:white; border:none; border-radius:8px; padding:10px 20px; cursor:pointer;'>🌐 Ouvrir</button>
                </a>
            </div>
            """, unsafe_allow_html=True)

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
    st.markdown("""
    **📧 Email :** [ibugueye@gmail.com](mailto:ibugueye@gmail.com)  
    **💼 LinkedIn :** [linkedin.com/in/ibrahima-gueye](https://www.linkedin.com/)  
    **🐙 GitHub :** [github.com/ibrahimagueye](https://github.com/)  
    **📱 Téléphone :** +33 7 83 51 62 33  
    """)

    st.divider()
    st.markdown("Merci de visiter mon portail professionnel 🙏")
