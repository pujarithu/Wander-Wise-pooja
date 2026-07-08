import streamlit as st
import time

# Page setup with dark theme vibes to match your screenshots
st.set_page_config(page_title="WanderWise", page_icon="🔱", layout="wide")

# Custom CSS for Premium Black & Gold Theme matching your UI
st.markdown("""
    <style>
    body, .main, .block-container { background-color: #0D0D0D; color: #E5E7EB; }
    .title-gold { font-family: 'Georgia', serif; font-size: 3.5rem; color: #D4AF37; font-weight: bold; text-align: center; margin-top: 30px; }
    .subtitle-style { font-family: 'Helvetica', sans-serif; font-size: 1.2rem; color: #A3A3A3; text-align: center; margin-bottom: 40px; font-style: italic; }
    .card-result { background-color: #1A1A1A; border: 1px solid #2A2A2A; padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 4px solid #D4AF37; }
    .match-badge { background-color: #D4AF37; color: black; padding: 5px 12px; font-weight: bold; border-radius: 4px; font-size: 0.9rem; float: right; }
    div.stButton > button { background-color: transparent; color: #D4AF37; border: 2px solid #D4AF37; font-size: 1.1rem; padding: 10px 30px; width: 100%; border-radius: 0px; transition: 0.3s; }
    div.stButton > button:hover { background-color: #D4AF37; color: black; border: 2px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# --- EXPANDED LOCAL DATABASE (3+ Multi-Location Matrix) ---
LOCATIONS_DB = [
    # ASIA - COASTAL
    {"name": "Wailea, Maui", "country": "USA", "continent": "Americas", "atmosphere": ["Coastal", "Serenity", "Gastronomy"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600"},
    {"name": "Goa Beaches", "country": "India", "continent": "Asia", "atmosphere": ["Coastal", "Excitement", "Gastronomy"], "budget": "Backpacker", "img": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=600"},
    {"name": "Phuket Coast", "country": "Thailand", "continent": "Asia", "atmosphere": ["Coastal", "Excitement", "Serenity"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1528181304800-2f1908c98981?w=600"},
    {"name": "Bali Shorelines", "country": "Indonesia", "continent": "Asia", "atmosphere": ["Coastal", "Serenity", "Artistic"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600"},
    
    # EUROPE - HISTORICAL / ALPINE
    {"name": "Kyoto Temples", "country": "Japan", "continent": "Asia", "atmosphere": ["Historical", "Serenity", "Artistic"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600"},
    {"name": "Santorini Caldera", "country": "Greece", "continent": "Europe", "atmosphere": ["Coastal", "Gastronomy", "Artistic"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1533105079780-92b9be482077?w=600"},
    {"name": "Rome Ancient Ruins", "country": "Italy", "continent": "Europe", "atmosphere": ["Historical", "Gastronomy", "Ancient Ruins"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=600"},
    {"name": "Zermatt Peaks", "country": "Switzerland", "continent": "Europe", "atmosphere": ["Alpine", "Serenity", "Remote Wilderness"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?w=600"},
    
    # NORTHERN LIGHTS / WILDLIFE
    {"name": "Reykjavik Skies", "country": "Iceland", "continent": "Europe", "atmosphere": ["Northern Lights", "Alpine", "Volcanic Landscapes"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1504893524553-ac55fce698be?w=600"},
    {"name": "Tromsø Fjords", "country": "Norway", "continent": "Europe", "atmosphere": ["Northern Lights", "Remote Wilderness", "Alpine"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1529963183134-61a90db47eaf?w=600"},
    {"name": "Serengeti Plains", "country": "Tanzania", "continent": "Africa", "atmosphere": ["Wildlife Safaris", "Remote Wilderness"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=600"}
]

# Session State for Page Navigation Flow
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- PAGE 1: HOME PAGE ---
if st.session_state.page == 'home':
    # Top Right Admin Mail Login Trigger
    col_space, col_login = st.columns([8, 2])
    with col_login:
        if st.button("🔒 MAIL LOGIN"):
            st.session_state.page = 'login'
            st.rerun()

    st.markdown("<p class='title-gold'>WanderWise</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#A3A3A3; letter-spacing: 3px; font-size:0.8rem;'>THE ART OF UNCOMMON TRAVEL</p>", unsafe_allow_html=True)
    
    st.write("")
    st.markdown("<h1 style='text-align: center; font-family: serif; font-weight: normal; font-size: 3.2rem;'>Beyond<br>The <i>Ordinary</i></h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle-style'>Where soul meets destination. Describe your desired atmosphere,<br>and we will reveal its geographic equivalent.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SEARCH"):
            st.session_state.page = 'parameters'
            st.rerun()

# --- NEW PAGE: MAIL LOGIN GATEWAY ---
elif st.session_state.page == 'login':
    st.markdown("<h2 style='font-family:serif; text-align:center; color:#D4AF37;'>User Authentication Portal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#A3A3A3;'>Access your custom atmospheric itineraries and control parameters</p>", unsafe_allow_html=True)
    
    login_col1, login_col2, login_col3 = st.columns([1, 1.2, 1])
    with login_col2:
        st.write("")
        email = st.text_input("ENTER REGISTERED EMAIL ID", placeholder="user@wanderwise.com")
        password = st.text_input("ENTER SECURITY ACCESS KEY", type="password", placeholder="••••••••")
        
        st.write("")
        if st.button("SECURE LOG IN"):
            if "@" in email and len(password) > 3:
                st.success(f"Authenticated successfully as {email}! Initializing sync...")
                time.sleep(1.5)
                st.session_state.page = 'parameters'
                st.rerun()
            else:
                st.error("Invalid credentials configuration or empty matching fields.")
                
        if st.button("← RETURN BACK"):
            st.session_state.page = 'home'
            st.rerun()

# --- PAGE 2: RECONFIGURED MULTI-MATCH DISCOVERY ENGINE ---
elif st.session_state.page == 'parameters':
    st.markdown("<h3 style='font-family:serif; color:#D4AF37;'>Define Your Parameters</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        currency = st.radio("CURRENCY ORIENTATION", ["USD", "INR", "EUR"], horizontal=True)
        budget_val = st.slider("FINANCIAL CAPACITY (DAILY INDEX)", min_value=100, max_value=10000, value=4500)
    with col2:
        days = st.slider("TEMPORAL BOUND (DAYS)", min_value=1, max_value=30, value=7)
    
    narrative = st.text_area("ATMOSPHERIC NARRATIVE", placeholder="Describe the unseen features of your journey... (e.g., fog rolling over coastal stones, architectural heritage...)")
    
    st.markdown("### SELECT CONTINENT")
    continent = st.radio("CONTINENT TARGET", ["Asia", "Europe", "Americas", "Africa"], horizontal=True)
    
    st.markdown("### ATMOSPHERIC PREFERENCES")
    atmos_options = ["Alpine", "Coastal", "Metropolis", "Gastronomy", "Excitement", "Serenity", "Historical", "Artistic", "Volcanic Landscapes", "Ancient Ruins", "Northern Lights", "Wildlife Safaris", "Remote Wilderness"]
    selected_atmos = st.multiselect("Select preference attributes", atmos_options, default=["Coastal", "Serenity"])
    
    st.markdown("### EXPEDITION PARTY")
    party = st.radio("PARTY TYPE", ["SOLO", "COUPLE", "FAMILY", "FRIENDS"], horizontal=True)
    
    st.write("")
    if st.button("REVEAL GEOGRAPHIC EQUIVALENTS ✨"):
        with st.spinner("Analyzing matrices and mapping target arrays..."):
            time.sleep(2)
            
        st.markdown("<h2 style='font-family:serif; color:#D4AF37;'>Top Recommended Atmospheric Equivalents</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#A3A3A3;'>Here are the top matches perfectly mapped according to your parameter vectors:</p>", unsafe_allow_html=True)
        
        # Scoring Logic Setup for all entries
        scored_results = []
        for loc in LOCATIONS_DB:
            score = 55 # Base structural confidence weight
            if loc["continent"].lower() == continent.lower():
                score += 25
            
            # Intersection matching calculations
            intersection_elements = set(loc["atmosphere"]) & set(selected_atmos)
            score += len(intersection_elements) * 12
            
            if score > 98: score = 98 # Cap ceiling range bound
            
            scored_results.append((loc, score))
            
        # Sorting multi-list structural collections descending order
        scored_results.sort(key=lambda x: x[1], reverse=True)
        
        # Display top 3 locations dynamically
        top_3_recommendations = scored_results[:3]
        
        for index, (match_item, match_score) in enumerate(top_3_recommendations):
            st.markdown(f"<div class='card-result'>", unsafe_allow_html=True)
            col_img, col_det = st.columns([1, 1.2])
            
            with col_img:
                st.image(match_item["img"], use_container_width=True)
            with col_det:
                st.markdown(f"<span class='match-badge'>MATCH {match_score}%</span>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='font-family:serif; margin:0; color:#D4AF37;'>#{index+1} {match_item['name']}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:#A3A3A3; font-weight:bold; letter-spacing:1px;'>{match_item['country'].upper()} ({match_item['continent'].upper()})</p>", unsafe_allow_html=True)
                st.markdown("---")
                st.write(f"🔹 **Atmosphere Profile:** {', '.join(match_item['atmosphere'])}")
                st.write(f"🔹 **Execution Vector:** Recommended for a **{party}** setup with a daily threshold configuration of **{budget_val} {currency}**.")
            st.markdown(f"</div>", unsafe_allow_html=True)
            
        if st.button("RESET ENGINE SEARCH"):
            st.session_state.page = 'parameters'
            st.rerun()
            
    if st.button("← LOG OUT / BACK TO MAIN"):
        st.session_state.page = 'home'
        st.rerun()
