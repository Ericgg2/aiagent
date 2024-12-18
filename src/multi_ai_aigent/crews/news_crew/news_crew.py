from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class NewsCrew():
	"""NewsCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def user_input_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['user_input_analyzer'],
			verbose=True,
		)

	@agent
	def news_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['news_researcher'],
			verbose=True,
			tools=[SerperDevTool()]
		)
	
	@agent
	def news_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['news_scraper'],
			verbose=True,
			tools=[ScrapeWebsiteTool()]
		)
	
	@agent
	def news_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['news_summarizer'],
			verbose=True,
		)

	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			verbose=True,
			tools=[FileWriterTool()]
		)

	@task
	def user_input_analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['user_input_analyzer_task'],
		)

	@task
	def news_researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['news_researcher_task'],
			
		)
	
	@task
	def news_scraper_task(self) -> Task:
		return Task(
			config=self.tasks_config['news_scraper_task'],
			
		)

	@task
	def news_summarizer_task(self) -> Task:
		return Task(
			config=self.tasks_config['news_summarizer_task'],
		)

	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the NewsCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
