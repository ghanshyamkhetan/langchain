from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


class Source(BaseModel):
    """Schema for a Source used by the agent """

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with anser and sources"""

    answer:str = Field(description="The agent's answer the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite"
        )
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for dba jobs in bangalore")})
    print(result)


if __name__ == "__main__":
    main()