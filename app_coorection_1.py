 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from scipy import stats
import sympy as sp

# Configuration de la page
st.set_page_config(
    page_title="📚 Théories IA & Data Science - Documentation Complète",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .theory-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
    }
    .math-section {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 15px 0;
    }
    .algorithm-card {
        background: #e3f2fd;
        border: 1px solid #2196f3;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .deep-learning {
        background: #f3e5f5;
        border: 1px solid #9c27b0;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .statistical-theory {
        background: #e8f5e8;
        border: 1px solid #4caf50;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .implementation {
        background: #fff3cd;
        border: 1px solid #ffc107;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<div class="theory-header"><h1>🧠 Théories IA & Data Science - Documentation Complète</h1></div>', unsafe_allow_html=True)
    
    # Navigation principale
    section = st.sidebar.selectbox(
        "**📖 Domaines Théoriques**",
        [
            "🎯 Fondements Mathématiques",
            "📊 Apprentissage Statistique",
            "🌳 Machine Learning Classique", 
            "🧠 Deep Learning Théorique",
            "⚙️ Optimisation & Apprentissage",
            "📈 Validation & Évaluation",
            "🔄 Apprentissage par Renforcement",
            "🔍 NLP & Traitement du Langage",
            "👁️ Computer Vision Théorique",
            "🏗️ MLOps & Ingénierie"
        ]
    )
    
    if section == "🎯 Fondements Mathématiques":
        fondements_mathematiques()
    elif section == "📊 Apprentissage Statistique":
        apprentissage_statistique()
    elif section == "🌳 Machine Learning Classique":
        ml_classique()
    elif section == "🧠 Deep Learning Théorique":
        deep_learning_theorique()
    elif section == "⚙️ Optimisation & Apprentissage":
        optimisation_apprentissage()
    elif section == "📈 Validation & Évaluation":
        validation_evaluation()
    elif section == "🔄 Apprentissage par Renforcement":
        reinforcement_learning()
    elif section == "🔍 NLP & Traitement du Langage":
        nlp_theorie()
    elif section == "👁️ Computer Vision Théorique":
        computer_vision()
    elif section == "🏗️ MLOps & Ingénierie":
        mlops_engineering()

# =============================================================================
# FONDEMENTS MATHÉMATIQUES
# =============================================================================

def fondements_mathematiques():
    st.header("🎯 Fondements Mathématiques de l'IA")
    
    st.markdown("""
    ## 📐 Algèbre Linéaire pour le Machine Learning
    
    ### Espaces Vectoriels et Transformations
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Produit Scalaire et Normes
        """)
        st.latex(r"""
        \langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^n x_i y_i
        """)
        st.latex(r"""
        \|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}
        """)
        st.latex(r"""
        \|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i|
        """)
        
        st.markdown("""
        #### Décomposition Matricielle
        """)
        st.latex(r"""
        A = U \Sigma V^T \quad \text{(SVD)}
        """)
        st.latex(r"""
        A = Q \Lambda Q^T \quad \text{(Diagonalisation)}
        """)
    
    with col2:
        st.markdown("""
        #### Valeurs Propres et Vecteurs Propres
        """)
        st.latex(r"""
        A\mathbf{v} = \lambda \mathbf{v}
        """)
        
        st.markdown("""
        **Applications en ML:**
        - PCA: Réduction dimensionnalité
        - PageRank: Analyse de réseaux
        - Clustering spectral
        """)
        
        st.markdown("""
        #### Produit de Matrices
        """)
        st.latex(r"""
        (AB)_{ij} = \sum_{k=1}^n A_{ik} B_{kj}
        """)
    
    st.markdown("""
    ## 📊 Calcul Différentiel et Optimisation
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Gradient et Dérivées
        """)
        st.latex(r"""
        \nabla f(\mathbf{x}) = \left[\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right]^T
        """)
        
        st.markdown("""
        #### Règle de Chaîne
        """)
        st.latex(r"""
        \frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}
        """)
        
        st.markdown("""
        #### Dérivée d'une Fonction Composition
        """)
        st.latex(r"""
        \nabla(f \circ g)(x) = \nabla f(g(x)) \cdot J_g(x)
        """)
    
    with col2:
        st.markdown("""
        #### Hessienne
        """)
        st.latex(r"""
        H(f)_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
        """)
        
        st.markdown("""
        #### Condition d'Optimalité
        """)
        st.latex(r"""
        \nabla f(\mathbf{x}^*) = 0 \quad \text{et} \quad H(f)(\mathbf{x}^*) \succeq 0
        """)
        
        st.markdown("""
        #### Formule de Taylor
        """)
        st.latex(r"""
        f(\mathbf{x} + \Delta\mathbf{x}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^T \Delta\mathbf{x} + \frac{1}{2} \Delta\mathbf{x}^T H(f)(\mathbf{x}) \Delta\mathbf{x}
        """)
    
    st.markdown("""
    ## 📈 Probabilités et Statistiques
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### Distributions Fondamentales
        """)
        st.latex(r"""
        P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}
        """)
        st.latex(r"""
        f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
        """)
    
    with col2:
        st.markdown("""
        #### Théorème de Bayes
        """)
        st.latex(r"""
        P(A|B) = \frac{P(B|A)P(A)}{P(B)}
        """)
        
        st.markdown("""
        #### Espérance et Variance
        """)
        st.latex(r"""
        \mathbb{E}[X] = \sum x_i P(X=x_i)
        """)
        st.latex(r"""
        \text{Var}(X) = \mathbb{E}[(X - \mu)^2]
        """)
    
    with col3:
        st.markdown("""
        #### Lois des Grands Nombres
        """)
        st.latex(r"""
        \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p} \mathbb{E}[X]
        """)
        
        st.markdown("""
        #### Théorème Central Limite
        """)
        st.latex(r"""
        \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)
        """)
    
    # Visualisation interactive des concepts
    st.markdown("## 🎨 Visualisations Interactives")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Fonction d'Activation Sigmoid")
        x = np.linspace(-10, 10, 100)
        y = 1 / (1 + np.exp(-x))
        fig = px.line(x=x, y=y, title="Sigmoid: σ(x) = 1/(1 + e⁻ˣ)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Distribution Normale")
        x = np.linspace(-4, 4, 100)
        y = stats.norm.pdf(x)
        fig = px.line(x=x, y=y, title="Distribution Normale Standard")
        st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# APPRENTISSAGE STATISTIQUE
# =============================================================================

def apprentissage_statistique():
    st.header("📊 Théorie de l'Apprentissage Statistique")
    
    st.markdown("""
    ## 🎯 Cadre Théorique de Vapnik-Chervonenkis
    """)
    
    st.markdown("""
    ### Risque Empirique vs Risque Réel
    """)
    
    st.latex(r"""
    R(h) = \mathbb{E}_{(x,y) \sim P} [L(h(x), y)]
    """)
    st.latex(r"""
    \hat{R}(h) = \frac{1}{n} \sum_{i=1}^n L(h(x_i), y_i)
    """)
    
    st.markdown("""
    ### Borne de Généralisation VC
    """)
    
    st.latex(r"""
    R(h) \leq \hat{R}(h) + \sqrt{\frac{VC(\mathcal{H}) \left( \log \frac{2n}{VC(\mathcal{H})} + 1 \right) - \log \frac{\delta}{4}}{n}}
    """)
    
    st.markdown("""
    Où:
    - **VC(ℋ):** Dimension de Vapnik-Chervonenkis
    - **δ:** Niveau de confiance (1-δ)
    - **n:** Taille de l'échantillon
    """)
    
    st.markdown("""
    ## 📈 Théorie de l'Information de Shannon
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Entropie
        """)
        st.latex(r"""
        H(X) = -\sum_{i=1}^n p(x_i) \log p(x_i)
        """)
        
        st.markdown("""
        #### Information Mutuelle
        """)
        st.latex(r"""
        I(X;Y) = \sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x)p(y)}
        """)
    
    with col2:
        st.markdown("""
        #### Divergence de Kullback-Leibler
        """)
        st.latex(r"""
        D_{KL}(P \| Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}
        """)
        
        st.markdown("""
        #### Entropie Croisée
        """)
        st.latex(r"""
        H(P,Q) = -\sum_x P(x) \log Q(x)
        """)
    
    st.markdown("""
    ## 🎲 Inférence Bayésienne
    """)
    
    st.markdown("""
    ### Théorème de Bayes
    """)
    
    st.latex(r"""
    P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}
    """)
    
    st.markdown("""
    Où:
    - **P(θ|D):** Distribution a posteriori
    - **P(D|θ):** Vraisemblance
    - **P(θ):** Distribution a priori
    - **P(D):** Évidence
    """)
    
    st.markdown("""
    ### Maximum a Posteriori (MAP)
    """)
    
    st.latex(r"""
    \theta_{MAP} = \arg\max_{\theta} P(\theta | D) = \arg\max_{\theta} P(D | \theta) P(\theta)
    """)

# =============================================================================
# MACHINE LEARNING CLASSIQUE
# =============================================================================

def ml_classique():
    st.header("🌳 Algorithmes de Machine Learning Classique")
    
    st.markdown("""
    ## 📈 Régression et Méthodes Linéaires
    """)
    
    st.markdown("""
    ### Régression Linéaire
    """)
    
    st.latex(r"""
    \hat{y} = \mathbf{w}^T \mathbf{x} + b
    """)
    
    st.markdown("""
    #### Moindres Carrés
    """)
    
    st.latex(r"""
    \min_{\mathbf{w}} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2
    """)
    
    st.markdown("""
    Solution fermée:
    """)
    
    st.latex(r"""
    \mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}
    """)
    
    st.markdown("""
    ### Régression Logistique
    """)
    
    st.latex(r"""
    P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T\mathbf{x} + b)}}
    """)
    
    st.markdown("""
    Fonction de coût (entropie croisée):
    """)
    
    st.latex(r"""
    J(\mathbf{w}) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \right]
    """)
    
    st.markdown("""
    ## 🌲 Arbres de Décision et Ensembles
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Arbre de Décision
        """)
        st.markdown("""
        **Mesure d'impureté:**
        - Entropie: $H(S) = -\sum p_i \log p_i$
        - Gini: $G(S) = 1 - \sum p_i^2$
        """)
        
        st.markdown("""
        **Gain d'information:**
        """)
        st.latex(r"""
        IG(S,A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)
        """)
    
    with col2:
        st.markdown("""
        ### Random Forest
        """)
        st.markdown("""
        **Bagging + décorrélation:**
        """)
        st.latex(r"""
        \hat{f}_{RF}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x})
        """)
        
        st.markdown("""
        ### Gradient Boosting
        """)
        st.latex(r"""
        F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \gamma_m h_m(\mathbf{x})
        """)
        st.latex(r"""
        \gamma_m = \arg\min_{\gamma} \sum_{i=1}^n L(y_i, F_{m-1}(\mathbf{x}_i) + \gamma h_m(\mathbf{x}_i))
        """)
    
    st.markdown("""
    ## 🎯 Machines à Vecteurs de Support (SVM)
    """)
    
    st.markdown("""
    ### SVM Linéaire
    """)
    
    st.latex(r"""
    \min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^n \xi_i
    """)
    st.latex(r"""
    \text{s.t. } y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0
    """)
    
    st.markdown("""
    ### Formulation Duale
    """)
    
    st.latex(r"""
    \max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j
    """)
    st.latex(r"""
    \text{s.t. } 0 \leq \alpha_i \leq C, \quad \sum_{i=1}^n \alpha_i y_i = 0
    """)
    
    st.markdown("""
    ### Kernel Trick
    """)
    
    st.latex(r"""
    K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)
    """)
    
    st.markdown("""
    **Kernels courants:**
    - Polynomial: $K(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T\mathbf{z} + c)^d$
    - RBF: $K(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$
    """)

# =============================================================================
# DEEP LEARNING THÉORIQUE
# =============================================================================

def deep_learning_theorique():
    st.header("🧠 Théorie du Deep Learning")
    
    st.markdown("""
    ## 🏗️ Architectures de Réseaux Neuronaux
    """)
    
    st.markdown("""
    ### Perceptron Multicouche (MLP)
    """)
    
    st.latex(r"""
    \mathbf{h}^{(l)} = \sigma\left(\mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}\right)
    """)
    
    st.markdown("""
    ### Fonctions d'Activation
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### ReLU
        """)
        st.latex(r"""
        \text{ReLU}(x) = \max(0, x)
        """)
        
        st.markdown("""
        #### Sigmoid
        """)
        st.latex(r"""
        \sigma(x) = \frac{1}{1 + e^{-x}}
        """)
    
    with col2:
        st.markdown("""
        #### Tanh
        """)
        st.latex(r"""
        \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
        """)
        
        st.markdown("""
        #### Leaky ReLU
        """)
        st.latex(r"""
        \text{LReLU}(x) = \max(\alpha x, x)
        """)
    
    with col3:
        st.markdown("""
        #### Softmax
        """)
        st.latex(r"""
        \text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}
        """)
        
        st.markdown("""
        #### Swish
        """)
        st.latex(r"""
        \text{swish}(x) = x \cdot \sigma(\beta x)
        """)
    
    st.markdown("""
    ## 🔄 Réseaux Récurrents (RNN/LSTM)
    """)
    
    st.markdown("""
    ### RNN Standard
    """)
    
    st.latex(r"""
    \mathbf{h}_t = \tanh(\mathbf{W}_h \mathbf{h}_{t-1} + \mathbf{W}_x \mathbf{x}_t + \mathbf{b})
    """)
    
    st.markdown("""
    ### LSTM
    """)
    
    st.latex(r"""
    \begin{aligned}
    \mathbf{f}_t &= \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) \\
    \mathbf{i}_t &= \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i) \\
    \mathbf{o}_t &= \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) \\
    \tilde{\mathbf{C}}_t &= \tanh(\mathbf{W}_C [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_C) \\
    \mathbf{C}_t &= \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t \\
    \mathbf{h}_t &= \mathbf{o}_t \odot \tanh(\mathbf{C}_t)
    \end{aligned}
    """)
    
    st.markdown("""
    ## 🎭 Réseaux Convolutifs (CNN)
    """)
    
    st.markdown("""
    ### Opération de Convolution
    """)
    
    st.latex(r"""
    (I * K)(i,j) = \sum_{m} \sum_{n} I(i+m, j+n) K(m, n)
    """)
    
    st.markdown("""
    ### Pooling
    """)
    
    st.latex(r"""
    \text{MaxPool}(X)_{i,j} = \max_{m,n \in \text{window}} X_{i+m, j+n}
    """)
    
    st.markdown("""
    ## 🎯 Transformers et Attention
    """)
    
    st.markdown("""
    ### Attention Scaled Dot-Product
    """)
    
    st.latex(r"""
    \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
    """)
    
    st.markdown("""
    ### Multi-Head Attention
    """)
    
    st.latex(r"""
    \text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)W^O
    """)
    st.latex(r"""
    \text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
    """)

# =============================================================================
# OPTIMISATION & APPRENTISSAGE
# =============================================================================

def optimisation_apprentissage():
    st.header("⚙️ Théorie de l'Optimisation en ML")
    
    st.markdown("""
    ## 📉 Algorithmes d'Optimisation
    """)
    
    st.markdown("""
    ### Descente de Gradient
    """)
    
    st.latex(r"""
    \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla J(\mathbf{w}_t)
    """)
    
    st.markdown("""
    ### Momentum
    """)
    
    st.latex(r"""
    \begin{aligned}
    \mathbf{v}_{t+1} &= \beta \mathbf{v}_t + (1-\beta) \nabla J(\mathbf{w}_t) \\
    \mathbf{w}_{t+1} &= \mathbf{w}_t - \eta \mathbf{v}_{t+1}
    \end{aligned}
    """)
    
    st.markdown("""
    ### Adam
    """)
    
    st.latex(r"""
    \begin{aligned}
    \mathbf{m}_t &= \beta_1 \mathbf{m}_{t-1} + (1-\beta_1) \nabla J(\mathbf{w}_t) \\
    \mathbf{v}_t &= \beta_2 \mathbf{v}_{t-1} + (1-\beta_2) (\nabla J(\mathbf{w}_t))^2 \\
    \hat{\mathbf{m}}_t &= \frac{\mathbf{m}_t}{1-\beta_1^t} \\
    \hat{\mathbf{v}}_t &= \frac{\mathbf{v}_t}{1-\beta_2^t} \\
    \mathbf{w}_{t+1} &= \mathbf{w}_t - \eta \frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon}
    \end{aligned}
    """)
    
    st.markdown("""
    ## 🎯 Théorie de la Convergence
    """)
    
    st.markdown("""
    ### Conditions de Convergence
    """)
    
    st.latex(r"""
    \|\nabla J(\mathbf{w}_t)\| \leq \epsilon \quad \text{ou} \quad |J(\mathbf{w}_{t+1}) - J(\mathbf{w}_t)| \leq \epsilon
    """)
    
    st.markdown("""
    ### Taux de Convergence
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### Linéaire
        """)
        st.latex(r"""
        \|\mathbf{w}_{t+1} - \mathbf{w}^*\| \leq \rho \|\mathbf{w}_t - \mathbf{w}^*\|
        """)
    
    with col2:
        st.markdown("""
        #### Super-linéaire
        """)
        st.latex(r"""
        \lim_{t\to\infty} \frac{\|\mathbf{w}_{t+1} - \mathbf{w}^*\|}{\|\mathbf{w}_t - \mathbf{w}^*\|} = 0
        """)
    
    with col3:
        st.markdown("""
        #### Quadratique
        """)
        st.latex(r"""
        \|\mathbf{w}_{t+1} - \mathbf{w}^*\| \leq C \|\mathbf{w}_t - \mathbf{w}^*\|^2
        """)
    
    st.markdown("""
    ## 🛡️ Régularisation
    """)
    
    st.markdown("""
    ### L1 et L2 Regularization
    """)
    
    st.latex(r"""
    J_{L2}(\mathbf{w}) = J(\mathbf{w}) + \lambda \|\mathbf{w}\|_2^2
    """)
    st.latex(r"""
    J_{L1}(\mathbf{w}) = J(\mathbf{w}) + \lambda \|\mathbf{w}\|_1
    """)
    
    st.markdown("""
    ### Dropout
    """)
    
    st.latex(r"""
    \mathbf{h}_{drop} = \mathbf{h} \odot \mathbf{m}, \quad \mathbf{m}_i \sim \text{Bernoulli}(p)
    """)

# =============================================================================
# FONCTIONS SUIVANTES (similaires pour les autres sections)
# =============================================================================

def validation_evaluation():
    st.header("📈 Théorie de la Validation et Évaluation")
    
    st.markdown("""
    ## 🎯 Métriques de Performance
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Classification
        """)
        st.latex(r"""
        \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
        """)
        st.latex(r"""
        \text{Precision} = \frac{TP}{TP + FP}
        """)
        st.latex(r"""
        \text{Recall} = \frac{TP}{TP + FN}
        """)
        st.latex(r"""
        F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
        """)
    
    with col2:
        st.markdown("""
        ### Régression
        """)
        st.latex(r"""
        \text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
        """)
        st.latex(r"""
        \text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
        """)
        st.latex(r"""
        R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
        """)

def reinforcement_learning():
    st.header("🔄 Apprentissage par Renforcement")
    
    st.markdown("""
    ## 🎯 Processus de Décision Markovien (MDP)
    """)
    
    st.latex(r"""
    \mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)
    """)
    
    st.markdown("""
    ### Équation de Bellman
    """)
    
    st.latex(r"""
    V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_t \mid s_0 = s \right]
    """)
    st.latex(r"""
    V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s'} \mathcal{P}(s'|s,a) [\mathcal{R}(s,a,s') + \gamma V^\pi(s')]
    """)

def nlp_theorie():
    st.header("🔍 Théorie du Traitement du Langage Naturel")
    
    st.markdown("""
    ## 📝 Modèles de Langage
    """)
    
    st.markdown("""
    ### n-gram
    """)
    
    st.latex(r"""
    P(w_n | w_{1:n-1}) \approx P(w_n | w_{n-N+1:n-1})
    """)
    
    st.markdown("""
    ### Word2Vec
    """)
    
    st.latex(r"""
    P(w_o | w_i) = \frac{\exp(\mathbf{v}_{w_o}^T \mathbf{v}_{w_i})}{\sum_{w=1}^W \exp(\mathbf{v}_w^T \mathbf{v}_{w_i})}
    """)

def computer_vision():
    st.header("👁️ Théorie de la Computer Vision")
    
    st.markdown("""
    ## 🎭 Opérations Convolutives
    """)
    
    st.latex(r"""
    \frac{\partial}{\partial x} I(x,y) = I(x+1,y) - I(x,y)
    """)

def mlops_engineering():
    st.header("🏗️ MLOps et Ingénierie des Systèmes IA")
    
    st.markdown("""
    ## 🔄 Cycle de Vie des Modèles ML
    """)
    
    st.markdown("""
    ### ML Pipeline
    """)
    
    st.latex(r"""
    \text{Pipeline} = \{ \text{Data Ingestion} \rightarrow \text{Preprocessing} \rightarrow \text{Training} \rightarrow \text{Evaluation} \rightarrow \text{Deployment} \}
    """)

if __name__ == "__main__":
    main()

# Footer avec références académiques
st.sidebar.markdown("---")
st.sidebar.header("📚 Références Académiques")

st.sidebar.markdown("""
**Livres Fondamentaux:**
- 📖 "Pattern Recognition and Machine Learning" - Bishop
- 📖 "Deep Learning" - Goodfellow, Bengio, Courville
- 📖 "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman

**Articles Séminales:**
- 🎓 "A Theory of Learnability" - Valiant (1984)
- 🎓 "Support-Vector Networks" - Cortes & Vapnik (1995)
- 🎓 "Attention Is All You Need" - Vaswani et al. (2017)

**Cours Universitaires:**
- 🎓 CS229 - Machine Learning (Stanford)
- 🎓 CS231n - CNN for Visual Recognition (Stanford)
- 🎓 6.S191 - Introduction to Deep Learning (MIT)
""")