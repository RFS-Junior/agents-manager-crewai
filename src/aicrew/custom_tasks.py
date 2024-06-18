from textwrap import dedent
from crewai import Task

class CustomTask:
    def __init__(self, question):
        self.question = question

    def fisrt_task(self, agent):
        return Task(
            description=dedent(
                f"""**Task**: ...
                **Description**: ...
                **Parameter**:
                - input: {self.question}"""),
            expected_output='A list in JSON format',
            agent=agent,
        )
    
    def second_task(self, agent):
        return Task(
            description=dedent(
                f"""**Task**: ...
                **Description**: ...

                **Parameter**:
                - input: {self.question}"""),
            expected_output='A entity in JSON format',
            agent=agent,
        )
