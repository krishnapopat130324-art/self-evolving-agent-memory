"""Main entry point for Self-Evolving Agent Memory System"""

import sys
import os
import streamlit as st

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ui import run_ui
from app.agent import MemoryAgent

def main():
    """Initialize and run the application"""
    st.set_page_config(
        page_title="Self-Evolving Agent Memory",
        page_icon="🧠",
        layout="wide"
    )
    
    # Initialize agent (persists across sessions)
    if "agent" not in st.session_state:
        st.session_state.agent = MemoryAgent()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    run_ui(st.session_state.agent)

if __name__ == "__main__":
    main()