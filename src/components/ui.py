from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st
from plotly import graph_objects as go


ROOT = Path(__file__).resolve().parents[2]


def load_css() -> None:
    css_path = ROOT / "src" / "styles" / "main.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def badge(label: str, tone: str = "violet") -> str:
    return f'<span class="badge badge-{tone}">{label}</span>'


def page_title(eyebrow: str, title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <section class="page-title reveal">
            <div>{badge(eyebrow, "cyan")}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def hero() -> None:
    st.markdown(
        """
        <section class="hero-shell reveal">
            <div class="hero-copy">
                <span class="badge badge-violet">AI Cybersecurity Command Center</span>
                <h1>Turn security experiments into executive-grade intelligence.</h1>
                <p>
                    SentinelAI blends model evaluation, analyst workflows, and board-ready reporting
                    into one polished Streamlit product surface.
                </p>
                <div class="hero-actions">
                    <span class="hero-button">Explore Dashboard</span>
                    <span class="hero-link">Review model evidence</span>
                </div>
            </div>
            <div class="hero-orbit" aria-hidden="true">
                <div class="signal-card signal-a">Risk<br><strong>74</strong></div>
                <div class="signal-card signal-b">Latency<br><strong>842ms</strong></div>
                <div class="signal-card signal-c">Coverage<br><strong>98%</strong></div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, delta: str, tone: str = "violet") -> None:
    st.markdown(
        f"""
        <article class="metric-card metric-{tone} reveal">
            <span>{label}</span>
            <strong>{value}</strong>
            <small>{delta}</small>
        </article>
        """,
        unsafe_allow_html=True,
    )


def feature_card(title: str, text: str, icon: str, tone: str = "violet") -> None:
    st.markdown(
        f"""
        <article class="feature-card reveal">
            <div class="feature-icon icon-{tone}">{icon}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </article>
        """,
        unsafe_allow_html=True,
    )


def glass_panel(title: str, subtitle: str = "") -> None:
    st.markdown(
        f"""
        <div class="panel-heading">
            <div>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def activity_feed(items: Iterable[dict[str, str]]) -> None:
    rows = []
    for item in items:
        tone = item.get("tone", "violet")
        rows.append(
            "<div class='activity-item'>"
            f"<span class='activity-dot {tone}'></span>"
            "<div>"
            f"<strong>{item['title']}</strong>"
            f"<p>{item['detail']}</p>"
            "</div>"
            f"<small>{item['time']}</small>"
            "</div>"
        )

    html = "<div class='activity-feed'>" + "".join(rows) + "</div>"
    if hasattr(st, "html"):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)


def empty_state(title: str, text: str, action: str = "Add data") -> None:
    st.markdown(
        f"""
        <section class="empty-state">
            <div class="empty-symbol">+</div>
            <h3>{title}</h3>
            <p>{text}</p>
            <span>{action}</span>
        </section>
        """,
        unsafe_allow_html=True,
    )


def status_pill(label: str, tone: str) -> str:
    return f'<span class="status-pill {tone}">{label}</span>'


def apply_plot_theme(fig: go.Figure, height: int = 360) -> go.Figure:
    fig.update_layout(
        height=height,
        margin=dict(l=18, r=18, t=42, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB", family="Inter, sans-serif"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor="rgba(148, 163, 184, 0.14)", zeroline=False)
    return fig


def floating_action() -> None:
    st.markdown('<button class="fab" title="Create investigation">+</button>', unsafe_allow_html=True)

