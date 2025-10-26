import streamlit as st
import json
from pathlib import Path
import os
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go

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
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 40px;">🧠</div>
        <div style="font-size: 16px; font-weight: bold; color: #004aad;">
            L'intelligence au service de la performance
        </div>
        <div style="font-size: 12px; color: #0078ff;">
            🌍 L'Afrique, puissance de la donnée
        </div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["🏠 À propos", "💻 Applications", "🌍 Afrique", "📬 Contact"])

# --- DONNÉES AFRIQUE ---
africa_data = {
    'Pays': ['Nigeria', 'Égypte', 'Afrique du Sud', 'Kenya', 'Ghana', 'Côte d\'Ivoire', 
             'Maroc', 'Éthiopie', 'Tanzanie', 'RDC', 'Algérie', 'Sénégal', 'Tunisie',
             'Ouganda', 'Angola', 'Cameroun', 'Zimbabwe', 'Mali', 'Burkina Faso', 'Rwanda'],
    'Population (millions)': [206, 102, 59, 54, 31, 26, 37, 115, 59, 90, 44, 17, 12, 46, 33, 27, 15, 20, 21, 13],
    'PIB (milliards $)': [448, 303, 351, 95, 67, 58, 119, 96, 62, 49, 169, 24, 43, 37, 105, 39, 21, 17, 16, 10],
    'Croissance PIB (%)': [2.2, 3.6, 0.7, 5.7, 6.3, 7.4, 3.1, 6.1, 6.4, 4.4, 2.1, 5.3, 2.5, 6.5, -1.1, 3.5, 3.4, 5.0, 6.0, 8.0],
    'Taux de pénétration internet (%)': [50, 57, 56, 43, 40, 36, 65, 20, 46, 19, 58, 46, 67, 25, 30, 38, 30, 25, 22, 52],
    'Latitude': [9.0820, 26.8206, -30.5595, -1.2921, 7.9465, 7.5400, 31.7917, 9.1450, -6.3690, -4.0383, 28.0339, 14.4974, 33.8869, 1.3733, -11.2027, 7.3697, -19.0154, 17.5707, 12.2383, -1.9403],
    'Longitude': [8.6753, 30.8025, 22.9375, 36.8219, -1.0232, -5.5471, -7.0926, 40.4897, 34.8888, 21.7587, 1.6596, -14.4524, 9.5375, 32.2903, 17.8739, 12.3547, 29.1549, -3.9962, -1.5616, 29.8739]
}

df_africa = pd.DataFrame(africa_data)

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
            "**Chef de projet** – Conception & Développement d'applications informatiques",ISIC Paris 
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
        - **Power BI, Tableau , Excel avancé, Power Query**
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

