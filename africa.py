import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import requests
import io

# Configuration de la page
st.set_page_config(
    page_title="Carte de l'Afrique - Puissance de la Donnée",
    page_icon="🌍",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
<style>
    .africa-header {
        background: linear-gradient(90deg, #2E8B57, #004aad);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #004aad;
        margin: 10px 0;
    }
    .country-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
        border-left: 4px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="africa-header">
    <h1>🌍 Carte Interactive de l'Afrique</h1>
    <h3>« L'Afrique, puissance de la donnée »</h3>
    <p>Explorez le continent africain et ses opportunités en data science</p>
</div>
""", unsafe_allow_html=True)

# Données des pays africains (exemple simplifié)
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

df = pd.DataFrame(africa_data)

# Navigation
st.sidebar.title("🌍 Navigation Afrique")
page = st.sidebar.radio("Choisir la vue:", 
                       ["Carte Interactive", "Données Économiques", "Opportunités Tech", "Pays Phares"])

# Page 1: Carte Interactive
if page == "Carte Interactive":
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🗺️ Carte 3D de l'Afrique")
        
        # Carte PyDeck 3D
        layer = pdk.Layer(
            'ScatterplotLayer',
            df,
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
        total_population = df['Population (millions)'].sum()
        total_gdp = df['PIB (milliards $)'].sum()
        avg_growth = df['Croissance PIB (%)'].mean()
        avg_internet = df['Taux de pénétration internet (%)'].mean()
        
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

# Page 2: Données Économiques
elif page == "Données Économiques":
    
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
    fig = px.scatter(df, 
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
    st.dataframe(df, use_container_width=True)

# Page 3: Opportunités Tech
elif page == "Opportunités Tech":
    
    st.subheader("🚀 Opportunités Technologiques en Afrique")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📱 FinTech & Mobile Money</h4>
            <p><strong>Leader mondial:</strong> M-Pesa (Kenya)</p>
            <p><strong>Croissance:</strong> +15% par an</p>
            <p><strong>Opportunités:</strong> Blockchain, paiements digitaux</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🏥 HealthTech</h4>
            <p><strong>Enjeu:</strong> Accès aux soins</p>
            <p><strong>Solutions:</strong> Télémédecine, drones médicaux</p>
            <p><strong>Exemple:</strong> Zipline (Rwanda)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>🌾 AgriTech</h4>
            <p><strong>Potentiel:</strong> 60% des terres arables</p>
            <p><strong>Solutions:</strong> Capteurs IoT, analyse sol</p>
            <p><strong>Impact:</strong> Sécurité alimentaire</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>🎓 EdTech</h4>
            <p><strong>Défi:</strong> Éducation accessible</p>
            <p><strong>Solutions:</strong> Plateformes e-learning</p>
            <p><strong>Marché:</strong> 450M jeunes</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>⚡ CleanTech</h4>
            <p><strong>Opportunité:</strong> Énergie solaire</p>
            <p><strong>Potentiel:</strong> 40% du potentiel mondial</p>
            <p><strong>Exemple:</strong> M-Kopa (Kenya)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Data Science</h4>
            <p><strong>Besoin:</strong> Analytics local</p>
            <p><strong>Opportunités:</strong> ML, NLP africain</p>
            <p><strong>Impact:</strong> Décisions data-driven</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Carte des hubs tech
    st.subheader("📍 Hubs Technologiques Africains")
    
    tech_hubs = {
        'Ville': ['Lagos', 'Nairobi', 'Le Cap', 'Kigali', 'Accra', 'Abidjan', 'Cairo', 'Tunis'],
        'Pays': ['Nigeria', 'Kenya', 'Afrique du Sud', 'Rwanda', 'Ghana', 'Côte d\'Ivoire', 'Égypte', 'Tunisie'],
        'Type': ['FinTech', 'AI & Blockchain', 'E-commerce', 'GovTech', 'Mobile', 'Startup', 'DeepTech', 'Digital'],
        'Nombre de startups': [800, 500, 450, 100, 300, 200, 600, 150],
        'Latitude': [6.5244, -1.2921, -33.9249, -1.9441, 5.6037, 5.3599, 30.0444, 36.8065],
        'Longitude': [3.3792, 36.8219, 18.4241, 30.0619, -0.1870, -4.0083, 31.2357, 10.1815]
    }
    
    hubs_df = pd.DataFrame(tech_hubs)
    
    fig = px.scatter_mapbox(hubs_df, 
                           lat="Latitude", 
                           lon="Longitude", 
                           hover_name="Ville",
                           hover_data=["Pays", "Type", "Nombre de startups"],
                           color="Type",
                           size="Nombre de startups",
                           zoom=3,
                           height=500,
                           title="Carte des Hubs Technologiques Africains")
    
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)

# Page 4: Pays Phares
elif page == "Pays Phares":
    
    st.subheader("🏆 Pays Phares du Numérique en Afrique")
    
    # Sélection du pays
    selected_country = st.selectbox("Choisir un pays:", df['Pays'].unique())
    
    country_data = df[df['Pays'] == selected_country].iloc[0]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="country-card">
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
            country_data['Population (millions)'] / df['Population (millions)'].max() * 100,
            country_data['PIB (milliards $)'] / df['PIB (milliards $)'].max() * 100,
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

# Footer avec appel à l'action
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🧠 Intelligence Africaine**")
    st.markdown("Développement de solutions IA adaptées au contexte local")

with col2:
    st.markdown("**📊 Data Science**")
    st.markdown("Formation et mise en œuvre de projets data-driven")

with col3:
    st.markdown("**🌍 Impact Continental**")
    st.markdown("Transformation numérique pour le développement")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "🌍 « L'Afrique, puissance de la donnée » | "
    "🧠 « L'intelligence au service de la performance » | "
    "© 2024 - Construit avec Streamlit"
    "</div>", 
    unsafe_allow_html=True
)