# agents/report_writer.py
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def create_report_writer_agent():
    """Creates an agent that compiles the final investment report."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert financial report writer. Your task is to synthesize the quantitative and qualitative analyses into a single, comprehensive, and well-structured investment report. The report should be clear, concise, and provide a final recommendation."),
        ("human", "Please compile a final investment report based on the following analyses:\n\nQuantitative Analysis:\n{quant_analysis}\n\nQualitative Analysis:\n{qual_analysis}\n\nBased on all this information, conclude with a final investment recommendation (e.g., 'Strong Buy', 'Buy', 'Hold', 'Sell', 'Strong Sell') and a brief justification for your recommendation."),
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    return prompt | llm