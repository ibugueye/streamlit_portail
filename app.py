import streamlit as st
import json

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Portail des Applications Streamlit - Ibrahima Gueye",
    page_icon="🚀",
    layout="wide"
)

# --- HEADER ---
st.title("🚀 Portail des Applications Streamlit")
st.markdown("### Centralisation de toutes mes applications hébergées sur Render")
st.markdown("Explorez mes différents projets : finance, IA, éducation, hôtellerie et plus encore.")

st.divider()

# --- CHARGEMENT DES APPS ---
with open("apps.json", "r", encoding="utf-8") as f:
    apps = json.load(f)

# --- AFFICHAGE EN GRILLE ---
cols = st.columns(2)
for i, app in enumerate(apps):
    col = cols[i % 2]
    with col:
        st.markdown(f"### {app['name']}")
        st.markdown(app["description"])
        st.link_button("Ouvrir l’application", app["url"])
        st.markdown("---")

# --- SECTION CONTACT ---
st.divider()
st.subheader("📬 Contact & Liens")
st.markdown("""
**Auteur :** Ibrahima Gueye  
**Email :** [ibugueye@gmail.com](mailto:ibugueye@gmail.com)  
**LinkedIn :** [Profil LinkedIn](https://www.linkedin.com/)  
**GitHub :** [Mes projets GitHub](https://github.com/)
""")
