import streamlit as st
import time
from main import run_travel_planner

st.set_page_config(
    page_title="FlyR — AI Travel Planner",
    page_icon="🛫",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

[data-testid="stAppViewContainer"] {
    background: #f8f9fa;
}

[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e8ecf0;
    box-shadow: 2px 0 12px rgba(0,0,0,0.06);
}

.hero {
    background: linear-gradient(135deg, #003580 0%, #0071c2 60%, #00a8e6 100%);
    border-radius: 24px;
    padding: 3.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    color: white;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
    border-radius: 50%;
}

.hero::after {
    content: '✈';
    position: absolute;
    font-size: 18rem;
    opacity: 0.05;
    bottom: -3rem;
    right: 2rem;
    transform: rotate(-20deg);
}

.hero-logo {
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.7);
    margin-bottom: 1rem;
}

.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    color: white;
    line-height: 1.1;
    margin-bottom: 1rem;
}

.hero-title span {
    color: #ffd700;
}

.hero-sub {
    color: rgba(255,255,255,0.8);
    font-size: 1.1rem;
    font-weight: 300;
    max-width: 550px;
    line-height: 1.6;
}

.search-box {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    margin-bottom: 1.5rem;
    border: 1px solid #e8ecf0;
}

.search-box-title {
    font-size: 1rem;
    font-weight: 700;
    color: #003580;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.stat-card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    border: 1px solid #e8ecf0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,113,194,0.15);
    border-color: #0071c2;
}

.stat-number {
    font-size: 2.2rem;
    font-weight: 800;
    color: #0071c2;
}

.stat-label {
    color: #6b7280;
    font-size: 0.8rem;
    margin-top: 0.3rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.agent-pill {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.9rem 1rem;
    border-radius: 12px;
    margin-bottom: 0.5rem;
    background: #f8f9fa;
    border: 1px solid #e8ecf0;
    transition: all 0.3s ease;
    cursor: default;
}

.agent-pill:hover {
    background: #e8f4fd;
    border-color: #0071c2;
    transform: translateX(4px);
}

.agent-pill-icon {
    font-size: 1.3rem;
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #003580, #0071c2);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.agent-pill-name {
    font-weight: 600;
    font-size: 0.88rem;
    color: #1a1a2e;
}

.agent-pill-role {
    font-size: 0.75rem;
    color: #9ca3af;
}

.pulse-dot {
    width: 7px;
    height: 7px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 1.5s infinite;
    margin-right: 4px;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

.progress-step {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.85rem 1.2rem;
    border-radius: 12px;
    margin-bottom: 0.5rem;
    font-size: 0.88rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

.step-done {
    background: #f0fdf4;
    border: 1px solid #86efac;
    color: #16a34a;
}

.step-active {
    background: #eff6ff;
    border: 1px solid #93c5fd;
    color: #1d4ed8;
}

.step-pending {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    color: #9ca3af;
}

.result-card {
    background: white;
    border-radius: 20px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    border: 1px solid #e8ecf0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
}

.result-card:hover {
    box-shadow: 0 8px 24px rgba(0,113,194,0.1);
    border-color: #0071c2;
}

.result-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: #003580;
    margin-bottom: 1rem;
    padding-bottom: 0.8rem;
    border-bottom: 2px solid #e8f4fd;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.result-content {
    color: #374151;
    font-size: 0.92rem;
    line-height: 1.8;
    white-space: pre-wrap;
}

.summary-card {
    background: linear-gradient(135deg, #003580 0%, #0071c2 100%);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    color: white;
}

.summary-card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffd700;
    margin-bottom: 1rem;
}

.summary-card-content {
    color: rgba(255,255,255,0.9);
    font-size: 0.95rem;
    line-height: 1.8;
    white-space: pre-wrap;
}

.trip-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 20px;
    padding: 0.3rem 1rem;
    font-size: 0.82rem;
    color: white;
    font-weight: 600;
    margin: 0.2rem;
}

.feature-card {
    background: white;
    border-radius: 18px;
    padding: 1.8rem;
    border: 1px solid #e8ecf0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
    height: 100%;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,113,194,0.12);
    border-color: #0071c2;
}

.feature-icon {
    font-size: 2.2rem;
    margin-bottom: 1rem;
}

.feature-title {
    font-size: 1rem;
    font-weight: 700;
    color: #003580;
    margin-bottom: 0.5rem;
}

.feature-desc {
    color: #6b7280;
    font-size: 0.88rem;
    line-height: 1.7;
}

