# agents/quant_analyst.py
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def create_quantitative_analyst_agent():
    """Creates an agent that analyzes stock price data."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert quantitative financial analyst. Your task is to analyze the provided stock price data and provide a summary of key metrics and trends. Focus on numbers and objective analysis."),
        ("human", "Here is the stock price data for the company:\n\n{stock_data}\n\nPlease provide a quantitative analysis. Identify the current price, the 52-week high and low if available, and any notable recent trends (e.g., is the stock price increasing or decreasing?)."),
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    # This agent doesn't need tools, it just processes text
    return prompt | llm