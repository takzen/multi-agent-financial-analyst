# agents/data_fetcher.py
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.financial_tools import get_stock_price, get_recent_news

def create_data_fetcher_agent():
    """Creates an agent responsible for fetching initial data."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert data fetching agent. Your job is to use the available tools to get stock prices and recent news for a given company."),
        ("human", "Fetch the necessary data for the company: {company_name} (Symbol: {symbol})"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    tools = [get_stock_price, get_recent_news]
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)