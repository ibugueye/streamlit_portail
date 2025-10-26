import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import base64

# Configuration de la page
st.set_page_config(
    page_title="Générateur de Logo Professionnel",
    page_icon="🎨",
    layout="centered"
)

def create_logo(primary_color, secondary_color, logo_style, include_emoji=True):
    """Crée un logo personnalisé avec les couleurs et style choisis"""
    
    # Dimensions de l'image
    width, height = 600, 400
    
    # Créer une nouvelle image avec fond transparent ou dégradé
    if logo_style == "gradient":
        # Créer un dégradé
        image = Image.new('RGB', (width, height), color=primary_color)
        draw = ImageDraw.Draw(image)
        
        # Dessiner un dégradé simple
        for i in range(height):
            ratio = i / height
            r = int(int(primary_color[1:3], 16) * (1 - ratio) + int(secondary_color[1:3], 16) * ratio)
            g = int(int(primary_color[3:5], 16) * (1 - ratio) + int(secondary_color[3:5], 16) * ratio)
            b = int(int(primary_color[5:7], 16) * (1 - ratio) + int(secondary_color[5:7], 16) * ratio)
            draw.line([(0, i), (width, i)], fill=(r, g, b))
    else:
        # Fond uni
        image = Image.new('RGB', (width, height), color=primary_color)
        draw = ImageDraw.Draw(image)
    
    # Ajouter des éléments décoratifs
    if logo_style == "modern":
        # Cercles concentriques
        draw.ellipse([50, 50, 200, 200], outline=secondary_color, width=5)
        draw.ellipse([70, 70, 180, 180], outline=secondary_color, width=3)
    elif logo_style == "corporate":
        # Lignes géométriques
        draw.rectangle([50, 150, 550, 170], fill=secondary_color)
        draw.polygon([(300, 50), (250, 150), (350, 150)], fill=secondary_color)
    
    # Essayer de charger une police, sinon utiliser une police par défaut
    try:
        # Essayer différentes polices selon le système
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 28)
            subtitle_font = ImageFont.truetype("arial.ttf", 20)
        except:
            try:
                title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
                subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            except:
                # Police par défaut si les autres ne sont pas disponibles
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Couleur du texte (blanc ou noir selon la luminosité du fond)
    def get_text_color(bg_color):
        r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return "white" if luminance < 0.6 else "black"
    
    text_color = get_text_color(primary_color)
    
    # Ajouter les emojis si demandé
    if include_emoji:
        # Positionner les emojis
        emoji_size = 40
        # Cerveau en haut
        draw.text((width//2 - 15, 60), "🧠", fill=text_color, font=title_font)
        # Terre en bas
        draw.text((width//2 - 15, height - 120), "🌍", fill=text_color, font=title_font)
    
    # Ajouter le texte principal
    main_text = "L'intelligence au service de la performance"
    # Calculer la position pour centrer le texte
    bbox = draw.textbbox((0, 0), main_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    
    draw.text((text_x, height//2 - 30), main_text, fill=text_color, font=title_font)
    
    # Ajouter le sous-titre
    subtitle = "L'Afrique, puissance de la donnée"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sub_width = bbox_sub[2] - bbox_sub[0]
    sub_x = (width - sub_width) // 2
    
    draw.text((sub_x, height//2 + 20), subtitle, fill=text_color, font=subtitle_font)
    
    # Ajouter une bordure
    draw.rectangle([10, 10, width-10, height-10], outline=secondary_color, width=3)
    
    return image

def image_to_base64(image):
    """Convertit une image PIL en base64 pour l'affichage Streamlit"""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def get_image_download_link(img, filename="logo_afrique_intelligence.png"):
    """Génère un lien de téléchargement pour l'image"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}" style="background-color:#4CAF50; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block;">📥 Télécharger le Logo</a>'
    return href

# Interface Streamlit
st.title("🎨 Générateur de Logo Professionnel")
st.markdown("Créez votre logo **« L'intelligence au service de la performance »** avec **« L'Afrique, puissance de la donnée »**")

# Sidebar pour les paramètres
st.sidebar.header("⚙️ Paramètres du Logo")

# Sélection des couleurs
col1, col2 = st.sidebar.columns(2)
with col1:
    primary_color = st.color_picker("Couleur principale", "#004aad")
with col2:
    secondary_color = st.color_picker("Couleur secondaire", "#FFD43B")

# Style du logo
logo_style = st.sidebar.selectbox(
    "Style du logo",
    ["modern", "corporate", "gradient", "simple"],
    format_func=lambda x: {
        "modern": "Moderne",
        "corporate": "Corporate", 
        "gradient": "Dégradé",
        "simple": "Simple"
    }[x]
)

# Options supplémentaires
include_emoji = st.sidebar.checkbox("Inclure les emojis 🧠🌍", value=True)
image_format = st.sidebar.selectbox("Format d'export", ["PNG", "JPEG"])

# Bouton pour générer le logo
if st.sidebar.button("🔄 Générer le Logo"):
    st.session_state.generate_logo = True

# Section principale
if st.session_state.get('generate_logo', False):
    # Créer le logo
    logo_image = create_logo(primary_color, secondary_color, logo_style, include_emoji)
    
    # Afficher le logo
    st.subheader("👁️ Aperçu de votre logo")
    st.image(logo_image, use_column_width=True)
    
    # Options de téléchargement
    st.subheader("📥 Télécharger votre logo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Lien de téléchargement
        st.markdown(get_image_download_link(logo_image), unsafe_allow_html=True)
    
    with col2:
        # Aperçu des tailles
        st.markdown("**Format recommandé :**")
        st.markdown("- PNG 600×400 pixels (web)")
        st.markdown("- PNG 1200×800 pixels (print)")
    
    # Code pour intégration
    with st.expander("🖼️ Code d'intégration HTML"):
        # Convertir en base64 pour l'affichage inline
        img_base64 = image_to_base64(logo_image)
        html_code = f'''
        <img src="data:image/png;base64,{img_base64}" alt="Logo Intelligence Performance Afrique" width="300">
        '''
        st.code(html_code, language='html')
    
    # Variantes du logo
    st.subheader("🎨 Variantes de couleurs")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Variante bleu**")
        variant1 = create_logo("#004aad", "#FFFFFF", "simple", include_emoji)
        st.image(variant1, use_column_width=True)
    
    with col2:
        st.markdown("**Variante vert**")
        variant2 = create_logo("#2E8B57", "#FFD700", "simple", include_emoji)
        st.image(variant2, use_column_width=True)
    
    with col3:
        st.markdown("**Variante orange**")
        variant3 = create_logo("#FF6B35", "#004aad", "simple", include_emoji)
        st.image(variant3, use_column_width=True)

else:
    # Page d'accueil avec instructions
    st.markdown("""
    ## Bienvenue dans le générateur de logo
    
    Ce générateur vous permet de créer un logo professionnel avec vos slogans :
    
    - **🧠 « L'intelligence au service de la performance. »**
    - **🌍 « L'Afrique, puissance de la donnée. »**
    
    ### Instructions :
    1. ⚙️ Utilisez la sidebar pour personnaliser les couleurs et le style
    2. 🎨 Choisissez votre palette de couleurs préférée
    3. 🔄 Cliquez sur "Générer le Logo" pour créer votre design
    4. 📥 Téléchargez le logo final au format PNG
    
    ### Utilisations recommandées :
    - **Site web et applications**
    - **Présentations professionnelles**
    - **Documents marketing**
    - **Signature email**
    - **Réseaux sociaux**
    """)
    
    # Exemple de logo par défaut
    st.subheader("Exemple de logo généré")
    example_logo = create_logo("#004aad", "#FFD43B", "modern", True)
    st.image(example_logo, use_column_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Générateur de Logo Professionnel | Créé avec Streamlit 🚀 et Python 🐍"
    "</div>", 
    unsafe_allow_html=True
)