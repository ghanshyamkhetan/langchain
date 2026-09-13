from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
    """
    print(f"Searching for {query}")
    #return "tokyo weather is sunny"
    return tavily.search(query=query)

llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite"
        )
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for dba jobs in bangalore")})
    print(result)


if __name__ == "__main__":
    main()