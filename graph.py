# graph.py
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage
import operator
from langgraph.graph import StateGraph, END

# Import all agent creation functions and node functions
from agents.data_fetcher import create_data_fetcher_agent
from agents.quant_analyst import create_quantitative_analyst_agent
from agents.qual_analyst import create_qualitative_analyst_agent
from agents.report_writer import create_report_writer_agent
from tools.financial_tools import get_stock_price, get_recent_news

class AgentState(TypedDict):
    """
    Represents the state of our multi-agent system.
    This state is passed between nodes in the graph.
    """
    company_name: str
    symbol: str
    stock_data: str
    news_data: str
    quant_analysis: str
    qual_analysis: str
    final_report: str
    # 'messages' is not used in this linear graph but is good practice for more complex agents
    messages: Annotated[List[BaseMessage], operator.add]

# --- Agent Node Definitions ---

def data_fetcher_node(state: AgentState):
    """
    Node for the data fetching agent. This node calls the tools directly for simplicity and reliability.
    """
    print("--- 1. Fetching Data ---")
    company_name = state["company_name"]
    symbol = state["symbol"]
    
    # Call tools directly to get structured data
    stock_data = get_stock_price.invoke(symbol)
    news_data = get_recent_news.invoke(company_name)
    
    return {"stock_data": stock_data, "news_data": news_data}

def quantitative_analyst_node(state: AgentState):
    """Node for the quantitative analyst agent."""
    print("--- 2. Analyzing Quantitative Data ---")
    quant_analyst_chain = create_quantitative_analyst_agent()
    result = quant_analyst_chain.invoke({"stock_data": state["stock_data"]})
    return {"quant_analysis": result.content}

def qualitative_analyst_node(state: AgentState):
    """Node for the qualitative analyst agent."""
    print("--- 3. Analyzing Qualitative Data ---")
    qual_analyst_chain = create_qualitative_analyst_agent()
    result = qual_analyst_chain.invoke({"news_data": state["news_data"]})
    return {"qual_analysis": result.content}

def report_writer_node(state: AgentState):
    """Node for the report writer agent."""
    print("--- 4. Compiling Final Report ---")
    report_writer_chain = create_report_writer_agent()
    result = report_writer_chain.invoke({
        "quant_analysis": state["quant_analysis"],
        "qual_analysis": state["qual_analysis"]
    })
    return {"final_report": result.content}


# --- Graph Definition and Compilation ---

# Define the workflow graph
workflow = StateGraph(AgentState)

# Add the nodes to the graph
workflow.add_node("data_fetcher", data_fetcher_node)
workflow.add_node("quantitative_analyst", quantitative_analyst_node)
workflow.add_node("qualitative_analyst", qualitative_analyst_node)
workflow.add_node("report_writer", report_writer_node)

# Define the edges that connect the nodes in a linear sequence
workflow.add_edge("data_fetcher", "quantitative_analyst")
workflow.add_edge("quantitative_analyst", "qualitative_analyst")
workflow.add_edge("qualitative_analyst", "report_writer")
workflow.add_edge("report_writer", END) # The final node connects to the end

# Set the entry point for the graph
workflow.set_entry_point("data_fetcher")

# Compile the graph into a runnable LangChain object
app_graph = workflow.compile()