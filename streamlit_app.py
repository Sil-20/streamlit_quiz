quiz_data = [
    {"question": "D'après vous, qu'est-ce qui a le moins d'impact sur le climat ?",
     "option_a": "Repas avec du Boeuf",
     "option_b": "A/R Paris-Marseille en TGV",
     "a_ecv": 7.26,
     "b_ecv": 4.4,
     "img_a": "C:/Users/niems/Downloads/fiche Quiz/repasavecduboeuf.jpg",
     "img_b": "C:/Users/niems/Downloads/fiche Quiz/TGV.jpg",
     "explanation": " 7.26 kg Co2 vs 4.4 kg Co2 pour le TGV. Par personne et par kilomètre, le train pollue 8 fois moins que la voiture et 14 fois moins que l'avion."},
     
    {"question": "D'après vous, qu'est-ce qui a le moins d'impact sur le climat ?",
     "option_a": "1000 recherches Google par jour",
     "option_b": "1 email avec pièce jointe lourde (10Mo)",
     "a_ecv": 0.219,
     "b_ecv": 0.5,
     "img_a": "C:/Users/niems/Downloads/fiche Quiz/recherche_google.jpg",
     "img_b": "C:/Users/niems/Downloads/fiche Quiz/email_lourd.jpg",
     "explanation": "2.19 kg CO2 pour 1000 recherches vs 50g CO2 pour 1 email lourd ! Une recherche Google émet environ 0.2g de CO2, donc même 1000 recherches par jour pendant un an restent moins polluantes qu'un seul gros email avec pièce jointe. Pensez à compresser vos fichiers et vider régulièrement votre boîte mail !"},

    {"question": "D'après vous, qu'est-ce qui a le moins d'impact sur le climat ?",
     "option_a": "10 km en vélo électrique",
     "option_b": "10 km en transports en commun",
     "a_ecv": 0.022,
     "b_ecv": 0.032,
     "img_a": "C:/Users/niems/Downloads/fiche Quiz/velo_electrique.jpg",
     "img_b": "C:/Users/niems/Downloads/fiche Quiz/bus_tram.jpg",
     "explanation": "0.022 kg CO2 pour 10 km en vélo électrique vs 0.032 kg CO2 en transports en commun ! Le vélo électrique reste champion avec seulement 2.2g CO2/km contre 3.2g pour les transports en commun. Même avec sa batterie, le vélo électrique reste très vertueux comparé à tous les autres modes de transport."},

    {"question": "D'après vous, qu'est-ce qui a le moins d'impact sur le climat ?",
     "option_a": "1 Réfrigérateur",
     "option_b": "1 Ordinateur Portable",
     "a_ecv": 339,
     "b_ecv": 193,
     "img_a": "C:/Users/niems/Downloads/fiche Quiz/Refrigerateur.jpg",
     "img_b": "C:/Users/niems/Downloads/fiche Quiz/ordinateur portable.jpg",
     "explanation" : " 339 kg/Co2 pour le réfrigérateur vs 193 kg/Co2 pour l'ordianteur portable ! Les appareils électroménagers ont aussi un fort impact sur le climat. Tout comme les appareils numériques, l'étape de fabrication est celle qui pèse le plus lourd dans leur bilan carbone."},

    {"question": "D'après vous, qu'est-ce qui a le moins d'impact sur le climat ?",
     "option_a": "L'intrégrale de Friends en steaming",
     "option_b": "1 A/R Lille-Nimes en voiture",
     "a_ecv": 7.86,
     "b_ecv": 410,
     "img_a": "C:/Users/niems/Downloads/fiche Quiz/friends.jpg",
     "img_b": "C:/Users/niems/Downloads/fiche Quiz/voiture.jpg",
     "explanation": "7.86 Kg/Co2 pour l'intégrale de Friends vs 410 Kg/Co2 pour un A/R Lille-Nimes ! Regarder les 236 épisodes de Friends en streaming a 50 fois moins d'impact sur l'environnement qu'un déplacement de presque 1000 km en voiture thermique. En effet, aujourd'hui le secteur du transport représente 30% des émission de gaz à effet de serre en France, alors que le secteur du numérique seulement 2,5%."},
]