# --- PAGE 3 : AFRIQUE ---
elif page == "🌍 Afrique":
    st.markdown(
        """
        <div style='background:linear-gradient(90deg, #2E8B57, #004aad); padding:30px; border-radius:15px; text-align:center; color:white; margin-bottom:30px'>
            <h1>🌍 Carte Interactive de l'Afrique</h1>
            <h3>« L'Afrique, puissance de la donnée »</h3>
            <p>Explorez le continent africain et ses opportunités en data science</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Navigation interne pour la page Afrique
    africa_menu = st.radio("Navigation Afrique", 
                          ["🗺️ Carte Interactive", "📈 Données Économiques", "🚀 Opportunités Tech", "🏆 Pays Phares"], 
                          horizontal=True)
    
    st.markdown("---")

    if africa_menu == "🗺️ Carte Interactive":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("🗺️ Carte 3D de l'Afrique")
            
            # Carte PyDeck 3D
            layer = pdk.Layer(
                'ScatterplotLayer',
                df_africa,
                get_position=['Longitude', 'Latitude'],
                get_color='[200, 30, 0, 160]',
                get_radius=50000,
                pickable=True
            )
            
            view_state = pdk.ViewState(
                latitude=8,
                longitude=20,
                zoom=2,
                pitch=45
            )
            
            r = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={
                    'html': '<b>{Pays}</b><br>Population: {Population (millions)}M<br>PIB: {PIB (milliards $)}B$',
                    'style': {'color': 'white'}
                }
            )
            
            st.pydeck_chart(r)
        
        with col2:
            st.subheader("📊 Indicateurs Clés")
            
            # Métriques principales
            total_population = df_africa['Population (millions)'].sum()
            total_gdp = df_africa['PIB (milliards $)'].sum()
            avg_growth = df_africa['Croissance PIB (%)'].mean()
            avg_internet = df_africa['Taux de pénétration internet (%)'].mean()
            
            st.metric("Population Totale", f"{total_population:.0f}M")
            st.metric("PIB Total", f"{total_gdp:.0f}B$")
            st.metric("Croissance Moyenne", f"{avg_growth:.1f}%")
            st.metric("Internet Moyen", f"{avg_internet:.1f}%")
            
            st.markdown("---")
            st.subheader("🎯 Focus Data Science")
            st.markdown("""
            - **Marché en croissance** rapide
            - **Jeunesse digitale** connectée
            - **Opportunités** en IA et FinTech
            - **Besoin criant** en solutions data
            """)

    elif africa_menu == "📈 Données Économiques":
        st.subheader("📈 Données Économiques Africaines")
        
        # Sélection des indicateurs
        col1, col2, col3 = st.columns(3)
        
        with col1:
            x_axis = st.selectbox("Axe X:", ['Population (millions)', 'PIB (milliards $)', 'Taux de pénétration internet (%)'])
        with col2:
            y_axis = st.selectbox("Axe Y:", ['PIB (milliards $)', 'Croissance PIB (%)', 'Taux de pénétration internet (%)'])
        with col3:
            size_var = st.selectbox("Taille des bulles:", ['Population (millions)', 'PIB (milliards $)', 'Croissance PIB (%)'])
        
        # Graphique interactif
        fig = px.scatter(df_africa, 
                        x=x_axis, 
                        y=y_axis, 
                        size=size_var,
                        color='Croissance PIB (%)',
                        hover_name='Pays',
                        title=f"Relation entre {x_axis} et {y_axis}",
                        color_continuous_scale='Viridis')
        
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        # Tableau de données
        st.subheader("📋 Données Détailées par Pays")
        st.dataframe(df_africa, use_container_width=True)

    elif africa_menu == "🚀 Opportunités Tech":
        st.subheader("🚀 Opportunités Technologiques en Afrique")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>📱 FinTech & Mobile Money</h4>
                <p><strong>Leader mondial:</strong> M-Pesa (Kenya)</p>
                <p><strong>Croissance:</strong> +15% par an</p>
                <p><strong>Opportunités:</strong> Blockchain, paiements digitaux</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>🏥 HealthTech</h4>
                <p><strong>Enjeu:</strong> Accès aux soins</p>
                <p><strong>Solutions:</strong> Télémédecine, drones médicaux</p>
                <p><strong>Exemple:</strong> Zipline (Rwanda)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>🌾 AgriTech</h4>
                <p><strong>Potentiel:</strong> 60% des terres arables</p>
                <p><strong>Solutions:</strong> Capteurs IoT, analyse sol</p>
                <p><strong>Impact:</strong> Sécurité alimentaire</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>🎓 EdTech</h4>
                <p><strong>Défi:</strong> Éducation accessible</p>
                <p><strong>Solutions:</strong> Plateformes e-learning</p>
                <p><strong>Marché:</strong> 450M jeunes</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>⚡ CleanTech</h4>
                <p><strong>Opportunité:</strong> Énergie solaire</p>
                <p><strong>Potentiel:</strong> 40% du potentiel mondial</p>
                <p><strong>Exemple:</strong> M-Kopa (Kenya)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #004aad; margin: 10px 0;'>
                <h4>📊 Data Science</h4>
                <p><strong>Besoin:</strong> Analytics local</p>
                <p><strong>Opportunités:</strong> ML, NLP africain</p>
                <p><strong>Impact:</strong> Décisions data-driven</p>
            </div>
            """, unsafe_allow_html=True)

    elif africa_menu == "🏆 Pays Phares":
        st.subheader("🏆 Pays Phares du Numérique en Afrique")
        
        # Sélection du pays
        selected_country = st.selectbox("Choisir un pays:", df_africa['Pays'].unique())
        
        country_data = df_africa[df_africa['Pays'] == selected_country].iloc[0]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 10px 0; border-left: 4px solid #2E8B57;'>
                <h3>🇺🇳 {selected_country}</h3>
                <p><strong>Population:</strong> {country_data['Population (millions)']} millions</p>
                <p><strong>PIB:</strong> {country_data['PIB (milliards $)']} milliards $</p>
                <p><strong>Croissance:</strong> {country_data['Croissance PIB (%)']}%</p>
                <p><strong>Connectivité:</strong> {country_data['Taux de pénétration internet (%)']}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Graphique radar pour le pays sélectionné
            categories = ['Population', 'PIB', 'Croissance', 'Internet']
            values = [
                country_data['Population (millions)'] / df_africa['Population (millions)'].max() * 100,
                country_data['PIB (milliards $)'] / df_africa['PIB (milliards $)'].max() * 100,
                country_data['Croissance PIB (%)'],
                country_data['Taux de pénétration internet (%)']
            ]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=selected_country
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False,
                title=f"Profil Numérique - {selected_country}"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🌟 Points Forts")
            
            # Déterminer les points forts basés sur les données
            strengths = []
            if country_data['Croissance PIB (%)'] > 5:
                strengths.append("📈 Croissance économique rapide")
            if country_data['Taux de pénétration internet (%)'] > 50:
                strengths.append("🌐 Population bien connectée")
            if country_data['PIB (milliards $)'] > 100:
                strengths.append("💰 Économie importante")
            if country_data['Population (millions)'] > 50:
                strengths.append("👥 Grand marché domestique")
            
            for strength in strengths:
                st.markdown(f"- {strength}")
            
            st.markdown("---")
            st.subheader("💡 Opportunités Data")
            st.markdown("""
            - Analyse de données locales
            - Solutions adaptées au contexte
            - Formation aux métiers du numérique
            - Partenariats internationaux
            """)

# --- PAGE 4 : CONTACT ---
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
    - Stratégie Afrique
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
