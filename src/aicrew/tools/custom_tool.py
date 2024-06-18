from aicrew.utils.qdrant_singleton import QdrantSingleton
from crewai_tools import BaseTool

class RetrieverTool(BaseTool):
    name: str = "Retrieving Service Examples Tool"
    description: str = "Based on question parameter, it searches for the best examples of similar services through a vector database."

    def _run(self, question: str) -> str:
        """
        Retrieves information about applications based on user's question.

        Args:
        - question (str): The question asked by the user about applications.

        Returns:
        - str: Information or response based on the user's question.
        """
        
        try:
            return QdrantSingleton.get_instance().select_examples(question=question, k=2)
        except Exception as e:
            return f"Unable to retrieve application information: {e}"