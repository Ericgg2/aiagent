from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class PaperSummarizer():
	"""PaperSummarizer crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def paper_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['paper_summarizer'],
			verbose=True,
			
		)


	@task
	def paper_summarizer_task(self) -> Task:
		return Task(
			config=self.tasks_config['paper_summarizer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PaperSummarizer crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
