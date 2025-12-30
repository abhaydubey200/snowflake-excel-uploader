import streamlit as st
import pandas as pd
from snowflake_client import get_snowflake_connection
from data_utils import clean_dataframe

st.set_page_config(page_title="Snowflake Excel Uploader", layout="wide")

st.title(" Excel to Snowflake Uploader")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

table_name = st.text_input("Target Snowflake Table", value="OUTLET_MASTER")

if uploaded_file and st.button("Upload to Snowflake"):
    try:
        df = pd.read_excel(uploaded_file)
        df = clean_dataframe(df)

        conn = get_snowflake_connection()
        cursor = conn.cursor()

        # Create TEMP stage
        cursor.execute("CREATE OR REPLACE TEMP STAGE excel_stage")

        # Save CSV
        csv_path = "/tmp/upload.csv"
        df.to_csv(csv_path, index=False)

        # Upload to stage
        cursor.execute(f"PUT file://{csv_path} @excel_stage OVERWRITE = TRUE")

        # COPY INTO 
        copy_sql = f"""
        COPY INTO {table_name}
        FROM @excel_stage/upload.csv
        FILE_FORMAT = (
            TYPE = CSV
            SKIP_HEADER = 1
            FIELD_OPTIONALLY_ENCLOSED_BY = '"'
        )
        ON_ERROR = 'CONTINUE';
        """

        cursor.execute(copy_sql)

        st.success(" Data successfully loaded into Snowflake")

    except Exception as e:
        st.error(f" Error: {e}")

