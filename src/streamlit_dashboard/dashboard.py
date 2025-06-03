import streamlit as st
from read_data import read_data
from kpis import (
    number_approved
    , total_application
    , approved_percentage
    , provider_kpis
    , number_distance
    , approved_remote
)
from charts import approved_by_area

def layout():
    df = read_data()

    st.markdown("# YH dashboard 2024 applications")

    st.markdown(
        "This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard."
    )

    st.markdown("## KPIs in Sweden")

    labels = (
        "Total application"
        , "Number approved"
        , "Approved percentage"
        , "Remote education"
        , "Approved remote"
    )

    kpis = (
        total_application
        , number_approved
        , approved_percentage
        , number_distance
        , approved_remote
    )

    cols = st.columns(5)
    
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label = label, value = kpi)


    st.markdown("## Approved educations per area")

    approved_by_area()

    st.markdown("## Simple statistic on given provider")
    st.markdown("Search for education provider")

    provider = st.selectbox(
        "Search a provider",
        df["Utbildningsanordnare administrativ enhet"].unique()
    )

    applications, approved_applications = provider_kpis(provider)

    st.markdown(f"This educational provider {provider} has applied for {applications} educations and gotten {approved_applications} approved.")

    st.markdown("## Raw data")

    st.dataframe(df)


if __name__ == "__main__":
    layout()