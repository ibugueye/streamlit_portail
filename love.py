# app_amiharbi_author.py
# 🧠❤️ Amiharbi Eyeug – Love & Machine Learning
# Streamlit one-file app with navigation, visuals gallery, and PDF embeds
# How to use:
#   1) Put your PDFs in ./assets/ with exact names:
#        - Love_and_Machine_Learning_Amiharbi_Eyeug_A4.pdf
#        - Love_and_Machine_Learning_Amiharbi_Eyeug_A5.pdf
#   2) Put your 8 JPG images in ./assets/images/ (any names). The app will auto-load them.
#   3) Run:  streamlit run app_amiharbi_author.py

from pathlib import Path
from io import BytesIO
import base64
import textwrap

import streamlit as st

# ----------------------------- CONFIG ------------------------------------ #
st.set_page_config(
    page_title="Amiharbi Eyeug – Love & Machine Learning",
    page_icon="💙",
    layout="wide",
)

PRIMARY = "#0c1b3c"      # bleu nuit
GOLD = "#cfae60"          # doré doux
ROSE = "#d9b8c8"          # rose poudré (touches)
MUTED = "#0f214b"         # bleu plus clair
BG = "#08142f"            # fond général
TEXT = "#f5f7fb"          # texte clair

ASSETS_DIR = Path("assets")
IMAGES_DIR = ASSETS_DIR / "images"
PDF_A4 = ASSETS_DIR / "Love_and_Machine_Learning_Amiharbi_Eyeug_A4.pdf"
PDF_A5 = ASSETS_DIR / "Love_and_Machine_Learning_Amiharbi_Eyeug_A5.pdf"

# ----------------------------- STYLE ------------------------------------- #
CUSTOM_CSS = f"""
<style>
  .stApp {{ background:{BG}; color:{TEXT}; }}
  h1, h2, h3, h4, h5, h6 {{ color:{GOLD}; }}
  .amhi-hero {{
     padding: 40px 28px; border-radius: 24px; 
     background: radial-gradient(1200px 500px at 15% -10%, #132859 5%, transparent 60%),
                 radial-gradient(900px 600px at 95% 0%, #1a2f66 5%, transparent 55%),
                 linear-gradient(180deg, {PRIMARY} 0%, {BG} 65%);
     border: 1px solid rgba(207,174,96,.25);
     box-shadow: 0 10px 40px rgba(0,0,0,.35), inset 0 0 0 1px rgba(255,255,255,.03);
  }}
  .amhi-sub {{ color:#d9e2ff; opacity:.9; font-size:1.08rem; }}
  .amhi-chip {{
     display:inline-block; padding:.3rem .7rem; margin:.25rem; border-radius:999px;
     background:rgba(207,174,96,.12); color:{GOLD}; border:1px solid rgba(207,174,96,.35);
     font-size:.85rem;
  }}
  .amhi-card {{
     background:linear-gradient(180deg, rgba(255,255,255,.02), rgba(255,255,255,.00));
     border:1px solid rgba(207,174,96,.22); border-radius:20px; padding:20px; height:100%;
  }}
  .amhi-footer {{ opacity:.7; font-size:.9rem; }}
  .amhi-divider {{ height:1px; background:linear-gradient(90deg, transparent, rgba(207,174,96,.35), transparent); margin:12px 0 20px; }}
  .amhi-band {{
     width:100%; padding:8px 14px; text-align:center; border-radius:999px; 
     background:rgba(207,174,96,.15); color:{GOLD}; border:1px solid rgba(207,174,96,.35);
  }}
  .pdf-embed {{ border:1px solid rgba(207,174,96,.28); border-radius:16px; overflow:hidden; }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ----------------------------- HELPERS ----------------------------------- #
def file_to_bytes(path: Path) -> bytes:
    return path.read_bytes()


def pdf_embed_html(pdf_path: Path, height: int = 800) -> str:
    """Return an <iframe> embedding a local PDF with base64 data URI."""
    try:
        data = base64.b64encode(file_to_bytes(pdf_path)).decode("utf-8")
        return f'<iframe class="pdf-embed" src="data:application/pdf;base64,{data}" width="100%" height="{height}"></iframe>'
    except Exception as e:
        return f"<div class='amhi-card'>Impossible d'afficher le PDF : {e}</div>"


def list_images(dir_path: Path):
    if not dir_path.exists():
        return []
    exts = {".jpg", ".jpeg", ".png", ".webp"}
    return sorted([p for p in dir_path.iterdir() if p.suffix.lower() in exts])

# ----------------------------- HEADER ------------------------------------ #
with st.container():
    st.markdown(
        """
        <div class='amhi-hero'>
          <h1>LOVE & MACHINE LEARNING</h1>
          <div class='amhi-sub'>L’art de séduire à l’ère des algorithmes · Quand les algorithmes apprennent à aimer</div>
          <div style='height:10px'></div>
          <div class='amhi-band'>Par <b>Amiharbi Eyeug</b> – Là où la science rencontre la poésie</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------- NAVIGATION -------------------------------- #
