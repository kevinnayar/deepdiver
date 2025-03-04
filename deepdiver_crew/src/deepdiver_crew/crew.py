from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
scrape_website_tool = ScrapeWebsiteTool()


@CrewBase
class DeepdiverCrew:
    """DeepdiverCrew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs

    @after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            verbose=True,
            tools=[web_search_tool, serper_dev_tool, scrape_website_tool],
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            verbose=True,
        )

    @task
    def write_tldr_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_tldr_task"],
        )

    @task
    def write_eli5_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_eli5_task"],
        )

    @task
    def write_technical_deepdive_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_technical_deepdive_task"],
        )

    @task
    def edit_article_task(self) -> Task:
        return Task(
            config=self.tasks_config["edit_article_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DeepdiverCrew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
