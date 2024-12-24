from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start,router, or_
from dotenv import load_dotenv
from crews.input_analysis_crew.input_analysis_crew import InputAnalysisCrew
from crews.paper_search_crew.paper_search_crew import PaperSearchCrew
from crews.news_crew.news_crew import NewsCrew
from crews.paper_summarizer.paper_summarizer import PaperSummarizer
from crews.gmailcrew.gmailcrew import GmailCrew
import os
import agentops
import tempfile
import requests
import PyPDF2
from datetime import datetime
from divide import split_and_save_sections_by_keywords
import json
# from langgraph_chat import main

load_dotenv()


class UserInput(BaseModel):
    user_input: str = ""
    date: str = ""
    keywords: str = ""
    category: str = ""
    papers_info: dict = {
    }
    body: str = ""


def download_and_parse_pdf(url):
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered
    from marker.config.parser import ConfigParser
    from tempfile import NamedTemporaryFile

    # PDF 파일 경로 설정
    # tmp 디렉토리 생성
    tmp_dir = "./tmp"
    os.makedirs(tmp_dir, exist_ok=True)

    # PDF 다운로드
    response = requests.get(url)
    response.raise_for_status()  # HTTP 에러 발생 시 예외를 던짐

    # 임시 파일 생성
    with NamedTemporaryFile(delete=False, suffix=".pdf", dir=tmp_dir) as temp_pdf_file:
        temp_pdf_file.write(response.content)  # PDF 내용을 임시 파일에 저장
        temp_pdf_path = temp_pdf_file.name
    
    pdf_path = temp_pdf_path
    # PDF을 markdown 형태로 변환
    try:
        config = {
            "output_format": "markdown",
        }

        config_parser = ConfigParser(config)

        converter = PdfConverter(
            config=config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
            processor_list=config_parser.get_processors(),
            renderer=config_parser.get_renderer()
        )

        rendered = converter(pdf_path)
        text, metadata, images = text_from_rendered(rendered)

    # Markdown 파일 저장
        output_markdown_path = tmp_dir + f"/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.md"
        with open(output_markdown_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Markdown file saved at: {output_markdown_path}")
    # 파일 이름 및 경로 설정
        for name, image in images.items():
            image.save(os.path.join(tmp_dir, name), "JPEG")
            print(f"이미지가 {name}으로 저장되었습니다.")
        
        return text

    except Exception as e:
        print(f"Error during Markdown conversion: {e}")

        return ""

    



class UserInputFlow(Flow[UserInput]):

    @start()
    def input_analysis(self):
        crew = InputAnalysisCrew()
        user_input = input("무엇을 원하시나요?: ")
        inputs = {"user_input": user_input, "date": datetime.now().strftime("%Y-%m-%d")}
        category = crew.crew().kickoff(inputs=inputs)
        print(f"category: {type(category)}")
        self.state.category = category
        self.state.user_input = user_input
        self.state.date = datetime.now().strftime("%Y-%m-%d") 

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
        
        # CrewOutput을 딕셔너리로 변환
        if hasattr(papers_result, 'raw'):
            try:
                raw_text = papers_result.raw.replace('```python', '').replace('```', '').strip()
                papers_dict = eval(raw_text)
            except:
                print("Error: Could not parse papers result")
                papers_dict = {"papers": []}
        else:
            papers_dict = {"papers": []}
        
        # 검색된 논문 목록 출력
        print("\n=== 검색된 논문 목록 ===")
        for idx, paper in enumerate(papers_dict['papers'], 1):
            print(f"\n{idx}. 제목: {paper['title']}")
            print(f"   저자: {paper['authors']}")
            print(f"   날짜: {paper['date']}")
            print(f"   URL: {paper['url']}")
            print(f"   초록: {paper['abstract'][:200]}...")  # 초록은 일부만 표시
        
        # 사용자 선택 받기
        while True:
            try:
                selection = input("\n분석할 논문 번호를 선택하세요 (여러 개인 경우 쉼표로 구분, 예: 1,3): ").strip()
                if not selection:
                    print("선택된 논문이 없습니다. 다시 선택해주세요.")
                    continue
                    
                selected_indices = [int(idx.strip()) for idx in selection.split(',')]
                
                # 유효한 인덱스 확인
                if any(idx < 1 or idx > len(papers_dict['papers']) for idx in selected_indices):
                    print(f"1부터 {len(papers_dict['papers'])}까지의 숫자만 입력해주세요.")
                    continue
                    
                # 선택된 논문만 필터링
                selected_papers = {
                    "papers": [papers_dict['papers'][idx-1] for idx in selected_indices]
                }
                
                print("\n=== 선택된 논문 ===")
                for paper in selected_papers['papers']:
                    print(f"- {paper['title']}")
                
                self.state.papers_info = selected_papers
                print(f"\npaper_search done results: {self.state.papers_info}")
                break
                
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
            except Exception as e:
                print(f"오류가 발생했습니다: {str(e)}")
                print("다시 선택해주세요.")

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
        if text == "":
            print("Error: Could not download or parse PDF")
            return
        
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
        
        # 파일 목록을 가져와서 숫자 순서대로 정렬
        files = os.listdir(sections_dir)
        files = [f for f in files if f.endswith('.md')]  # .md 파일만 선택
        
        # 파일명의 숫자 부분을 기준으로 정렬
        files.sort(key=lambda x: int(x.split('_')[0]) if x.split('_')[0].isdigit() else float('inf'))
        
        for file in files:
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
        
        # 현재 처리 중인 논문 정보 찾기
        paper_info = next(
            (paper for paper in self.state.papers_info['papers'] if paper['title'][:10] == title),
            None
        )
        summary_content = []
        with open(summary_path, 'w', encoding='utf-8') as f:
            # 논문 메타 정보 추가
            if paper_info:
                meta_info = f"# {paper_info['title']}\n\n"
                meta_info += f"**URL**: {paper_info['url']}\n"
                meta_info += f"**Date**: {paper_info['date']}\n"
                meta_info += f"**Authors**: {paper_info['authors']}\n\n"
                meta_info += "---\n\n"
                f.write(meta_info)
                summary_content.append(meta_info)
                
            
            # 각 섹션 요약 추가
            for file, summary in summaries:
                section_name = os.path.splitext(file)[0].upper()
                section_content = f"## {section_name}\n\n"
                section_content += f"{summary.raw}\n\n"
                section_content += "---\n\n"
                f.write(section_content)
                summary_content.append(section_content)
        
        self.state.body = "\n".join(summary_content)
        return summary_content
        
    @listen("news_search_go")
    def news_search(self):
        crew = NewsCrew()
        inputs = {"date": self.state.date, "user_input": self.state.user_input}
        news = crew.crew().kickoff(inputs=inputs)
        self.state.body = news
        print(news)
        return news

    @listen(or_("news_search", "paper_summarizer"))
    def gmail_draft(self):
        crew = GmailCrew()
        inputs = {"date": self.state.date, "user_input": self.state.user_input, "body": self.state.body, "category": self.state.category}
        draft_news = crew.crew().kickoff(inputs=inputs)
        print(draft_news)
        return draft_news
    
    # @listen("keyword_search_go")
    # def keyword_search(self):
    #     result = main(self.state.user_input)
    #     print(result)



def kickoff():
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))
    user_input_flow = UserInputFlow()
    user_input_flow.plot()
    user_input_flow.kickoff()
    session.end_session()

if __name__ == "__main__":
    kickoff()
