from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.components.ui import activity_feed, apply_plot_theme, empty_state, glass_panel, metric_card, page_title
from src.services.data_loader import load_result_tables, model_score_frame, synthetic_timeseries
from src.utils.formatting import compact_number, pct


def render() -> None:
    page_title("Live Operations", "AI security operations dashboard", "Track model performance, risk, detections, and analyst activity in a responsive command center.")

    tables = load_result_tables()
    scores = model_score_frame()
    ts = synthetic_timeseries()

    models = scores["Model"].tolist() if "Model" in scores else []
    selected_models = st.multiselect("Filter models", models, default=models)
    filtered_scores = scores[scores["Model"].isin(selected_models)] if selected_models else scores

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        metric_card("Overall model average", pct(filtered_scores["Overall Avg"].mean()), "+6.4% this run", "violet")
    with k2:
        metric_card("Defensive average", pct(filtered_scores["Defensive Avg"].mean()), "Needs calibration", "cyan")
    with k3:
        metric_card("Offensive average", pct(filtered_scores["Offensive Avg"].mean()), "High quality", "emerald")
    with k4:
        metric_card("Samples reviewed", compact_number(sum(len(df) for df in tables.values() if isinstance(df, pd.DataFrame))), "Across all CSVs", "amber")

    left, right = st.columns([1.55, 0.85])
    with left:
        glass_panel("Detection telemetry", "Synthetic real-time trend for product UI preview")
        fig = px.area(ts, x="date", y=["detections", "risk_score"], color_discrete_sequence=["#8b5cf6", "#22d3ee"])
        st.plotly_chart(apply_plot_theme(fig, 410), use_container_width=True)

    with right:
        glass_panel("Activity feed", "Recent analyst and model events")
        activity_feed(
            [
                {"title": "GPT-4 ranked first overall", "detail": "Overall average reached 83.3%.", "time": "2m", "tone": "emerald"},
                {"title": "Intrusion confidence drift", "detail": "False positives increased in low-confidence samples.", "time": "11m", "tone": "cyan"},
                {"title": "Phishing review completed", "detail": "30 samples scored and archived.", "time": "24m", "tone": "violet"},
                {"title": "Risk threshold exceeded", "detail": "Dashboard risk score crossed 72.", "time": "41m", "tone": "rose"},
            ]
        )

    tab1, tab2, tab3 = st.tabs(["Model ranking", "Incident queue", "Evidence"])
    with tab1:
        fig = px.bar(filtered_scores, x="Model", y=["Defensive Avg", "Offensive Avg", "Overall Avg"], barmode="group", color_discrete_sequence=["#22d3ee", "#fbbf24", "#8b5cf6"])
        st.plotly_chart(apply_plot_theme(fig, 420), use_container_width=True)
    with tab2:
        queue = pd.DataFrame(
            [
                ["High", "Suspicious OAuth grant", "Identity", "Contain"],
                ["Medium", "Malware entropy anomaly", "Endpoint", "Investigate"],
                ["High", "Intrusion signature mismatch", "Network", "Tune model"],
                ["Low", "Dataset import completed", "Data", "Closed"],
            ],
            columns=["Severity", "Finding", "Domain", "Status"],
        )
        st.dataframe(queue, use_container_width=True, hide_index=True)
    with tab3:
        summary = tables["summary"]
        if summary.empty:
            empty_state("No summary loaded", "Add result CSV files to populate the dashboard.", "Refresh data")
        else:
            st.dataframe(summary, use_container_width=True, hide_index=True)