######################################  debut quizz ######################################

import streamlit as st
import plotly.graph_objects as go  

# 🎨 CSS personnalisé pour un look écologique moderne
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .question-container {
        background: linear-gradient(135deg, #a8e6cf 0%, #dcedc8 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 5px solid #4caf50;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .eco-metric {
        background: rgba(76, 175, 80, 0.1);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #4caf50;
        margin: 0.5rem 0;
    }
    
    .fun-fact {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

# En-tête principal 
st.markdown("""
<div class="main-header">
    <h1>🌍 Quiz Empreinte Carbone 🌱</h1>
    <p>Découvrez les secrets de l'impact climatique !</p>
</div>
""", unsafe_allow_html=True)

# Initialisation des états
if "score" not in st.session_state:  
    st.session_state.score = 0  
if "current" not in st.session_state:  
    st.session_state.current = 0  
if "answered" not in st.session_state:  
    st.session_state.answered = False  

# Sidebar avec tableau de bord en temps réel
with st.sidebar:
    st.markdown("### 🏆 Tableau de Bord Écolo")
    
    # Barre de progression
    progress_percent = st.session_state.current / len(quiz_data)
    st.progress(progress_percent)
    
    # Métriques en temps réel
    current_score_percent = (st.session_state.score / max(1, st.session_state.current)) * 100 if st.session_state.current > 0 else 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Score", f"{st.session_state.score}/{st.session_state.current}")
    with col2:
        st.metric("📈 Réussite", f"{round(current_score_percent)}%")
    
    st.markdown("---")
    st.markdown("### 🌿 Le saviez-vous ?")
    eco_facts = [
        "🚗 1 français émet en moyenne 8,2 tonnes de CO2/an",
        "🌱 Un arbre absorbe 25kg de CO2/an",
        "♻️ Le recyclage réduit l'empreinte de 70%",
        "🚲 Le vélo = 0 émission directe !",
        "💡 LED consomme 80% moins qu'une ampoule classique"
    ]
    if st.session_state.current < len(eco_facts):
        st.info(eco_facts[st.session_state.current])

# Fonction de vérification avec animations
def check_answer(choice):  
    q = quiz_data[st.session_state.current]  
    right = "a" if q["a_ecv"] < q["b_ecv"] else "b"  
    
    if choice == right:  
        st.success("🎉 Excellent ! Bonne réponse !")  
        st.session_state.score += 1
        st.balloons()  # Animation de réussite
    else:  
        st.error("🤔 Pas tout à fait ! Mais c'est instructif !")  

    # Affichage des données avec style
    better_option = "a" if q["a_ecv"] < q["b_ecv"] else "b"
    color_a = "#4caf50" if better_option == "a" else "#ff6b6b"  # Vert si meilleur, rouge sinon
    color_b = "#4caf50" if better_option == "b" else "#ff6b6b"  # Vert si meilleur, rouge sinon
    
    st.markdown(f"""
    <div class="eco-metric">
        <strong>📊 Comparaison CO2 :</strong><br>
        🅰️ {q['option_a']} : <span style="color: {color_a}; font-weight: bold;">{q['a_ecv']} kg CO2</span><br>
        🅱️ {q['option_b']} : <span style="color: {color_b}; font-weight: bold;">{q['b_ecv']} kg CO2</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="fun-fact">
        <strong>💡 Explication :</strong> {q['explanation']}
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.answered = True

# Fonction d'affichage de la question avec style
def show_question(i):  
    q = quiz_data[i]  
    
    # En-tête de question stylé
    st.markdown(f"""
    <div class="question-container">
        <h3>🤔 Question {i+1}/{len(quiz_data)}</h3>
        <p style="font-size: 1.1em; font-weight: 500;">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Options avec layout amélioré
    col1, col2 = st.columns(2, gap="large")  
    
    with col1:  
        st.image(q["img_a"], width=200, caption=f"Option A")
        if st.button(f"🅰️ {q['option_a']}", key="a" + str(i), disabled=st.session_state.answered, 
                    help="Cliquez pour choisir cette option", use_container_width=True):  
            check_answer("a")  
            
    with col2:  
        st.image(q["img_b"], width=200, caption=f"Option B")
        if st.button(f"🅱️ {q['option_b']}", key="b" + str(i), disabled=st.session_state.answered,
                    help="Cliquez pour choisir cette option", use_container_width=True):  
            check_answer("b")  

# Logique principale du quiz
if st.session_state.current < len(quiz_data):  
    show_question(st.session_state.current)  
    
    if st.session_state.answered:
        st.markdown("---")
        if st.button("➡️ Question suivante", key=f"next_{st.session_state.current}", 
                    type="primary", use_container_width=True):  
            st.session_state.current += 1  
            st.session_state.answered = False
            st.rerun()
            
else:   
    # Page finale avec résultats stylés
    score = st.session_state.score
    total = len(quiz_data)
    
    st.markdown("""
    <div class="main-header">
        <h1>🎉 Quiz Terminé ! 🎉</h1>
        <p>Découvrez vos résultats éco-responsables</p>
    </div>
    """, unsafe_allow_html=True)

    # Jauge interactive avec Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "🌱 Score Écologique", 'font': {'size': 28, 'color': '#2e7d32'}},
        delta={'reference': total/2, 'increasing': {'color': "#4caf50"}, 'decreasing': {'color': "#ff9800"}},
        gauge={
            'axis': {'range': [0, total], 'tickwidth': 2, 'tickcolor': "#2e7d32"},
            'bar': {'color': "#4caf50", 'thickness': 0.8},
            'bgcolor': "rgba(255,255,255,0.8)",
            'borderwidth': 3,
            'bordercolor': "#2e7d32",
            'steps': [
                {'range': [0, total*0.2], 'color': '#ffcdd2'},
                {'range': [total*0.2, total*0.4], 'color': '#fff3e0'},
                {'range': [total*0.4, total*0.6], 'color': '#f3e5f5'},
                {'range': [total*0.6, total*0.8], 'color': '#e8f5e8'},
                {'range': [total*0.8, total], 'color': '#c8e6c9'},
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': total*0.8
            }
        }
    ))
    
    fig.update_layout(
        height=400,
        font={'color': "#2e7d32", 'family': "Arial"},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Messages personnalisés avec émojis et couleurs
    score_percentage = (score / total) * 100
    
    if score == total:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4caf50, #8bc34a); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h2>🌟 PARFAIT ! 🌟</h2>
            <p style="font-size: 1.2em;">Vous êtes un véritable champion de l'écologie ! 🏆</p>
            <p>Votre conscience environnementale est exemplaire ! 🌍💚</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
    elif score_percentage >= 60:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8bc34a, #cddc39); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h2>🌱 BIEN JOUÉ ! 🌱</h2>
            <p style="font-size: 1.2em;">Vous avez une bonne connaissance écologique ! 👏</p>
            <p>Continuez sur cette voie verte ! 🚀</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9800, #ffb74d); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h2>🌍 À AMÉLIORER ! 🌍</h2>
            <p style="font-size: 1.2em;">Chaque geste compte pour la planète ! 💪</p>
            <p>Refaites le quiz pour apprendre davantage ! 🔄</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bouton de recommencement stylé
    st.markdown("---")
    if st.button("🔄 Recommencer le Quiz", type="primary", use_container_width=True):
        for key in ['score', 'current', 'answered']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
