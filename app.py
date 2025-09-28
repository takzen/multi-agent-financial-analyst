# app.py
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(layout="wide")
st.title("Multi-Agent Financial Analyst 📈")
st.write("Enter a stock symbol and a company name to start the automated analysis.")

stock_symbol = st.text_input("Stock Symbol (e.g., 'GOOGL', 'TSLA')", "GOOGL")
company_name = st.text_input("Company Name (for news search)", "Alphabet Inc.")

if st.button("Generate Investment Report"):
    if stock_symbol and company_name:
        st.info("The multi-agent system has started the analysis. This may take a few minutes...")
        
        # Placeholder for the LangGraph execution logic
        st.warning("Agent system and LangGraph logic not yet implemented.")
    else:
        st.warning("Please provide both a stock symbol and a company name.")