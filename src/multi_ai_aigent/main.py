from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from crews.input_analysis_crew.input_analysis_crew import InputAnalysisCrew
from crews.paper_search_crew.paper_search_crew import PaperSearchCrew
from crews.news_crew.news_crew import NewsCrew
import os
import agentops
from datetime import datetime
load_dotenv()


class UserInput(BaseModel):
    user_input: str = ""
    date: str = ""
    keywords: str = ""

class UserInputFlow(Flow[UserInput]):

    @start()
    def input_analysis(self):
        crew = InputAnalysisCrew()
        user_input = input("무엇을 원하시나요?: ")
        inputs = {"user_input": user_input, "date": datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}
        keywords = crew.crew().kickoff(inputs=inputs)
        print(keywords)
        self.state.user_input = user_input
        self.state.date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.state.keywords = keywords
        print(f"self.state: {self.state.keywords}")


    @listen(input_analysis)
    def paper_search(self):
        crew = PaperSearchCrew()
        inputs = {"keywords": self.state.keywords, "date": self.state.date, "user_input": self.state.user_input}
        papers = crew.crew().kickoff(inputs=inputs)
        print(papers)

    @listen(input_analysis)
    def news_search(self):
        crew = NewsCrew()
        inputs = {"keywords": self.state.keywords, "date": self.state.date, "user_input": self.state.user_input}
        news = crew.crew().kickoff(inputs=inputs)
        print(news)

def kickoff():
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))
    user_input_flow = UserInputFlow()
    user_input_flow.plot()
    user_input_flow.kickoff()
    session.end_session()

if __name__ == "__main__":
    kickoff()
