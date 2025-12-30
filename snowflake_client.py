import snowflake.connector

def get_snowflake_connection():
    return snowflake.connector.connect(
        user="ABHAY2004",
        password="Abhay@7505991639",
        account="VKOZIAJ-KC24613",
        warehouse="COMPANY_WH",
        database="BIZOM_DB",
        schema="OUTLET_SCHEMA",
        role="PUBLIC"
    )
