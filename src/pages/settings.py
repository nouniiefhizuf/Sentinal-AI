from __future__ import annotations

import streamlit as st

from src.components.ui import page_title


def render() -> None:
    page_title("Settings", "Workspace profile and controls", "Customize the product experience, API configuration, notification posture, and runtime preferences.")

    st.markdown("### Profile")
    a, b = st.columns([0.4, 0.6])
    with a:
        st.markdown(
            """
            <div class="profile-card" style="padding:1.25rem">
                <div class="avatar" style="width:64px;height:64px">A</div>
                <h3>Ahmed Security Lab</h3>
                <p style="color:var(--muted)">AI cybersecurity research workspace</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with b:
        with st.form("profile"):
            st.text_input("Workspace name", "SentinelAI")
            st.text_input("Owner", "Ahmed")
            st.text_input("Organization", "AI Cybersecurity Lab")
            st.form_submit_button("Save profile")

    st.markdown("### Preferences")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.settings["theme_mode"] = st.radio("Theme", ["Dark", "Light"], horizontal=True)
        st.session_state.settings["accent"] = st.selectbox("Accent", ["Violet", "Cyan", "Emerald", "Rose"])
    with c2:
        st.session_state.settings["density"] = st.select_slider("Density", ["Compact", "Comfortable", "Spacious"])
        st.session_state.settings["risk_threshold"] = st.slider("Risk threshold", 1, 100, st.session_state.settings["risk_threshold"])
    with c3:
        st.session_state.settings["realtime"] = st.toggle("Real-time updates", st.session_state.settings["realtime"])
        st.session_state.settings["notifications"] = st.toggle("Notifications", st.session_state.settings["notifications"])

    with st.expander("API and model configuration", expanded=True):
        st.selectbox("Default model", ["OpenAI GPT-4", "Mistral Small", "Llama 3 (Groq)", "Local demo responder"])
        st.text_input("API key source", "Use .streamlit/secrets.toml or environment variables", disabled=True)
        st.text_area("System instruction", "You are SentinelAI, a concise cybersecurity analyst copilot.")
