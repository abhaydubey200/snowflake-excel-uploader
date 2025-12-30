import streamlit as st
import pandas as pd  
import sqlalchemy
from sqlalchemy.engine import create_engine


# ------------------ Streamlit Config ------------------
st.set_page_config(
    page_title="Excel to Snowflake Uploader",
    layout="wide"
)

st.title("📤 Excel to Snowflake Uploader")

# ------------------ Snowflake Secrets ------------------
SNOWFLAKE_USER = st.secrets["SNOWFLAKE_USER"]
SNOWFLAKE_PASSWORD = st.secrets["SNOWFLAKE_PASSWORD"]
SNOWFLAKE_ACCOUNT = st.secrets["SNOWFLAKE_ACCOUNT"]
SNOWFLAKE_WAREHOUSE = st.secrets["SNOWFLAKE_WAREHOUSE"]
SNOWFLAKE_DATABASE = st.secrets["SNOWFLAKE_DATABASE"]
SNOWFLAKE_SCHEMA = st.secrets["SNOWFLAKE_SCHEMA"]
TABLE_NAME = "OUTLET_MASTER"

# ------------------ Snowflake Engine ------------------
engine = create_engine(
    f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}@{SNOWFLAKE_ACCOUNT}/"
    f"{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}"
    f"?warehouse={SNOWFLAKE_WAREHOUSE}"
)

# ------------------ File Upload ------------------
uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.subheader("🔍 Preview Data")
        st.dataframe(df.head())

        # Deduplicate
        if "Stockist_Id" in df.columns:
            df = df.drop_duplicates(subset=["Stockist_Id"])

        # Handle NULLs
        df = df.where(pd.notnull(df), None)

        with engine.begin() as conn:
            df.to_sql(
                TABLE_NAME,
                con=conn,
                if_exists="append",
                index=False,
                method="multi"
            )

        st.success(f"✅ {len(df)} rows uploaded successfully")

    except Exception as e:
        st.error(f"❌ Error: {e}")

