from __future__ import annotations

import streamlit as st

from src.components.ui import page_title
from src.services.data_loader import load_result_tables, result_images


def render() -> None:
    page_title("Analytics Lab", "Advanced model and dataset analytics", "Explore performance, calibration, evidence artifacts, exports, and interactive tables.")

    tables = load_result_tables()

    st.markdown("### Experiment tables")
    table_name = st.selectbox("Choose evidence table", list(tables.keys()))
    table = tables[table_name]
    st.dataframe(table, use_container_width=True, hide_index=True)
    st.download_button("Export filtered table", table.to_csv(index=False).encode("utf-8"), file_name=f"{table_name}_export.csv", mime="text/csv")

    st.markdown("### Published figures")
    images = result_images()
    cols = st.columns(3)
    for index, image in enumerate(images):
        with cols[index % 3]:
            st.image(str(image), caption=image.stem.replace("_", " ").title(), use_container_width=True)
