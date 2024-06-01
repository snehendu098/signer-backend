from crewai import Agent
from langchain_google_genai import GoogleGenerativeAI
from textwrap import dedent
from crewai_tools import SerperDevTool


class Agents:
    def __init__(self):
        self.llm = GoogleGenerativeAI(model="gemini-pro")
        self.searchTool = SerperDevTool()

    def planner(self):
        return Agent(
            role="Planner Agent",
            goal="Make a structured report for the petitioners about where they can go. Give the work to the Researcher Agent accordingly so that most accurate results can be found out",
            backstory="You are a creative thinker and has proper knowledge of locations of a city. You create structured report for people so that they can go out of their home and then get signatures from people",
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
            tools=[self.searchTool],
        )

    def researcher(self):
        return Agent(
            role="Researcher Agent",
            goal="Find out the best events that are happing in a certain place at a certain time",
            backstory="You are an agent who contacts petitoners on a daily basis. Petetioners need the data for the latest events that will be happening in the place given my them. You have more than 30 years of experience in this industry and you know which events are best for petitoners so that they can get signatures of maximum number of people possible",
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            tools=[self.searchTool],
        )
