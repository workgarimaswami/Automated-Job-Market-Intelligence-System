import sys
import os
import streamlit as st
import pandas as pd

# ==============================
# Fix Python import path
# ==============================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraping.scrape_jobs import scrape_sap_jobs

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="AI Job Market Intelligence", layout="wide")

st.title("🤖 AI-Based Job Market Intelligence System")
st.subheader("Germany / EU Focus")

# ==============================
# Sidebar Controls
# ==============================
st.sidebar.header("Your Profile")

keyword = st.sidebar.text_input("Search keyword", "ai")
pages = st.sidebar.slider("Pages to scrape", 1, 5, 1)

if st.sidebar.button("🔄 Scrape Latest SAP Jobs"):
    with st.spinner("Scraping SAP jobs..."):
        count = scrape_sap_jobs(keyword, pages)

    if count > 0:
        st.success(f"Scraped {count} jobs successfully!")
    else:
        st.error("No jobs scraped.")

# ==============================
# Load scraped data safely
# ==============================
st.divider()
st.subheader("📄 Latest Scraped Jobs")

if os.path.exists("data/jobs_live.csv") and os.path.getsize("data/jobs_live.csv") > 0:
    jobs_df = pd.read_csv("data/jobs_live.csv")
    st.dataframe(jobs_df)
else:
    st.info("No scraped data available yet. Click 'Scrape Latest SAP Jobs'.")
