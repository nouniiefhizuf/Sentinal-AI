from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = ROOT / "datasets"
RESULTS_DIR = ROOT / "results"


@st.cache_data(show_spinner=False)
def load_csv(path: str | Path, nrows: int | None = None) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        return pd.DataFrame()
    return pd.read_csv(file_path, nrows=nrows)


@st.cache_data(show_spinner=False)
def load_result_tables() -> dict[str, pd.DataFrame]:
    tables = {
        "scores": load_csv(RESULTS_DIR / "experiment_scores.csv"),
        "summary": load_csv(RESULTS_DIR / "master_results_summary.csv"),
        "phishing": load_csv(RESULTS_DIR / "p1_phishing_detection.csv"),
        "malware": load_csv(RESULTS_DIR / "p3_malware_analysis.csv"),
        "intrusion": load_csv(RESULTS_DIR / "p5_intrusion_detection.csv"),
        "generation": load_csv(RESULTS_DIR / "p2_phishing_generation.csv"),
        "vulns": load_csv(RESULTS_DIR / "p4_vuln_discovery.csv"),
        "planning": load_csv(RESULTS_DIR / "p6_attack_planning.csv"),
    }
    return tables


@st.cache_data(show_spinner=False)
def dataset_inventory() -> pd.DataFrame:
    rows = []
    for file_path in sorted(DATASETS_DIR.glob("*.csv")):
        preview = load_csv(file_path, nrows=5)
        rows.append(
            {
                "Dataset": file_path.stem.replace("_", " ").title(),
                "File": file_path.name,
                "Size MB": round(file_path.stat().st_size / 1_048_576, 2),
                "Columns": len(preview.columns),
                "Preview Rows": len(preview),
            }
        )
    return pd.DataFrame(rows)


def result_images() -> list[Path]:
    return sorted(RESULTS_DIR.glob("*.png"))


def model_score_frame() -> pd.DataFrame:
    scores = load_result_tables()["scores"]
    if scores.empty:
        return pd.DataFrame(
            {
                "Model": ["OpenAI GPT-4", "Mistral Small", "Llama 3 (Groq)"],
                "Defensive Avg": [0.67, 0.50, 0.47],
                "Offensive Avg": [1.00, 0.83, 0.98],
                "Overall Avg": [0.83, 0.67, 0.73],
            }
        )
    return scores


def synthetic_timeseries(days: int = 30) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days)
    return pd.DataFrame(
        {
            "date": dates,
            "detections": rng.integers(120, 360, size=days),
            "false_positive_rate": np.clip(rng.normal(0.12, 0.035, size=days), 0.03, 0.22),
            "latency_ms": rng.integers(420, 1250, size=days),
            "risk_score": np.clip(rng.normal(71, 8, size=days), 42, 96),
        }
    )