# Compact top navigation via tabs (stable across Streamlit versions)
TABS = st.tabs(["🏠 Accueil", "📘 Œuvre", "🖼️ Galerie", "🪶 À propos", "✉️ Contact"])

# ----------------------------- CONTENT: HOME ----------------------------- #
with TABS[0]:
    st.write("")
    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.markdown(
            f"""
            ### Bienvenue
            *Et si aimer, c’était comme entraîner un algorithme ?* Observer, apprendre, ajuster… recommencer. 
            Ce projet tisse un lien entre **data science** et **poésie** pour célébrer la part imprévisible du cœur humain.

            <div class='amhi-divider'></div>
            **Ce que vous trouverez ici**
            - Le texte **complet** _Love & Machine Learning_ (version écran et mobile)
            - Une **galerie visuelle** en bleu & doré
            - Une **philosophie** : quand la technique devient poétique
            - Un **espace de contact** pour vos lectures & collaborations
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
        <span class='amhi-chip'>Poésie</span>
        <span class='amhi-chip'>IA</span>
        <span class='amhi-chip'>Machine Learning</span>
        <span class='amhi-chip'>Humanité</span>
        <span class='amhi-chip'>Esthétique</span>
        """, unsafe_allow_html=True)

    with col2:
        # Drop zone for quick-adding images
        st.markdown("**Ajouter rapidement des visuels (optionnel)**")
        uploaded = st.file_uploader("Glissez-déposez vos JPG/PNG (ils seront affichés dans la Galerie)", type=["jpg","jpeg","png","webp"], accept_multiple_files=True)
        if uploaded:
            IMAGES_DIR.mkdir(parents=True, exist_ok=True)
            for up in uploaded:
                out = IMAGES_DIR / up.name
                out.write_bytes(up.getvalue())
            st.success(f"{len(uploaded)} image(s) ajoutée(s) dans assets/images/")

# ----------------------------- CONTENT: WORK ----------------------------- #
with TABS[1]:
    st.subheader("Texte complet & versions PDF")
    left, right = st.columns([1.15, 1])

    with left:
        st.markdown(
            textwrap.dedent(
                f"""
                #### Extrait d'ouverture
                *« Entre données et désirs, il existe une équation que même l’intelligence artificielle ne peut résoudre : celle du cœur. »*

                ##### Introduction
                Il y a un an, alors que je potassais des modèles de *deep learning*, une idée m’a traversé l’esprit : 
                **Et si courtiser ma future épouse relevait aussi de l’apprentissage automatique ?**
                Après tout, les relations humaines reposent sur l’observation, l’adaptation et l’optimisation — trois piliers chers aux data scientists.

                ##### Plan en 5 mouvements
                1. **Apprentissage supervisé** — écouter les retours, ajuster les gestes
                2. **Apprentissage non supervisé** — découvrir sans étiquettes
                3. **Apprentissage par renforcement** — essayer, échouer, réessayer
                4. **Apprentissage semi-supervisé** — équilibre entre raison et intuition
                5. **Apprentissage par transfert** — s’inspirer sans copier

                **Le biais à éviter :** le surapprentissage (routine)
                
                **La métrique ultime :** la complicité (son bonheur & le vôtre)
                """
            )
        )

        # Inline PDF viewers (if present)
        if PDF_A4.exists():
            st.markdown("###### Version lecture (A4)")
            st.markdown(pdf_embed_html(PDF_A4, height=700), unsafe_allow_html=True)
            st.download_button("⬇️ Télécharger le PDF A4", data=PDF_A4.read_bytes(), file_name=PDF_A4.name)
        else:
            st.info("Placez votre fichier **A4** dans `assets/` pour activer l'aperçu et le téléchargement.")

        if PDF_A5.exists():
            st.markdown("###### Version mobile (A5)")
            st.markdown(pdf_embed_html(PDF_A5, height=700), unsafe_allow_html=True)
            st.download_button("⬇️ Télécharger le PDF A5", data=PDF_A5.read_bytes(), file_name=PDF_A5.name)
        else:
            st.info("Placez votre fichier **A5** dans `assets/` pour activer l'aperçu et le téléchargement.")

    with right:
        st.markdown("""
        ##### Philosophie de l'œuvre
        > *Je crois que la poésie et la data sont deux langages qui cherchent la même chose : comprendre l’invisible.*

        Cette œuvre propose un pont esthétique entre **science** et **humanité**, une écriture qui fait dialoguer **algorithmes** et **émotions**.
        """)
        st.markdown("<div class='amhi-divider'></div>", unsafe_allow_html=True)
        st.markdown("""
        ##### Détails 
        • Palette : bleu nuit & doré  
        • Typographies : Lora & Playfair Display  
        • Signature : *Amiharbi Eyeug*  
        """)

