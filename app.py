import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

SNOWFLAKE_USER = "ABHAY2004"
SNOWFLAKE_PASSWORD = "Abhay@7505991639"   
SNOWFLAKE_ACCOUNT = "VKOZIAJ-KC24613"
SNOWFLAKE_WAREHOUSE = "COMPANY_WH"
SNOWFLAKE_DATABASE = "BIZOM_DB"
SNOWFLAKE_SCHEMA = "OUTLET_SCHEMA"
TABLE_NAME = "OUTLET_MASTER"

st.set_page_config(page_title="Excel → Snowflake Uploader", layout="wide")
st.title(" Excel to Snowflake Data Uploader")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Excel loaded successfully")
        st.dataframe(df.head())

        if st.button("Upload to Snowflake"):
            engine = create_engine(
                f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}"
                f"@{SNOWFLAKE_ACCOUNT}/{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}"
                f"?warehouse={SNOWFLAKE_WAREHOUSE}"
            )

            # Replace NaN with None
            df = df.where(pd.notnull(df), None)

            # Upload
            df.to_sql(
                TABLE_NAME,
                engine,
                if_exists="append",
                index=False,
                method="multi",
                chunksize=1000
            )

            st.success(f"✅ {len(df)} records uploaded successfully!")

    except Exception as e:
        st.error(f"❌ Error: {e}")

