from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()  # Load environment variables from .env file



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Singapore on linkedin and list their details")})
    print(f"Agent's response: {result}")


if __name__ == "__main__":
    main()
