from textwrap import dedent
from aicrew.tools.custom_tool import RetrieverTool
from crewai import Agent
from langchain_openai import ChatOpenAI

class CustomAgent:
    def __init__(self, question):
        self.question = question
        self.llm = ChatOpenAI(model="") #ADD YOUR FAVORITE MODEL

    def first_agent(self):
        retrieverTool = RetrieverTool()
        return Agent(
            role="Agent specialized in ...",
            backstory=dedent(
                """Specialized in ..."""),
            goal=dedent(
                """ ... """),
            tools=[retrieverTool],
            verbose=True,
            llm=self.llm,
        )

    def second_agent(self):
        return Agent(
            role="Agent specialized in ...",
            backstory=dedent(
                """Specialized in ..."""),
            goal=dedent(
                """ ... """),
            verbose=True,
            llm=self.llm,
        )
