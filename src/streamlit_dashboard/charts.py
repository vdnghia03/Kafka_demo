import streamlit as st
import duckdb
from read_data import read_data



def approved_by_area():
    df = read_data()

    df = duckdb.query(
        """
            SELECT 
                utbildningsområde, COUNT(*) as Beviljad
            FROM 
                df
            WHERE 
                beslut = 'Beviljad'
            GROUP BY
                utbildningsområde
            ORDER BY 
                Beviljad
            DESC 
        """
    ).df()

    st.bar_chart(df, x = "Utbildningsområde", y = "Beviljad")