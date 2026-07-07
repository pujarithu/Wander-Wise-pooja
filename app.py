import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="WanderWise | AI Travel Planner", page_icon="🌍", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title { font-size: 3rem; font-weight: 700; color: #2E86C1; margin-bottom: 0px; }
    .sub-title { font-size: 1.2rem; color: #5D6D7E; margin-bottom: 30px; }
    .stButton>button { background-color: #2E86C1; color: white; font-weight: bold; border-radius: 5px; width: 100%; }
    .stButton>button:hover { background-color: #1B4F72; }
    .card { background-color: #F2F4F4; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #2E86C1; }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<div class="main-title">🌍 WanderWise</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your AI-Powered Travel Companion</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar Controls
st.sidebar.header("✈️ Plan Your Trip")
destination = st.sidebar.text_input("Where do you want to go?", placeholder="e.g., Goa, Paris, Bali")
days = st.sidebar.slider("Number of Days", min_value=1, max_value=7, value=3)
budget = st.sidebar.selectbox("Budget", ["Backpacker", "Standard", "Luxury"])
travel_style = st.sidebar.multiselect("Travel Style", ["Culture & History", "Adventure", "Relaxation", "Food & Drink", "Nightlife"], default=["Relaxation", "Food & Drink"])

if st.sidebar.button("Generate Itinerary ✨"):
    if destination:
        # Faking the API call for presentation
        with st.spinner(f"WanderWise AI is analyzing {destination.title()} and crafting your {budget.lower()} trip..."):
            time.sleep(3) 
            
        st.success(f"🎉 Your {days}-day itinerary for **{destination.title()}** is ready!")
        
        # Dashboard Metrics
        st.header(f"📍 {destination.title()} Trip Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Duration", f"{days} Days")
        col2.metric("Budget Level", budget)
        col3.metric("Style", ", ".join(travel_style) if travel_style else "General Sightseeing")
        
        st.markdown("### 🗺️ Daily Itinerary")
        
        # Dynamic Tabs based on days selected
        tabs = st.tabs([f"Day {i+1}" for i in range(days)])
        
        for i, tab in enumerate(tabs):
            with tab:
                st.markdown(f"#### 🌅 Morning")
                st.markdown(f'<div class="card"><b>Breakfast & Explore:</b> Start your day with a local breakfast in {destination.title()}. Head out to visit the most iconic landmarks nearby.</div>', unsafe_allow_html=True)
                
                st.markdown(f"#### ☀️ Afternoon")
                st.markdown(f'<div class="card"><b>Lunch & Activities:</b> Enjoy a {budget.lower()}-friendly meal. The afternoon is reserved for the best <b>{travel_style[0] if travel_style else "activities"}</b> experiences {destination.title()} has to offer! 📸</div>', unsafe_allow_html=True)
                
                st.markdown(f"#### 🌙 Evening")
                st.markdown(f'<div class="card"><b>Dinner & Unwind:</b> Perfect time to relax. Head to a highly-rated local spot to wrap up your day. 🍽️</div>', unsafe_allow_html=True)
                
        st.markdown("---")
        st.markdown("### ⭐ WanderWise Top Recommendations")
        rc1, rc2, rc3 = st.columns(3)
        with rc1:
            st.info(f"**🏨 Hotels in {destination.title()}**\n- Central Boutique Hotel\n- The Grand Stay\n- Cozy Backpackers Hostel")
        with rc2:
            st.warning("**🍲 Must Try Food**\n- Local Street Food\n- Signature Regional Dish\n- Traditional Dessert")
        with rc3:
            st.success("**💡 Travel Tips**\n- Carry local currency\n- Book tickets in advance\n- Use public transport")
            
        st.balloons()
    else:
        st.sidebar.error("Please enter a destination to get started!")
else:
    st.info("👈 Enter your travel preferences in the sidebar and click 'Generate Itinerary' to see the magic!")
    
    # Beautiful landing images
    st.markdown("### Trending Destinations")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=400&q=80", caption="Paris, France")
    with col2:
        st.image("https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=400&q=80", caption="Bali, Indonesia")
    with col3:
        st.image("https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=400&q=80", caption="Taj Mahal, India")