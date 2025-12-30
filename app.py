import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

st.set_page_config(page_title="Excel to Snowflake Uploader", layout="wide")
st.title(" Excel → Snowflake Uploader")

SNOWFLAKE_USER = st.secrets["SNOWFLAKE_USER"]
SNOWFLAKE_PASSWORD = quote_plus(st.secrets["SNOWFLAKE_PASSWORD"])
SNOWFLAKE_ACCOUNT = st.secrets["SNOWFLAKE_ACCOUNT"]
SNOWFLAKE_WAREHOUSE = st.secrets["SNOWFLAKE_WAREHOUSE"]
SNOWFLAKE_DATABASE = st.secrets["SNOWFLAKE_DATABASE"]
SNOWFLAKE_SCHEMA = st.secrets["SNOWFLAKE_SCHEMA"]
TABLE_NAME = "OUTLET_MASTER"

engine = create_engine(
    f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}"
    f"@{SNOWFLAKE_ACCOUNT}/{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}"
    f"?warehouse={SNOWFLAKE_WAREHOUSE}"
)

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Excel loaded successfully")
        st.dataframe(df.head())

        if st.button("Upload to Snowflake"):
            df = df.where(pd.notnull(df), None)

            df.to_sql(
                TABLE_NAME,
                engine,
                if_exists="append",
                index=False,
                method="multi",
                chunksize=1000
            )

            st.success(f" {len(df)} rows uploaded successfully")

    except Exception as e:
        st.error(f" Error: {e}")
