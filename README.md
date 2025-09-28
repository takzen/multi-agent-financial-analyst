# Multi-Agent Financial Analyst (LangGraph & Gemini Pro)

### A multi-agent system powered by LangGraph and Google's Gemini 2.5 Pro that autonomously researches a given stock, performs quantitative and qualitative analysis, and generates a comprehensive investment report.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-orange?logo=streamlit) ![LangGraph](https://img.shields.io/badge/LangGraph-0.6.7-purple) ![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green) ![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Pro-blue?logo=google-gemini)

## 🚀 Overview

This project showcases an advanced implementation of a **multi-agent system**, a sophisticated AI architecture where multiple specialized agents collaborate to solve a complex problem. The application takes a stock symbol as input and orchestrates a team of AI agents to perform a comprehensive financial analysis.

The system is built using **LangGraph**, a library for building stateful, multi-agent applications. It demonstrates an advanced understanding of agent-based architectures, state management, and workflow orchestration in Generative AI.

## ✨ Key Features & Architecture

The application is composed of a team of four distinct agents working in a sequence:

1.  **Data Fetcher Agent:** Equipped with tools to access real-time financial data and news from external APIs (**Alpha Vantage** and **NewsAPI**).
2.  **Quantitative Analyst Agent:** Processes the fetched numerical stock data to identify key metrics, trends, and statistical insights.
3.  **Qualitative Analyst Agent:** Analyzes recent news articles to gauge market sentiment and identify qualitative risks and opportunities.
4.  **Report Writer Agent:** The final agent in the chain, responsible for synthesizing the analyses from the other agents into a single, coherent, and well-structured investment report.

### Core Techniques Demonstrated:

*   **Multi-Agent Systems with LangGraph:** The entire workflow is defined as a stateful graph where each agent is a node. This showcases the ability to design and build complex, state-driven AI systems.
*   **Tool-Using Agents:** The Data Fetcher agent demonstrates practical tool use, a fundamental concept in building capable AI agents that can interact with external systems.
*   **Orchestration and State Management:** LangGraph is used to manage the flow of data (`AgentState`) between agents, ensuring that the output of one agent becomes the input for the next.
*   **End-to-End System Design:** From a user-facing **Streamlit** interface to a complex, multi-step backend, this project demonstrates the full lifecycle of building an advanced AI product.

## 🛠️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/takzen/multi-agent-financial-analyst.git
    cd multi-agent-financial-analyst
    ```

2.  **Set up API Keys:**
    *   Create a file named `.env` in the root of the project.
    *   Add your API keys to this file:
        ```        
        GOOGLE_API_KEY="YOUR_GOOGLE_AI_KEY"
        ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_KEY"
        NEWS_API_KEY="YOUR_NEWS_API_KEY"
        ```

3.  **Create a virtual environment and install dependencies:**
    *   This project requires Python 3.9+. Create a virtual environment (`uv venv`).
    *   Install the required packages:
        ```bash
        uv pip install streamlit python-dotenv langchain langchain-google-genai langgraph langchain_community alpha_vantage newsapi-python
        ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## 🖼️ Showcase

| 1. User Input                                        | 2. Final AI-Generated Report                             |
| :--------------------------------------------------- | :------------------------------------------------------- |
| ![User Input](images/01_user_input.png)              | ![Agent Report](images/02_final_report.png)              |
| *The user provides a stock symbol and company name to initiate the analysis.* | *The multi-agent system generates and displays a comprehensive investment report.* |