# app.py
import streamlit as st
from dotenv import load_dotenv
from graph import app_graph # Import the compiled graph

# Load environment variables from .env file
load_dotenv()

st.set_page_config(layout="wide")
st.title("Multi-Agent Financial Analyst 📈")
st.write("Enter a stock symbol and a company name to start the automated analysis. The process involves multiple AI agents and may take a few minutes.")

# --- User Input ---
stock_symbol = st.text_input("Stock Symbol (e.g., 'GOOGL', 'TSLA')", "TSLA")
company_name = st.text_input("Company Name (for news search)", "Tesla Inc.")

if st.button("Generate Investment Report"):
    if stock_symbol and company_name:
        with st.spinner("The multi-agent system is running... Agents are collaborating to generate your report."):
            try:
                # Define the initial state to pass to the graph
                initial_state = {
                    "company_name": company_name,
                    "symbol": stock_symbol,
                    "messages": [], # Not used in this linear graph, but required by the state
                }
                
                # The .stream() method executes the graph and yields the state at each step.
                # We are interested in the final result.
                # A more advanced UI could show progress at each node.
                final_state = app_graph.invoke(initial_state)
                
                # Extract the final report from the state
                final_report = final_state.get("final_report", "No report generated.")
                
                st.success("Analysis complete!")
                
                # Display the final report
                st.markdown("---")
                st.header("Generated Investment Report")
                st.markdown(final_report)

            except Exception as e:
                st.error(f"An error occurred during the agent run: {e}")
    else:
        st.warning("Please provide both a stock symbol and a company name.")