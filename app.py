import streamlit as st
import json
from pathlib import Path
import os
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
import feedparser
from datetime import datetime
import requests

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

# --- FONCTIONS POUR MEDIUM ---
def get_medium_articles(username="ibrahimagueye", max_articles=10):
    """Récupère les articles Medium d'un utilisateur"""
    try:
        # URL du flux RSS Medium
        url = f"https://medium.com/feed/@ibugueye"
        
        # Parser le flux RSS
        feed = feedparser.parse(url)
        
        articles = []
        for entry in feed.entries[:max_articles]:
            # Extraire l'image de l'article
            image_url = None
            if 'content' in entry and len(entry.content) > 0:
                # Chercher une image dans le contenu
                import re
                img_match = re.search(r'<img[^>]+src="([^">]+)"', entry.content[0].value)
                if img_match:
                    image_url = img_match.group(1)
            
            # Formater la date
            published = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else None
            
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': published,
                'summary': entry.summary if hasattr(entry, 'summary') else '',
                'image': image_url,
                'author': entry.author if hasattr(entry, 'author') else username
            })
        
        return articles
    except Exception as e:
        st.error(f"Erreur lors de la récupération des articles Medium: {e}")
        return []

def display_medium_articles(articles):
    """Affiche les articles Medium dans un format attrayant"""
    if not articles:
        st.info("📝 Aucun article trouvé. Mes prochaines publications arrivent bientôt!")
        return
    
    for i, article in enumerate(articles):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(article['title'])
            
            # Date de publication
            if article['published']:
                st.caption(f"📅 Publié le {article['published'].strftime('%d/%m/%Y')}")
            
            # Résumé
            if article['summary']:
                # Nettoyer le résumé (enlever le HTML)
                import re
                clean_summary = re.sub('<[^<]+?>', '', article['summary'])
                clean_summary = clean_summary[:200] + "..." if len(clean_summary) > 200 else clean_summary
                st.write(clean_summary)
            
            # Bouton de lecture
            st.markdown(f"""
            <a href="{article['link']}" target="_blank">
                <button style="
                    background-color: #00ab6c; 
                    color: white; 
                    border: none; 
                    border-radius: 5px; 
                    padding: 10px 20px; 
                    cursor: pointer;
                    margin-top: 10px;
                ">📖 Lire l'article</button>
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            # Image de l'article
            if article['image']:
                st.image(article['image'], use_container_width=True)
            else:
                # Image par défaut
                st.image("https://miro.medium.com/v2/resize:fit:1400/1*psYl0y9DUzZWtHzFJLIvTw.png", 
                        use_container_width=True, 
                        caption="Article Medium")
        
        if i < len(articles) - 1:
            st.markdown("---")

# --- MENU LATÉRAL ---
# Gestion sécurisée du logo
try:
    st.sidebar.image("assets/logo.png", use_container_width==True)
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
page = st.sidebar.radio("Aller à :", ["🏠 À propos", "💻 Applications","📝 Publications", "🌍 Afrique",  "📬 Contact"])

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
            "**Data Scientist** – OpenClassrooms / Centrale Supélec",
            "**Data Analyst & Data Scientist** - OpenClassrooms / l’ENSAE - ENSAI",
            "**Master Réseaux et Télécommunications (VAE) - UPMC**",
            "**Formation Administration Réseaux** – UPMC",
            "**Architecte infrastructure Réseaux et Systèmes** - CNAM Paris ,
            "**Micro-réseaux Maintenance informatique, sécurité réseau, hotline** – GRETA de Paris ",
            "**Chef de projet**– Conception & Développement d'applications informatiques - ESIC " ,
            "**DUT Gestion**" - Iut Paris-sud De Sceaux,
            "**BTS Comptabilité**" - Top Formation  ENC , 
            "**Comptabilité A, B1, B2** – CNAM Paris",
            "**Cours de mathématiques** – CNAM Paris ",
            "**Contrôle de gestion** – École des Cadres",
       
         
            
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

# --- PAGE 4 : PUBLICATIONS MEDIUM ---
elif page == "📝 Publications":
    st.markdown(
        """
        <div style='background:linear-gradient(90deg, #00ab6c, #0078ff); padding:30px; border-radius:10px; text-align:center; color:white; margin-bottom:30px'>
            <h1>📝 Mes Publications Medium</h1>
            <h3>Partage de connaissances en Data Science, IA et Innovation Africaine</h3>
            <p>Découvrez mes articles sur la data science, l'IA et le développement technologique en Afrique</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Configuration pour les articles Medium
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📚 Dernières Publications")
        
        # Indicateur de chargement
        with st.spinner("Chargement des articles Medium..."):
            # Récupérer les articles Medium
            articles = get_medium_articles("ibrahimagueye", 10)  # Remplacez par votre username Medium
            
            # Afficher les articles
            display_medium_articles(articles)
    
    with col2:
        st.subheader("🔍 Filtres")
        
        # Filtres optionnels
        st.selectbox("Trier par:", ["Plus récents", "Plus populaires", "Plus lus"])
        st.multiselect("Catégories:", ["Data Science", "IA", "Afrique Tech", "Business", "Tutoriels"])
        
        st.markdown("---")
        st.subheader("📈 Statistiques")
        
        # Statistiques fictives (à adapter avec vos vraies stats)
        st.metric("Articles publiés", len(articles))
        st.metric("Lectures totales", "5K+")
        st.metric("Followers", "500+")
        
        st.markdown("---")
        st.subheader("💡 Sujets abordés")
        st.markdown("""
        - 🤖 Intelligence Artificielle
        - 📊 Data Science
        - 🌍 Tech Africaine
        - 💼 Business Intelligence
        - 🎓 Tutoriels pratiques
        - 🚀 Innovation
        """)
    
    # Section d'appel à l'action
    st.markdown("---")
    st.subheader("🎯 Rejoignez-moi sur Medium")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: #f0f2f6; border-radius: 10px;'>
            <h3>📖 Lire</h3>
            <p>Découvrez mes analyses sur la data et l'innovation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: #f0f2f6; border-radius: 10px;'>
            <h3>👥 Suivre</h3>
            <p>Restez informé de mes nouvelles publications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: #f0f2f6; border-radius: 10px;'>
            <h3>💬 Interagir</h3>
            <p>Commentez et partagez vos retours</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Lien vers le profil Medium
    st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <a href="https://medium.com/@ibugueye" target="_blank">
            <button style='
                background-color: #00ab6c; 
                color: white; 
                border: none; 
                border-radius: 25px; 
                padding: 15px 30px; 
                font-size: 18px;
                cursor: pointer;
                margin: 10px;
            '>📝 Voir mon profil Medium complet</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 5 : CONTACT ---
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
        **📝 Medium :** [medium.com/@ibugueye](https://medium.com/@ibugueye)  
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
        - Rédaction Technique
        - Stratégie Afrique
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
    - **📝 Rédaction & partage** : transmission de connaissances via Medium
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
    **LinkedIn:** [Ibugueye](https://linkedin.com/in/ibucoumba/)  
    **GitHub:** [ibugueye](https://github.com/ibugueye?tab=repositories)
    **Medium:** [ ibugueye](https://medium.com/@ibugueye)
    """)
    
    st.header("🎯 Expertises")
    st.markdown("""
    - Data Science & Analyse
    - Contrôle de Gestion
    - Réseaux & Télécoms
    - Développement d'Apps
    - Formation & Pédagogie
    - Rédaction Technique
    - Stratégie Afrique
    """)
    
    # Indicateur de statut PDF
    st.markdown("---")
    if pdf_data:
        st.success("✅ Portfolio disponible")
    else:
        st.warning("📄 Portfolio en cours")
    
    # Dernières publications dans la sidebar
    st.markdown("---")
    st.header("📝 Dernier Article")
    try:
        articles = get_medium_articles("ibrahimagueye", 1)
        if articles:
            article = articles[0]
            st.write(f"**{article['title']}**")
            if article['published']:
                st.caption(f"Publié le {article['published'].strftime('%d/%m/%Y')}")
            st.markdown(f"[Lire l'article →]({article['link']})")
    except:
        st.info("Chargement des articles...")
    
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
