from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.custom_tools import SearchArxivTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class PaperSearchCrew():
	"""PaperSearchCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def research_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['research_analyzer'],
			verbose=True,
		)

	@agent
	def paper_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['paper_searcher'],
			verbose=True,
			tools=[SearchArxivTool()]
		)

	@task
	def research_analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_analyzer_task'],
		)

	@task
	def paper_searcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['paper_searcher_task'],
		)
		

	@crew
	def crew(self) -> Crew:
		"""Creates the PaperSearchCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
	
	