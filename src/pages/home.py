from __future__ import annotations

import streamlit as st

from src.components.ui import feature_card, hero, metric_card, page_title
from src.services.data_loader import dataset_inventory, model_score_frame
from src.utils.formatting import compact_number, pct


def render() -> None:
    hero()

    scores = model_score_frame()
    inventory = dataset_inventory()
    best_overall = scores["Overall Avg"].max() if "Overall Avg" in scores else 0

    st.markdown("### Platform snapshot")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Best model score", pct(best_overall), "+18% vs baseline", "violet")
    with c2:
        metric_card("Experiments", compact_number(6), "Defensive + offensive", "cyan")
    with c3:
        metric_card("Datasets indexed", compact_number(len(inventory)), "Ready for analysis", "emerald")
    with c4:
        metric_card("Evidence assets", "9", "Charts + CSVs", "amber")

    page_title(
        "Product Experience",
        "A cybersecurity AI workspace built for analysts, leaders, and model reviewers.",
        "The interface turns notebooks and raw experiment outputs into a navigable SaaS-grade cockpit.",
    )

    f1, f2, f3 = st.columns(3)
    with f1:
        feature_card("Model command center", "Compare LLM and ML performance with defensible, executive-ready visuals.", "AI", "violet")
    with f2:
        feature_card("Secure workspaces", "Create saved analyst accounts with hashed passwords and persistent cookie sessions.", "ID", "cyan")
    with f3:
        feature_card("Evidence-first analytics", "Inspect datasets, results, calibration charts, and performance patterns in one place.", "EV", "rose")

    st.markdown("### Dataset inventory")
    st.dataframe(inventory, use_container_width=True, hide_index=True)
