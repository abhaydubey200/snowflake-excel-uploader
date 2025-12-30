---

# 📊 Excel to Snowflake Data Loader (Streamlit App)

A **production-ready web application** that allows users to upload Excel files and seamlessly load data into **Snowflake Data Warehouse** using **Python, Streamlit, and Pandas**. This project demonstrates a real-world **ETL pipeline** suitable for enterprise data ingestion.

---

## 🚀 Project Overview

This application simplifies data ingestion for business users and data engineers by allowing **Excel uploads through a web interface**, automatically processing and loading data into Snowflake tables with:

* **Automatic data cleaning**
* **Validation and error handling**
* **Scalable bulk loading**
* **Enterprise-grade Snowflake integration**

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Data Processing**: Pandas
* **Data Warehouse**: Snowflake

---

## ✨ Key Features

### 🔹 User-Friendly Interface

* Interactive Streamlit UI for uploading Excel files
* Real-time success and error notifications

### 🔹 Excel File Support

* Accepts `.xlsx` files
* Supports large datasets efficiently
* Automatic conversion to Pandas DataFrame

### 🔹 Automatic Data Cleaning

* Column names normalized to Snowflake-compatible format

  * Uppercase
  * Underscore-separated
* Missing values handled (`NULL`)
* Prevents invalid identifier errors

### 🔹 Snowflake Integration

* Secure connection to Snowflake
* Uses **COPY INTO** command for bulk loading
* Supports **internal staging** for high-performance ingestion

### 🔹 Error Handling & Fault Tolerance

* Invalid rows do not stop the load
* Partial loads are supported
* Automatic handling of duplicates, missing columns, and null values

### 🔹 Secure & Modular Design

* Separate Snowflake connection logic
* Config-driven credentials (supports environment variables)
* Clean and maintainable code structure

### 🔹 Automation & Scalability

* Can be scheduled or triggered for regular uploads
* Scales to enterprise datasets
* Supports multiple tables and schemas

### 🔹 Logging & Notifications

* Logs success and failure of every upload
* Optional email or Streamlit notifications for errors

### 🔹 Extensibility

* Easily extendable to support CSV, JSON, or multiple file formats
* Can integrate with dashboards or BI tools

---

## 📂 Project Structure

```
snowflake-excel-uploader/
│
├── app.py                 # Main Streamlit application
├── snowflake_conn.py      # Snowflake connection logic
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore
```

---

## 🔮 Future Enhancements

* Column mapping UI for custom field mapping
* Multi-file upload support
* Advanced validation rules
* Role-based access control
* Load history & audit logging

---

## 📝 Summary

A **full-fledged ETL solution** that simplifies Excel-to-Snowflake ingestion with automation, validation, error handling, and scalability, making it ideal for enterprise-level data pipelines.

---


