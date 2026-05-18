from __future__ import annotations

from typing import Any

import streamlit as st

from src.services.auth_service import create_account


def _render_auth_form(authenticator: Any) -> None:
    try:
        result = authenticator.login(
            location="main",
            fields={
                "Form name": "Sign in",
                "Username": "Email / username",
                "Password": "Password",
                "Login": "Enter workspace",
            },
            key="sentinel_login",
        )
    except TypeError:
        result = authenticator.login("Sign in", "main")

    if isinstance(result, tuple):
        name, authentication_status, username = result
    else:
        name = st.session_state.get("name")
        username = st.session_state.get("username")
        authentication_status = st.session_state.get("authentication_status")

    if authentication_status is False:
        st.error("Email or password is incorrect.")
    elif authentication_status is None:
        st.info("Sign in with an existing account, or create a new one below.")
    elif authentication_status:
        st.success(f"Welcome back, {name or username}.")
        st.rerun()


def _render_registration_form() -> None:
    with st.form("create_account", clear_on_submit=False):
        name = st.text_input("Full name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")
        submitted = st.form_submit_button("Create account", use_container_width=True)

    if submitted:
        created, message = create_account(name, email, password, confirm_password)
        if created:
            st.success(message)
            st.info("Switch to the Sign in tab and use your new account.")
        else:
            st.error(message)


def render(authenticator: Any) -> None:
    left, right = st.columns([0.58, 0.42])
    with left:
        st.markdown(
            """
            <section class="hero-shell reveal" style="min-height:620px">
                <div class="hero-copy">
                    <span class="badge badge-violet">Private Workspace</span>
                    <h1>Welcome back to SentinelAI.</h1>
                    <p>Sign in to your AI cybersecurity command center, or create an account that is stored locally with a hashed password.</p>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown("## Secure access")
        sign_in_tab, create_tab = st.tabs(["Sign in", "Create account"])
        with sign_in_tab:
            _render_auth_form(authenticator)
        with create_tab:
            _render_registration_form()
        st.caption("Accounts are saved in config/auth.yaml. Passwords are stored as hashes, not plain text.")
