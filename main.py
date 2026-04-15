from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage


load_dotenv()  # Load environment variables from .env file

def search_web(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching the web for: {query}")
    return "Tokyo weather is sunny"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [search_web]
agent = create_agent(model=llm, tools=tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    print(f"Agent's response: {result}")


if __name__ == "__main__":
    main()
