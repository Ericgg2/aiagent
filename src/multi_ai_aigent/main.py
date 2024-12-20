from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start,router
from dotenv import load_dotenv
from crews.input_analysis_crew.input_analysis_crew import InputAnalysisCrew
from crews.paper_search_crew.paper_search_crew import PaperSearchCrew
from crews.news_crew.news_crew import NewsCrew
from crews.paper_summarizer.paper_summarizer import PaperSummarizer
import os
import agentops
import tempfile
import requests
import PyPDF2
from datetime import datetime
from divide import split_and_save_sections_by_keywords
import json

load_dotenv()


class UserInput(BaseModel):
    user_input: str = ""
    date: str = ""
    keywords: str = ""
    category: str = ""
    papers_info: dict = {
    }
    # papers_url: list = ['http://arxiv.org/pdf/2402.03328v2']

def download_and_parse_pdf(url):
    # 임시 파일로 다운로드
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_file:
        response = requests.get(url)
        temp_file.write(response.content)
        temp_file.seek(0)
        
        # PDF 파싱
        reader = PyPDF2.PdfReader(temp_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            
    return text





class UserInputFlow(Flow[UserInput]):

    @start()
    def input_analysis(self):
        crew = InputAnalysisCrew()
        user_input = input("무엇을 원하시나요?: ")
        inputs = {"user_input": user_input, "date": datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}
        category = crew.crew().kickoff(inputs=inputs)
        print(f"category: {type(category)}")
        self.state.category = category
        self.state.user_input = user_input
        self.state.date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    @router(input_analysis)
    def category_router(self):
        category = str(self.state.category).strip()
        print(f"category type: {type(category)}")
        print(f"category value: {category}")
        
        if category == "paper_search":
            print("paper_search")
            return "paper_search_go"
        elif category == "news_search":
            print("news_search")
            return "news_search_go"
        elif category == "keyword_search":
            return "keyword_search_go"
        else:
            return "failed"

    @listen("paper_search_go")
    def paper_search(self):
        crew = PaperSearchCrew()
        inputs = {"date": self.state.date, "user_input": self.state.user_input}
        papers_result = crew.crew().kickoff(inputs=inputs)
        
        # 디버깅을 위한 출력
        print("Papers result type:", type(papers_result))
        print("Papers result content:", papers_result)
        print("Papers result raw:", getattr(papers_result, 'raw', None))
        print("Papers result content:", getattr(papers_result, 'content', None))
        
        # CrewOutput 처리
        if hasattr(papers_result, 'content') and papers_result.content:
            # content 속성이 있고 비어있지 않은 경우
            papers_dict = papers_result.content
        elif hasattr(papers_result, 'raw') and papers_result.raw:
            # raw 속성에서 파이썬 딕셔너리 문자열 찾기
            raw_text = papers_result.raw
            # ```python과 ``` 마커 제거
            raw_text = raw_text.replace('```python', '').replace('```', '').strip()
            try:
                papers_dict = eval(raw_text)  # 파이썬 딕셔너리 문자열 평가
            except:
                try:
                    papers_dict = json.loads(raw_text)  # JSON 문자열 파싱
                except:
                    print(f"Error: Could not parse papers result: {raw_text}")
                    papers_dict = {"papers": []}
        else:
            papers_dict = {"papers": []}
        
        self.state.papers_info = papers_dict
        print(f"paper_search done results: {self.state.papers_info}")
        
        # 결과 검증
        if not self.state.papers_info.get('papers'):
            print("Warning: No papers found in the result")

    @listen("paper_search")
    def paper_summarizer(self):
        """논문 요약 처리를 위한 메인 함수"""
        crew = PaperSummarizer()
        self.state.date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        if not isinstance(self.state.papers_info, dict) or 'papers' not in self.state.papers_info:
            print("Error: Invalid papers_info format")
            return []
        
        for paper_info in self.state.papers_info['papers']:
            self._process_single_paper(paper_info, crew)

    def _process_single_paper(self, paper_info: dict, crew: PaperSummarizer):
        """단일 논문 처리 및 요약"""
        # 기본 정보 추출
        text = download_and_parse_pdf(paper_info['url'])
        title = paper_info['title'][:10]
        date = paper_info['date']
        print(f"Processing paper: {title}")
        
        # 섹션 분리
        split_and_save_sections_by_keywords(text, title, self.state.date)
        
        # 섹션별 요약 생성
        summaries = self._process_sections(title, date, crew)
        
        # 요약 저장
        self._save_summaries(summaries, title, date)

    def _process_sections(self, title: str, date: str, crew: PaperSummarizer) -> list:
        """논문의 각 섹션을 처리하고 요약"""
        summaries = []
        sections_dir = os.path.join(self.state.date, title, "sections")
        
        if not os.path.exists(sections_dir):
            print(f"Warning: Sections directory not found: {sections_dir}")
            return summaries
        
        for file in os.listdir(sections_dir):
            summary = self._process_single_section(file, sections_dir, date, crew)
            if summary:
                summaries.append((file, summary))
        
        return summaries

    def _process_single_section(self, file: str, sections_dir: str, date: str, crew: PaperSummarizer):
        """단일 섹션 처리 및 요약"""
        file_path = os.path.join(sections_dir, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                print(f"Processing section {file}: {len(text)} characters")
            
            inputs = {
                "file": file,
                "text": text,
                "date": date,
                "current_date": self.state.date
            }
            return crew.crew().kickoff(inputs=inputs)
        
        except Exception as e:
            print(f"Error processing section {file}: {str(e)}")
            return None

    def _save_summaries(self, summaries: list, title: str, date: str):
        """생성된 요약을 파일로 저장"""
        if not summaries:
            return
        
        summary_path = os.path.join(self.state.date, title, "summary.md")
        os.makedirs(os.path.dirname(summary_path), exist_ok=True)
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            for file, summary in summaries:
                section_name = os.path.splitext(file)[0].upper()
                f.write(f"## {section_name}\n\n")
                f.write(f"{summary.raw}\n\n")
                f.write("---\n\n")    

        

    @listen("news_search_go")
    def news_search(self):
        crew = NewsCrew()
        inputs = {"date": self.state.date, "user_input": self.state.user_input}
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
