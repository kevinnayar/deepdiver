# Deepdiver

## Development Setup

Create and activate a virtual environment using `uv`
Python Version 3.12

```bash
uv venv --python=python3.12
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Install `crewai` and `crewai-tools`

```bash
uv pip install crewai crewai-tools
```

(Optional) Lock the dependencies and install them
```bash
cd deepdiver_crew
crewai install
```

Copy the sample.env file to .env
```bash
cd deepdiver_crew
cp sample.env .env
```

Update the .env file with your own OpenAI and Serper API keys
```bash
MODEL=gpt-4o-mini
OPENAI_API_KEY=<your-openai-api-key>
SERPER_API_KEY=<your-serper-api-key>
```

Run the crew
```bash
crewai run
```

### Customizing

- Modify `src/deepdiver_crew/config/agents.yaml` to define your agents
- Modify `src/deepdiver_crew/config/tasks.yaml` to define your tasks
- Modify `src/deepdiver_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/deepdiver_crew/main.py` to add custom inputs for your agents and tasks
