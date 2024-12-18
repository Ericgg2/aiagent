from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class InputAnalysisCrew():
	"""InputAnalysisCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def research_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['research_analyzer'],
			verbose=True,
		)
	@task
	def research_analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_analyzer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the InputAnalysisCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
