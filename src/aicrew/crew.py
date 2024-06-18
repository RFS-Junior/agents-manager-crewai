from aicrew.custom_agents import CustomAgent
from aicrew.custom_tasks import CustomTask
from crewai import Crew

class AicrewCrew:
    def __init__(self, question):
        self.question = question

    def run(self):
        agents = CustomAgent(question=self.question)
        tasks = CustomTask(question=self.question)
  
        agent1 = agents.first_agent()
        agent2 = agents.second_agent()
  
        task1 = tasks.fisrt_task(agent=agent1)
        task2 = tasks.second_task(agent=agent2)

        crew = Crew(
            agents=[agent1, agent2],
            tasks=[task1, task2],
            verbose=True,
        )

        result = crew.kickoff()
        return result