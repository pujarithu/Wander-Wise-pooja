import streamlit as st
import time

# Page setup with dark theme vibes to match your screenshots
st.set_page_config(page_title="WanderWise", page_icon="🔱", layout="wide")

# Custom CSS for Premium Black & Gold Theme matching your UI
st.markdown("""
    <style>
    body, .main, .block-container { background-color: #0D0D0D; color: #E5E7EB; }
    .title-gold { font-family: 'Georgia', serif; font-size: 3.5rem; color: #D4AF37; font-weight: bold; text-align: center; margin-top: 50px; }
    .subtitle-style { font-family: 'Helvetica', sans-serif; font-size: 1.2rem; color: #A3A3A3; text-align: center; margin-bottom: 40px; font-style: italic; }
    .card-result { background-color: #1A1A1A; border: 1px solid #2A2A2A; padding: 25px; border-radius: 12px; margin-top: 20px; }
    .match-badge { background-color: #D4AF37; color: black; padding: 5px 12px; font-weight: bold; border-radius: 4px; font-size: 0.9rem; }
    div.stButton > button { background-color: transparent; color: #D4AF37; border: 2px solid #D4AF37; font-size: 1.1rem; padding: 10px 30px; width: 100%; border-radius: 0px; transition: 0.3s; }
    div.stButton > button:hover { background-color: #D4AF37; color: black; border: 2px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# --- LOCAL DATABASE FOR MATCHING ---
LOCATIONS_DB = [
    {"name": "Wailea, Maui", "country": "USA", "continent": "Americas", "atmosphere": ["Coastal", "Serenity", "Gastronomy"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600"},
    {"name": "Kyoto", "country": "Japan", "continent": "Asia", "atmosphere": ["Historical", "Serenity", "Artistic"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600"},
    {"name": "Santorini", "country": "Greece", "continent": "Europe", "atmosphere": ["Coastal", "Gastronomy", "Artistic"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1533105079780-92b9be482077?w=600"},
    {"name": "Reykjavik", "country": "Iceland", "continent": "Europe", "atmosphere": ["Northern Lights", "Alpine", "Volcanic Landscapes"], "budget": "Luxury", "img": "https://images.unsplash.com/photo-1504893524553-ac55fce698be?w=600"},
    {"name": "Goa", "country": "India", "continent": "Asia", "atmosphere": ["Coastal", "Excitement", "Gastronomy"], "budget": "Backpacker", "img": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=600"},
    {"name": "Serengeti National Park", "country": "Tanzania", "continent": "Africa", "atmosphere": ["Wildlife Safaris", "Remote Wilderness"], "budget": "Standard", "img": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=600"}
]

# Session State to handle page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- PAGE 1: HOME PAGE ---
if st.session_state.page == 'home':
    st.markdown("<p class='title-gold'>WanderWise</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#A3A3A3; letter-spacing: 3px; font-size:0.8rem;'>THE ART OF UNCOMMON TRAVEL</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    st.markdown("<h1 style='text-align: center; font-family: serif; font-weight: normal; font-size: 3rem;'>Beyond<br>The <i>Ordinary</i></h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle-style'>Where soul meets destination. Describe your desired atmosphere,<br>and we will reveal its geographic equivalent.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE SEARCH"):
            st.session_state.page = 'parameters'
            st.rerun()

# --- PAGE 2: PARAMETERS & SEARCH ---
elif st.session_state.page == 'parameters':
    st.markdown("<h3 style='font-family:serif; color:#D4AF37;'>Define Your Parameters</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Financial Capacity & Temporal Bound
    col1, col2 = st.columns(2)
    with col1:
        currency = st.radio("CURRENCY ORIENTATION", ["USD", "INR", "EUR"], horizontal=True)
        budget_val = st.slider("FINANCIAL CAPACITY (DAILY)", min_value=100, max_value=10000, value=5000)
    with col2:
        days = st.slider("TEMPORAL BOUND (DAYS)", min_value=1, max_value=30, value=7)
    
    # Atmospheric Narrative
    narrative = st.text_area("ATMOSPHERIC NARRATIVE", placeholder="Describe the unseen features of your journey... (e.g., fog rolling over ancient stones, the scent of cedar and rain)")
    
    st.markdown("### SELECT CONTINENT")
    continent = st.radio("CONTINENT", ["Asia", "Europe", "Americas", "Africa", "Oceania"], horizontal=True)
    
    st.markdown("### ATMOSPHERIC PREFERENCES")
    atmos_options = [
        "Alpine", "Coastal", "Metropolis", "Gastronomy", "Excitement", "Serenity", 
        "Historical", "Artistic", "Volcanic Landscapes", "Artisan Villages", 
        "Northern Lights", "Ancient Ruins", "Culinary Deep Dives", "Wildlife Safaris", 
        "Remote Wilderness", "Desert Dunes", "Lush Jungles"
    ]
    selected_atmos = st.multiselect("Select what you feel", atmos_options, default=["Coastal"])
    
    st.markdown("### EXPEDITION PARTY")
    party = st.radio("PARTY", ["SOLO", "COUPLE", "FAMILY", "FRIENDS"], horizontal=True)
    
    st.write("")
    if st.button("REVEAL GEOGRAPHIC EQUIVALENT ✨"):
        with st.spinner("Analyzing parameters and calculating atmospheric equivalents..."):
            time.sleep(2)
            
        st.markdown("### MATCHING DESTINATION")
        
        # Simple Matching Engine Logic
        matches_found = []
        for loc in LOCATIONS_DB:
            score = 60 # base match
            if loc["continent"].lower() == continent.lower():
                score += 20
            # Common atmospheric items
            common_tags = set(loc["atmosphere"]) & set(selected_atmos)
            score += len(common_tags) * 10
            
            if score > 100: score = 98  # Cap at 98% like the screenshot
            if score > 98: score = 98
            
            matches_found.append((loc, score))
            
        # Sort by best match score
        matches_found.sort(key=lambda x: x[1], reverse=True)
        best_match, best_score = matches_found[0]
        
        # Display matching layout similar to screenshot
        col_img, col_det = st.columns([1.2, 1])
        with col_img:
            st.image(best_match["img"], use_container_width=True)
        with col_det:
            st.markdown(f"<span class='match-badge'>MATCH {best_score}%</span>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-family:serif; margin-top:10px;'>{best_match['name']}</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#A3A3A3; font-size:1.2rem; font-weight:bold;'>{best_match['country'].upper()}</p>", unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("#### Dynamic Recommendations Based on Your Flow:")
            st.write(f"• **Expedition Style:** Perfect match for a **{party.title()}** trip.")
            st.write(f"• **Atmosphere Profile:** Filled with {', '.join(best_match['atmosphere'])} vibes.")
            st.write(f"• **Budget Allocation:** Optimized for a ${budget_val} daily index over {days} Days.")
            
        if st.button("BACK TO SEARCH"):
            st.session_state.page = 'parameters'
            st.rerun()
