# DeepdiverCrew Crew

## Development Setup

Create and activate a virtual environment using `uv`
Python Version 3.12

```bash
uv venv --python=python3.12
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Install crewai and crewai-tools

```bash
uv pip install crewai crewai-tools
```

Create a Crew or Flow

```bash
crewai create crew <crew_name>
crewai create flow <flow_name>
```

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
cd deepdiver_crew
crewai install
```

Run the crew

```bash
crewai run
```

### Customizing

Update .env
```bash
MODEL=gpt-4o-mini
OPENAI_API_KEY=<your-openai-api-key>
SERPER_API_KEY=<your-serper-api-key>
```

- Modify `src/deepdiver_crew/config/agents.yaml` to define your agents
- Modify `src/deepdiver_crew/config/tasks.yaml` to define your tasks
- Modify `src/deepdiver_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/deepdiver_crew/main.py` to add custom inputs for your agents and tasks
