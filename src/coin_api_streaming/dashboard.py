import streamlit as st
from streamlit_autorefresh import st_autorefresh
from sqlalchemy import create_engine
import pandas as pd

from constants import (
    POSTGRES_DB
    , POSTGRES_HOST
    , POSTGRES_PASSWORD
    , POSTGRES_PORT
    , POSTGRES_USER
)

from charts import line_chart

connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(connection_string)

def load_data(query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        df = df.set_index("timestamp")

        return df


count = st_autorefresh(interval = 10 * 1000, limit = 100, key = "data_refresh")

def layout():
    df = load_data("SELECT * FROM bitcoin;")

    st.markdown("# Bitcoin data")
    st.markdown("This will display live data from coinmarket API")

    st.markdown("Latest data")

    st.dataframe(df.tail())

    st.markdown("## Bitcoin latest price in USD")

    price_chart = line_chart(x = df.index, y = df["price_usd"], title = "price USD")

    st.pyplot(price_chart, bbox_inches = "tight")


if __name__ == "__main__":
    layout()