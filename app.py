from dotenv import load_dotenv

load_dotenv()

from agents import Agents
from tasks import ResearchTasks
from crewai import Crew


def run(city, timing):
    agents = Agents()
    tasks = ResearchTasks()

    # AGENTS
    planner = agents.planner()
    researcher = agents.researcher()

    # TASKS
    research = tasks.manage_event_and_places(city, researcher, timing)
    plan = tasks.create_plan(city, planner, timing)

    # CREW
    crew = Crew(
        agents=[planner, researcher],
        tasks=[research, plan],
        verbose=True,
    )

    result = crew.kickoff()
    return result
