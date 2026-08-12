"""Premium Light Theme for Self-Evolving Agent Memory System"""

import streamlit as st
import time
from datetime import datetime

# ============================================
# PREMIUM LIGHT CSS
# ============================================

def load_custom_css():
    """Load premium light custom CSS styling"""
    
    st.markdown("""
    <style>
        /* ===== IMPORT FONTS ===== */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* ===== RESET & BASE ===== */
        .stApp {
            background: linear-gradient(160deg, #f8f6f3 0%, #f0ede8 50%, #e8e4de 100%) !important;
        }
        
        /* ===== SIDEBAR - LIGHT PREMIUM ===== */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, #f8f6f3 100%) !important;
            border-right: 1px solid rgba(0, 0, 0, 0.06) !important;
            box-shadow: 2px 0 30px rgba(0, 0, 0, 0.03) !important;
            padding-top: 1.5rem !important;
        }
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span {
            color: #1a1a2e !important;
        }
        
        /* ===== SIDEBAR LOGO AREA ===== */
        .sidebar-logo {
            text-align: center;
            padding: 0.5rem 0 1.5rem 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        }
        
        .sidebar-logo .logo-icon {
            font-size: 3rem;
            display: block;
            margin-bottom: 0.25rem;
            animation: float 3s ease-in-out infinite;
        }
        
        .sidebar-logo .logo-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #1a1a2e !important;
            letter-spacing: 0.02em;
        }
        
        .sidebar-logo .logo-sub {
            font-family: 'Inter', sans-serif;
            font-size: 0.6rem;
            color: #8a7a6a !important;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-top: 0.1rem;
        }
        
        .sidebar-logo .logo-sub .gold {
            color: #b8860b !important;
        }
        
        /* ===== SIDEBAR SECTIONS ===== */
        .sidebar-section-title {
            font-family: 'Inter', sans-serif;
            font-size: 0.6rem !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: #8a7a6a !important;
            padding: 1rem 0 0.5rem 0;
        }
        
        /* ===== SIDEBAR STAT CARDS - LIGHT ===== */
        .premium-stat {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 0, 0, 0.04);
            border-radius: 12px;
            padding: 0.7rem 1rem;
            margin-bottom: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
        }
        
        .premium-stat:hover {
            background: rgba(255, 255, 255, 0.9);
            border-color: rgba(184, 134, 11, 0.2);
            transform: translateX(4px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
        }
        
        .premium-stat .label {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            color: #5a4a3a;
            font-weight: 400;
        }
        
        .premium-stat .value {
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: #1a1a2e;
        }
        
        .premium-stat .value.gold {
            color: #b8860b;
        }
        
        /* ===== SIDEBAR BUTTONS - LIGHT ===== */
        .premium-btn {
            width: 100%;
            padding: 0.6rem 1rem;
            border: 1px solid rgba(184, 134, 11, 0.2);
            border-radius: 10px;
            background: rgba(184, 134, 11, 0.04);
            color: #1a1a2e !important;
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .premium-btn:hover {
            background: rgba(184, 134, 11, 0.08);
            border-color: #b8860b;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(184, 134, 11, 0.08);
        }
        
        .premium-btn-secondary {
            width: 100%;
            padding: 0.6rem 1rem;
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-radius: 10px;
            background: rgba(0, 0, 0, 0.02);
            color: #5a4a3a !important;
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            font-weight: 400;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
        }
        
        .premium-btn-secondary:hover {
            background: rgba(0, 0, 0, 0.04);
            border-color: rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* ===== MAIN HEADER ===== */
        .main-header {
            text-align: center;
            padding: 1rem 0 0.25rem 0;
        }
        
        .main-header .title {
            font-family: 'Playfair Display', serif;
            font-size: 2.6rem;
            font-weight: 800;
            color: #1a1a2e;
            letter-spacing: -0.02em;
        }
        
        .main-header .title .gold {
            color: #b8860b;
        }
        
        .main-header .subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: #6a5a4a;
            font-weight: 300;
            margin-top: -0.2rem;
        }
        
        .main-header .status-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.5rem;
            margin-top: 0.6rem;
        }
        
        .main-header .status-item {
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        
        .main-header .status-dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #2ecc71;
            animation: pulse-dot 2s ease-in-out infinite;
        }
        
        .main-header .status-text {
            font-family: 'Inter', sans-serif;
            font-size: 0.65rem;
            color: #7a6a5a;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        .main-header .status-divider {
            color: #d4c8b8;
            font-size: 0.5rem;
        }
        
        /* ===== DIVIDER GOLD LIGHT ===== */
        .gold-divider {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, rgba(184, 134, 11, 0.15), rgba(184, 134, 11, 0.25), rgba(184, 134, 11, 0.15), transparent) !important;
            margin: 1rem 0 1.5rem 0 !important;
        }
        
        /* ===== CHAT MESSAGES - LIGHT ===== */
        .chat-user {
            background: linear-gradient(135deg, #1a1a2e 0%, #2d1b69 100%) !important;
            color: #f5f0eb !important;
            border-radius: 20px 20px 4px 20px !important;
            padding: 0.8rem 1.2rem !important;
            margin: 0.4rem 0 !important;
            max-width: 80% !important;
            float: right !important;
            clear: both !important;
            box-shadow: 0 6px 20px rgba(45, 27, 105, 0.15) !important;
            animation: slideRight 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .chat-assistant {
            background: rgba(255, 255, 255, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            color: #1a1a2e !important;
            border-radius: 20px 20px 20px 4px !important;
            padding: 0.8rem 1.2rem !important;
            margin: 0.4rem 0 !important;
            max-width: 80% !important;
            float: left !important;
            clear: both !important;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.04) !important;
            animation: slideLeft 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255, 255, 255, 0.8) !important;
        }
        
        .chat-timestamp {
            font-size: 0.55rem;
            opacity: 0.5;
            margin-top: 0.2rem;
            display: block;
            font-family: 'Inter', sans-serif;
        }
        
        /* ===== CHAT INPUT - LIGHT ===== */
        [data-testid="stChatInput"] {
            border-radius: 16px !important;
            border: 1px solid rgba(0, 0, 0, 0.06) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03) !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px) !important;
        }
        
        [data-testid="stChatInput"]:focus-within {
            border-color: #b8860b !important;
            box-shadow: 0 4px 30px rgba(184, 134, 11, 0.08) !important;
            transform: scale(1.01);
        }
        
        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            border-radius: 12px !important;
            background: rgba(255, 255, 255, 0.6) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(0, 0, 0, 0.04) !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            font-family: 'Inter', sans-serif !important;
            color: #1a1a2e !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(255, 255, 255, 0.8) !important;
            border-color: rgba(184, 134, 11, 0.15) !important;
            transform: translateX(4px);
        }
        
        /* ===== ANIMATIONS ===== */
        @keyframes slideRight {
            0% { opacity: 0; transform: translateX(30px) scale(0.95); }
            100% { opacity: 1; transform: translateX(0) scale(1); }
        }
        
        @keyframes slideLeft {
            0% { opacity: 0; transform: translateX(-30px) scale(0.95); }
            100% { opacity: 1; transform: translateX(0) scale(1); }
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }
        
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.8); }
        }
        
        /* ===== SCROLLBAR ===== */
        ::-webkit-scrollbar { width: 4px; height: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #b8860b, #d4af37);
            border-radius: 10px;
        }
        
        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .main-header .title { font-size: 1.8rem; }
            .chat-user, .chat-assistant { max-width: 95% !important; }
        }
        
        /* ===== STREAMLIT OVERRIDES ===== */
        .stButton > button {
            border-radius: 10px !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
        }
        
        .stAlert {
            border-radius: 12px !important;
            border-left: 3px solid #b8860b !important;
        }
        
        .stInfo {
            border-radius: 12px !important;
        }
        
        .stWarning {
            border-radius: 12px !important;
        }
        
        /* ===== MEMORY CONTEXT CARDS ===== */
        .context-card {
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 0.5rem 0.7rem;
            border-radius: 8px;
            margin-bottom: 0.3rem;
            border-left: 2px solid #b8860b;
            transition: all 0.3s ease;
        }
        
        .context-card:hover {
            background: rgba(255, 255, 255, 0.8);
        }
        
        .context-role {
            font-size: 0.6rem;
            color: #8a7a6a;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .context-text {
            font-size: 0.75rem;
            color: #3a2a2a;
            opacity: 0.7;
        }
    </style>
    """, unsafe_allow_html=True)

