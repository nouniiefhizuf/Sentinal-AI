from __future__ import annotations

import streamlit as st


DEFAULT_SETTINGS = {
    "theme_mode": "Dark",
    "accent": "Violet",
    "density": "Comfortable",
    "realtime": True,
    "notifications": True,
    "risk_threshold": 72,
    "model": "OpenAI GPT-4",
}


def init_session_state() -> None:
    """Initialize app-level state once per user session."""
    defaults = {
        "active_page": "Home",
        "settings": DEFAULT_SETTINGS.copy(),
        "last_upload_name": None,
    }

    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def setting(name: str):
    return st.session_state.settings.get(name, DEFAULT_SETTINGS.get(name))
