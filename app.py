from __future__ import annotations

import streamlit as st

from src.components.ui import floating_action, load_css
from src.pages import analytics, dashboard, home, login, settings
from src.services.auth_service import get_authenticator, load_auth_config
from src.utils.state import init_session_state, setting


st.set_page_config(
    page_title="SentinelAI | Cybersecurity Command Center",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()
load_css()

if setting("theme_mode") == "Light":
    st.markdown(
        """
        <style>
        .stApp {
          --bg: #f8fafc;
          --panel: rgba(255, 255, 255, 0.78);
          --panel-strong: rgba(255, 255, 255, 0.94);
          --stroke: rgba(15, 23, 42, 0.12);
          --text: #0f172a;
          --muted: #64748b;
          background:
            radial-gradient(circle at 6% 8%, rgba(124, 92, 255, 0.18), transparent 32rem),
            radial-gradient(circle at 88% 2%, rgba(34, 211, 238, 0.16), transparent 30rem),
            linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

PAGES = {
    "Home": home.render,
    "Dashboard": dashboard.render,
    "Analytics": analytics.render,
    "Settings": settings.render,
}


def render_sidebar(authenticator) -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="brand-lockup">
                <div class="brand-mark">S</div>
                <div>
                    <strong>SentinelAI</strong>
                    <span>AI Cybersecurity Platform</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        user_name = st.session_state.get("name") or "Analyst"
        st.caption(f"Signed in as {user_name}")
        st.caption("Navigation")
        if st.session_state.active_page not in PAGES:
            st.session_state.active_page = "Home"

        for page in PAGES:
            active = page == st.session_state.active_page
            label = f"{'* ' if active else ''}{page}"
            if st.button(label, key=f"nav_{page}", use_container_width=True):
                st.session_state.active_page = page
                st.rerun()

        st.divider()
        st.caption("Workspace")
        st.progress(st.session_state.settings["risk_threshold"] / 100, text=f"Risk threshold: {st.session_state.settings['risk_threshold']}")
        st.toggle("Real-time updates", key="sidebar_realtime", value=st.session_state.settings["realtime"])
        st.selectbox("Model", ["OpenAI GPT-4", "Mistral Small", "Llama 3 (Groq)", "Local demo responder"], index=0)

        st.divider()
        try:
            authenticator.logout("Lock workspace", "sidebar")
        except TypeError:
            authenticator.logout(location="sidebar")


config = load_auth_config()
authenticator = get_authenticator(config)

if st.session_state.get("authentication_status"):
    render_sidebar(authenticator)
    PAGES[st.session_state.active_page]()
    floating_action()
else:
    login.render(authenticator)