.stButton > button {
    background: linear-gradient(135deg, #003580, #0071c2) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 2rem !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    letter-spacing: 0.3px !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(0,113,194,0.35) !important;
}

.sidebar-section {
    font-size: 0.75rem;
    font-weight: 700;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 1.2rem 0 0.6rem 0;
}

.success-banner {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border: 1px solid #86efac;
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.5rem;
    color: #16a34a;
    font-weight: 600;
    font-size: 1rem;
    text-align: center;
}

.stTextInput input {
    border-radius: 10px !important;
    border: 1.5px solid #e8ecf0 !important;
    font-size: 0.9rem !important;
}

.stTextInput input:focus {
    border-color: #0071c2 !important;
    box-shadow: 0 0 0 3px rgba(0,113,194,0.1) !important;
}

div[data-testid="stMarkdownContainer"] p { color: #374151; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1.5rem 0;">
        <div style="font-size:1.8rem; font-weight:800; color:#003580; letter-spacing:-1px;">🛫 FlyR</div>
        <div style="font-size:0.8rem; color:#9ca3af; font-weight:500; margin-top:0.2rem;">AI-Powered Travel Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Trip Details</div>', unsafe_allow_html=True)

    origin = st.text_input("✈️ Flying From", placeholder="e.g. Lahore")
    destination = st.text_input("📍 Destination", placeholder="e.g. Paris")
    date = st.date_input("📅 Travel Date")
    days = st.slider("🌙 Duration (days)", min_value=1, max_value=14, value=5)
    interests = st.text_area("❤️ Interests", placeholder="e.g. art, food, history", height=90)

    st.markdown("<br>", unsafe_allow_html=True)
    plan_button = st.button("🚀 Launch AI Agents", use_container_width=True)

    st.markdown('<div class="sidebar-section">Agent Team</div>', unsafe_allow_html=True)

    agents_info = [
        ("🎯", "Orchestrator", "Master coordinator"),
        ("✈️", "Flight Agent", "Finds best flights"),
        ("🏨", "Hotel Agent", "Accommodation expert"),
        ("🌤️", "Weather Agent", "Forecast specialist"),
        ("💰", "Budget Agent", "Cost optimizer"),
        ("📅", "Itinerary Agent", "Trip designer"),
    ]

    for icon, name, role in agents_info:
        st.markdown(f"""
        <div class="agent-pill">
            <div style="font-size:1.1rem; min-width:28px;">{icon}</div>
            <div>
                <div class="agent-pill-name"><span class="pulse-dot"></span>{name}</div>
                <div class="agent-pill-role">{role}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#eff6ff; border-radius:12px; padding:1rem; border:1px solid #bfdbfe;">
        <div style="font-size:0.8rem; color:#1d4ed8; font-weight:600;">💡 Powered by</div>
        <div style="font-size:0.85rem; color:#374151; margin-top:0.3rem;">Groq LLaMA 3 · 70B · CrewAI Framework</div>
    </div>""", unsafe_allow_html=True)

# ── MAIN ──────────────────────────────────────────────────────────────
if not plan_button:
    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-logo">🛫 FlyR AI</div>
        <div class="hero-title">Your personal<br><span>AI travel team</span></div>
        <div class="hero-sub">6 specialized AI agents work together to plan your perfect trip — flights, hotels, weather, budget and a full itinerary in one click.</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip(
        [c1, c2, c3, c4],
        [("6", "AI Agents"), ("5+", "Task Types"), ("∞", "Destinations"), ("Free", "To Use")]
    ):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{num}</div>
                <div class="stat-label">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How it works
    st.markdown('<div style="font-size:1.3rem; font-weight:800; color:#003580; margin-bottom:1.2rem;">⚡ How FlyR Works</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    features = [
        ("🗺️", "Set Your Destination", "Enter origin, destination, travel dates and your personal interests in the sidebar panel."),
        ("🤖", "6 Agents Work For You", "Each AI agent specializes in one area — flights, hotels, weather, budget and itinerary."),
        ("📋", "Get Your Perfect Plan", "The Orchestrator compiles everything into one beautiful, comprehensive travel plan."),
    ]
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Agent showcase
    st.markdown('<div style="font-size:1.3rem; font-weight:800; color:#003580; margin-bottom:1.2rem;">🤖 Meet Your AI Agents</div>', unsafe_allow_html=True)
    agent_details = [
        ("🎯", "Orchestrator Agent", "Manages all agents, delegates tasks and compiles the final comprehensive travel plan.", "#003580"),
        ("✈️", "Flight Agent", "Searches global airlines to find the best flights matching your budget and schedule.", "#0071c2"),
        ("🏨", "Hotel Agent", "Finds perfect accommodations from budget to luxury matching your exact preferences.", "#0ea5e9"),
        ("🌤️", "Weather Agent", "Provides detailed forecasts and smart packing recommendations for your destination.", "#06b6d4"),
        ("💰", "Budget Agent", "Calculates complete trip costs across budget tiers with smart optimization tips.", "#10b981"),
        ("📅", "Itinerary Agent", "Designs a personalized day-by-day plan based on your interests and local insights.", "#8b5cf6"),
    ]
    col1, col2 = st.columns(2)
    for i, (icon, name, desc, color) in enumerate(agent_details):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="feature-card" style="border-left: 4px solid {color}; margin-bottom:1rem;">
                <div style="font-size:1.8rem; margin-bottom:0.5rem;">{icon}</div>
                <div class="feature-title" style="color:{color};">{name}</div>
                <div class="feature-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

else:
    if not origin or not destination or not interests:
        st.markdown("""
        <div style="background:#fef2f2; border:1px solid #fca5a5; border-radius:16px;
        padding:1.5rem; text-align:center; color:#dc2626; font-weight:600;">
            ⚠️ Please fill in Flying From, Destination, and Interests!
        </div>""", unsafe_allow_html=True)
    else:
        trip_details = {
            "origin": origin,
            "destination": destination,
            "date": str(date),
            "days": days,
            "interests": interests
        }

        # Trip header
        st.markdown(f"""
        <div class="hero" style="padding:2rem;">
            <div class="hero-logo">NEW TRIP</div>
            <div style="font-size:2.2rem; font-weight:800; color:white; margin-bottom:1rem;">
                {origin} → {destination}
            </div>
            <span class="trip-badge">📅 {str(date)}</span>
            <span class="trip-badge">🌙 {days} Days</span>
            <span class="trip-badge">❤️ {interests}</span>
        </div>
        """, unsafe_allow_html=True)

        # Agent progress
        st.markdown('<div style="font-size:1.1rem; font-weight:800; color:#003580; margin-bottom:1rem;">🤖 Agent Progress</div>', unsafe_allow_html=True)

        steps = [
            ("✈️", "Flight Agent", "Searching best flights"),
            ("🏨", "Hotel Agent", "Finding accommodations"),
            ("🌤️", "Weather Agent", "Checking forecasts"),
            ("💰", "Budget Agent", "Calculating costs"),
            ("📅", "Itinerary Agent", "Designing itinerary"),
            ("🎯", "Orchestrator", "Compiling final plan"),
        ]

        step_containers = []
        cols_steps = st.columns(2)
        for i, (icon, name, action) in enumerate(steps):
            with cols_steps[i % 2]:
                c = st.empty()
                step_containers.append(c)
                c.markdown(f"""
                <div class="progress-step step-pending">
                    {icon} {name} — {action}
                </div>""", unsafe_allow_html=True)

        progress_bar = st.progress(0)
        status_text = st.empty()

        def update_progress(step, message):
            for i, c in enumerate(step_containers):
                icon, name, action = steps[i]
                if i < step - 1:
                    c.markdown(f"""
                    <div class="progress-step step-done">
                        ✅ {name} — Complete
                    </div>""", unsafe_allow_html=True)
                elif i == step - 1:
                    c.markdown(f"""
                    <div class="progress-step step-active">
                        <span class="pulse-dot"></span>{icon} {name} — Working...
                    </div>""", unsafe_allow_html=True)
            progress_bar.progress(int((step / 6) * 100))
            status_text.markdown(f'<div style="color:#0071c2; font-size:0.9rem; text-align:center; font-weight:500;">{message}</div>', unsafe_allow_html=True)

        try:
            results = run_travel_planner(trip_details, update_progress)

            for i, c in enumerate(step_containers):
                icon, name, action = steps[i]
                c.markdown(f"""
                <div class="progress-step step-done">
                    ✅ {name} — Complete
                </div>""", unsafe_allow_html=True)

            progress_bar.progress(100)
            status_text.empty()

            st.markdown("""
            <div class="success-banner">
                ✅ All 6 AI Agents Completed — Your Travel Plan is Ready!
            </div>""", unsafe_allow_html=True)

            # Summary
            st.markdown(f"""
            <div class="summary-card">
                <div class="summary-card-title">📋 Executive Summary by Orchestrator Agent</div>
                <div class="summary-card-content">{results['summary']}</div>
            </div>""", unsafe_allow_html=True)

            # Stats
            c1, c2, c3, c4 = st.columns(4)
            for col, (num, label) in zip(
                [c1, c2, c3, c4],
                [(f"{origin}→{destination}", "Route"), (f"{days}", "Days"), ("6", "Agents"), ("✅", "Status")]
            ):
                with col:
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-number" style="font-size:1.4rem;">{num}</div>
                        <div class="stat-label">{label}</div>
                    </div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div style="font-size:1.2rem; font-weight:800; color:#003580; margin-bottom:1rem;">🔍 Detailed Agent Reports</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                for header, key in [("✈️ Flight Options", "flights"), ("🌤️ Weather Forecast", "weather"), ("📅 Day-by-Day Itinerary", "itinerary")]:
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-header">{header}</div>
                        <div class="result-content">{results[key]}</div>
                    </div>""", unsafe_allow_html=True)

            with col2:
                for header, key in [("🏨 Hotel Recommendations", "hotels"), ("💰 Budget Breakdown", "budget")]:
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-header">{header}</div>
                        <div class="result-content">{results[key]}</div>
                    </div>""", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Check your GROQ_API_KEY in the .env file")
            st.code(str(e))