# ----------------------------- CONTENT: GALLERY -------------------------- #
with TABS[2]:
    st.subheader("Galerie visuelle – Pack officiel (8 visuels)")

    imgs = list_images(IMAGES_DIR)
    if not imgs:
        st.info("Ajoutez vos images dans `assets/images/` (JPG/PNG). Elles s’afficheront ici automatiquement.")
    else:
        # Display images in a neat grid
        ncol = 3
        rows = [imgs[i:i+ncol] for i in range(0, len(imgs), ncol)]
        for row in rows:
            cols = st.columns(ncol)
            for c, img_path in zip(cols, row):
                with c:
                    st.image(str(img_path), use_column_width=True)
                    st.caption(img_path.name)

# ----------------------------- CONTENT: ABOUT ---------------------------- #
with TABS[3]:
    st.subheader("À propos d’Amiharbi Eyeug")
    st.markdown(
        textwrap.dedent(
            """
            *Amiharbi Eyeug est un auteur et explorateur des liens entre data science, philosophie et poésie.*  
            À travers ses écrits, il cherche à **rendre la technologie plus poétique** — et la **poésie, plus rationnelle**.  
            Il publie des œuvres où **algorithmes** et **émotions** apprennent à parler le même langage.
            """
        )
    )
    st.markdown("<div class='amhi-divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    **Thèmes récurrents**  
    — Intelligence artificielle humaine  
    — Beauté de l’imprévisible  
    — Dialogue entre logique et tendresse
    """)

# ----------------------------- CONTENT: CONTACT -------------------------- #
with TABS[4]:
    st.subheader("Entrer en contact")
    with st.form("contact_form", clear_on_submit=True):
        colA, colB = st.columns(2)
        with colA:
            name = st.text_input("Amiharbi Eyeug")
            email = st.text_input("ibugueye@ngorweb.com")
        with colB:
            topic = st.selectbox("Sujet", ["Lecture", "Collaboration", "Invitations & Conférences", "Autre"])
            opt_copy = st.checkbox("Recevoir une copie de mon message")
        message = st.text_area("Votre message", height=160)
        sent = st.form_submit_button("Envoyer ✉️")
    if sent:
        # Note: This demo doesn't actually send email. Hook up with an API if needed.
        st.success("Merci ! Votre message a été enregistré localement (démo). Connectez un service d'email pour l'envoi réel.")
        # Optionally write to a local file (for demo)
        (Path("inbox").mkdir(exist_ok=True))
        idx = len(list(Path("inbox").glob("message_*.txt"))) + 1
        (Path("inbox")/f"message_{idx:03d}.txt").write_text(
            f"From: {name} <{email}>\nSujet: {topic}\nCopy: {opt_copy}\n\n{message}", encoding="utf-8"
        )

# ----------------------------- FOOTER ----------------------------------- #
st.markdown("""
<div class='amhi-divider'></div>
<div class='amhi-footer'>© Amiharbi Eyeug · Love & Machine Learning · Design bleu & doré · Streamlit</div>
""", unsafe_allow_html=True)
