# AicrewCrew: Custom AI Crew Management System

Welcome to AicrewCrew! This repository contains a Python implementation for managing a custom AI crew to handle various tasks based on a given question. The system leverages the power of custom agents and tasks to provide tailored solutions.

## Introduction

AicrewCrew streamlines the process of managing AI agents and tasks. It allows the creation of specialized agents and the definition of tasks to address complex questions effectively.

## Features

- **Custom Agents**: Configure AI agents with specific roles and goals.
- **Custom Tasks**: Define tasks with detailed descriptions and expected outputs.
- **Qdrant Integration**: Efficient vector-based storage and retrieval of data.
- **Flexible Configuration**: Easily configure various components like Qdrant connection, models, and embeddings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aicrewcrew.git
   cd aicrewcrew
   ```

2. Install [Poetry](https://python-poetry.org/docs/#installation).

3. Create and activate a virtual environment:
   ```bash
   poetry shell
   ```

4. Install dependencies:
   ```bash
   poetry install
   ```

5. Set up environment variables in a `.env` file:
   ```env
   QDRANT_URL=your_qdrant_url
   QDRANT_PORT=your_qdrant_port
   COLLECTION_NAME=your_collection_name
   ```

## Configuration

### Qdrant Configuration

Edit the `QdrantConfig` class in `qdrant_config.py`:

```python
class QdrantConfig:
    URL = "your_qdrant_url"
    PORT = 6333
    COLLECTION_NAME = "your_collection_name"
    VECTOR_SIZE = 1536
    DISTANCE = Distance.COSINE
```

### Custom Agents and Tasks

Modify the `CustomAgent` and `CustomTask` classes in `custom_agents.py` and `custom_tasks.py`.

## Contributing

We welcome contributions! Open an issue or submit a pull request for suggestions or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

We hope you find AicrewCrew useful! For questions or further assistance, feel free to reach out. Happy coding!