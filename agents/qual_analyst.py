# agents/qual_analyst.py
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def create_qualitative_analyst_agent():
    """Creates an agent that analyzes news articles."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert qualitative financial analyst. Your task is to analyze the provided news articles about a company and identify the overall sentiment, key risk factors, and potential opportunities mentioned."),
        ("human", "Here are the recent news articles for the company:\n\n{news_data}\n\nPlease provide a qualitative analysis. Summarize the key news, determine the overall market sentiment (positive, negative, or neutral), and list any significant risks or opportunities discussed."),
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    # This agent also processes text
    return prompt | llm