from textwrap import dedent

from aicrew.crew import AicrewCrew

if __name__ == "__main__":
    print("Welcome")
    question = input(dedent("""
        What services would you like to create?"""))
    
    my_crew = AicrewCrew(question=question)
    result = my_crew.run()
    print("########################################")
    print("RESULT:")
    print(result)