# ============================================
# MAIN UI FUNCTION
# ============================================

def run_ui(agent):
    """Main UI function with premium light theme"""
    
    load_custom_css()
    
    # ===== SIDEBAR =====
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-logo">
            <span class="logo-icon">🧠</span>
            <div class="logo-title">Memory System</div>
            <div class="logo-sub"><span class="gold">✦</span> Premium Edition <span class="gold">✦</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="padding: 0 0.5rem;">', unsafe_allow_html=True)
        
        # System Status
        st.markdown('<div class="sidebar-section-title">📊 System Status</div>', unsafe_allow_html=True)
        
        try:
            stats = agent.get_memory_stats()
            total = stats.get("total_memories", 0)
            vector = stats.get("vector_count", 0)
        except:
            total = 0
            vector = 0
        
        st.markdown(f"""
        <div class="premium-stat">
            <span class="label">💾 Total Memories</span>
            <span class="value gold">{total}</span>
        </div>
        <div class="premium-stat">
            <span class="label">🔍 Vector Memories</span>
            <span class="value gold">{vector}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<hr style="border-color: rgba(0,0,0,0.04);">', unsafe_allow_html=True)
        
        # Evolution
        st.markdown('<div class="sidebar-section-title">🔄 Evolution</div>', unsafe_allow_html=True)
        
        try:
            evo_count = len(agent.evolution_engine.get_evolution_history())
        except:
            evo_count = 0
        
        st.markdown(f"""
        <div class="premium-stat">
            <span class="label">⚡ Evolution Events</span>
            <span class="value gold">{evo_count}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<br>', unsafe_allow_html=True)
        
        # Buttons
        st.markdown('<div class="premium-btn">📜 View Evolution Log</div>', unsafe_allow_html=True)
        if st.button("📜 View Evolution Log", key="evo_btn", use_container_width=True):
            try:
                history = agent.evolution_engine.get_evolution_history()
                if history:
                    with st.expander("📋 Evolution Log", expanded=True):
                        for entry in history[-5:]:
                            st.markdown(f"""
                            <div style="background:rgba(255,255,255,0.5);border-radius:8px;padding:0.6rem;margin-bottom:0.4rem;border-left:2px solid #b8860b;">
                                <div style="font-size:0.6rem;color:#8a7a6a;">{entry.get('timestamp','')[:16]}</div>
                                <div style="font-size:0.75rem;color:#1a1a2e;">{entry.get('query','')[:40]}...</div>
                                <div style="font-size:0.65rem;color:#b8860b;">✦ {entry.get('diagnosis',{}).get('category','')}</div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.info("No evolution events yet")
            except:
                st.error("Error loading log")
        
        st.markdown('<div class="premium-btn-secondary">🗑️ Clear Memory</div>', unsafe_allow_html=True)
        if st.button("🗑️ Clear Memory", key="clear_btn", use_container_width=True):
            st.warning("⚠️ Clear memory not implemented for safety")
        
        st.markdown("""
        <hr style="border-color: rgba(0,0,0,0.04);">
        <div style="text-align:center;padding:0.5rem 0;">
            <span style="font-family:'Inter',sans-serif;font-size:0.5rem;color:#b8a898;letter-spacing:0.15em;text-transform:uppercase;">✦ v1.0 · Production Ready ✦</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ===== MAIN CONTENT =====
    st.markdown("""
    <div class="main-header">
        <div class="title">🧠 Self-Evolving <span class="gold">Agent</span></div>
        <div class="subtitle">An AI assistant that learns from its mistakes</div>
        <div class="status-bar">
            <div class="status-item">
                <span class="status-dot"></span>
                <span class="status-text">System Active</span>
            </div>
            <span class="status-divider">✦</span>
            <div class="status-item">
                <span class="status-dot" style="background:#3498db;"></span>
                <span class="status-text">Real-time Memory</span>
            </div>
            <span class="status-divider">✦</span>
            <div class="status-item">
                <span class="status-dot" style="background:#b8860b;"></span>
                <span class="status-text">Self-Learning</span>
            </div>
        </div>
    </div>
    <hr class="gold-divider">
    """, unsafe_allow_html=True)
    
    # ===== CHAT + CONTEXT LAYOUT =====
    col_chat, col_context = st.columns([2.5, 1])
    
    with col_chat:
        st.markdown('<span style="font-family:Playfair Display,serif;font-size:1.1rem;font-weight:600;color:#1a1a2e;">💬 Conversation</span>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="chat-user">
                    {msg["content"]}
                    <span class="chat-timestamp">{msg.get("timestamp", "")}</span>
                </div>
                <div style="clear:both;"></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-assistant">
                    {msg["content"]}
                    <span class="chat-timestamp">{msg.get("timestamp", "")}</span>
                </div>
                <div style="clear:both;"></div>
                """, unsafe_allow_html=True)
    
    with col_context:
        st.markdown('<span style="font-family:Playfair Display,serif;font-size:1.1rem;font-weight:600;color:#1a1a2e;">🧠 Memory Context</span>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        
        if "messages" in st.session_state and st.session_state.messages:
            with st.expander("📝 Recent Context", expanded=True):
                for msg in st.session_state.messages[-3:]:
                    icon = "👤" if msg["role"] == "user" else "🤖"
                    st.markdown(f"""
                    <div class="context-card">
                        <div class="context-role">{icon} {msg["role"].capitalize()}</div>
                        <div class="context-text">{msg["content"][:60]}{"..." if len(msg["content"]) > 60 else ""}</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align:center;padding:2.5rem 0;">
                <div style="font-size:2.5rem;opacity:0.15;">💭</div>
                <div style="font-family:Inter,sans-serif;font-size:0.8rem;color:#8a7a6a;opacity:0.3;">No messages yet</div>
                <div style="font-family:Inter,sans-serif;font-size:0.65rem;color:#8a7a6a;opacity:0.2;">Start a conversation below</div>
            </div>
            """, unsafe_allow_html=True)
    
    # ===== CHAT INPUT =====
    st.markdown('<br>', unsafe_allow_html=True)
    
    prompt = st.chat_input("💬 Ask me anything...")
    
    if prompt:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("✨ Thinking..."):
                try:
                    result = agent.process_query(prompt, st.session_state.messages)
                    response = result.get("response", "No response generated")
                    
                    if result.get("memories_used"):
                        st.caption(f"📚 Used {len(result['memories_used'])} memories")
                    
                    st.markdown(response)
                    
                except Exception as e:
                    st.error(f"⚠️ {str(e)}")
                    response = "Sorry, I encountered an error. Please try again."
                    st.markdown(response)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        st.rerun()