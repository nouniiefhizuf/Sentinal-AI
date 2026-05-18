from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit_authenticator as stauth
import yaml

ROOT = Path(__file__).resolve().parents[2]
AUTH_CONFIG = ROOT / "config" / "auth.yaml"


def load_auth_config() -> dict[str, Any]:
    if not AUTH_CONFIG.exists():
        config = {
            "credentials": {"usernames": {}},
            "cookie": {
                "name": "sentinelai_auth",
                "key": "sentinelai-auth-cookie-key-change-me",
                "expiry_days": 7,
            },
            "preauthorized": {"emails": []},
        }
        save_auth_config(config)
        return config

    with AUTH_CONFIG.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def save_auth_config(config: dict[str, Any]) -> None:
    AUTH_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with AUTH_CONFIG.open("w", encoding="utf-8") as file:
        yaml.safe_dump(config, file, sort_keys=False)


def get_authenticator(config: dict[str, Any]) -> stauth.Authenticate:
    return stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )


def make_password_hash(password: str) -> str:
    """Return a bcrypt hash across supported streamlit-authenticator versions."""
    try:
        return stauth.Hasher([password]).generate()[0]
    except Exception:
        from streamlit_authenticator.utilities.hasher import Hasher

        try:
            return Hasher([password]).generate()[0]
        except Exception:
            return Hasher.hash(password)


def username_from_email(email: str) -> str:
    return email.strip().lower()


def create_account(name: str, email: str, password: str, confirm_password: str) -> tuple[bool, str]:
    if not name.strip() or not email.strip() or not password:
        return False, "Please complete all fields."
    if password != confirm_password:
        return False, "Passwords do not match."
    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    config = load_auth_config()
    users = config.setdefault("credentials", {}).setdefault("usernames", {})
    username = username_from_email(email)

    if username in users:
        return False, "An account with that email already exists."

    users[username] = {
        "email": email.strip().lower(),
        "name": name.strip(),
        "password": make_password_hash(password),
    }
    save_auth_config(config)
    return True, "Account created. You can sign in now."


