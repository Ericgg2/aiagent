import requests
import PyPDF2
import tempfile

url = 'http://arxiv.org/pdf/2402.03328v2'  

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

text = download_and_parse_pdf(url)
print(text)

    # def paper_summarizer(self):
    #     crew = PaperSummarizer()
    #     self.state.date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #     current_date = self.state.date
        
    #     for paper_info in self.state.papers_info['papers']:
    #         text = download_and_parse_pdf(paper_info['url'])
    #         date = paper_info['date']
    #         title = paper_info['title'][:10]
    #         print(f"title: {title}")
    #         summarized_papers = []
    #         split_and_save_sections_by_keywords(text,title,current_date)
    #         sections_dir = os.path.join(date, title, "sections")
    #         if os.path.exists(sections_dir):
    #             for file in os.listdir(sections_dir):
    #                 file_path = os.path.join(sections_dir, file)
    #                 with open(file_path, 'r', encoding='utf-8') as f:
    #                     text = f.read()
    #                     print(f"Reading section {file}: {len(text)} characters")
    #                 inputs = {"file": file, "text": text, "date": date, "current_date": current_date} 
    #                 summary = crew.crew().kickoff(inputs=inputs)
    #                 print(f"summary: {summary}")
    #                 summarized_papers.append(summary)
    #                 summary_path = os.path.join(date, title, "summary.md")
    #                 os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    #                 with open(summary_path, 'a', encoding='utf-8') as f:
    #                     f.write(f"## {os.path.splitext(file)[0].upper()}\n\n")
    #                     f.write(f"{summary.raw}\n\n")
    #                     f.write("---\n\n")
