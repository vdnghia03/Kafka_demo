import streamlit as st
from read_data import read_data
from kpis import number_approved, total_application, approved_percentage

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
    )

    kpis = (
        total_application
        , number_approved
        , approved_percentage
    )

    cols = st.columns(3)
    
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label = label, value = kpi)

    st.markdown("## Raw data")

    st.dataframe(df)


if __name__ == "__main__":
    layout()