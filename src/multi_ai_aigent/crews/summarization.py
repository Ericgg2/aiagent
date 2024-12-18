from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from marker.config.parser import ConfigParser
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import requests
from tempfile import NamedTemporaryFile
from PIL import Image
import os
import re
import glob

def download_and_convert_pdf(url, output_markdown_path):
    """PDF를 다운로드하고 마크다운으로 변환하는 함수"""
    try:
        # tmp 디렉토리 생성
        tmp_dir = "./tmp"
        os.makedirs(tmp_dir, exist_ok=True)

        # PDF 다운로드 및 변환 로직
        response = requests.get(url)
        response.raise_for_status()

        with NamedTemporaryFile(delete=False, suffix=".pdf", dir=tmp_dir) as temp_pdf_file:
            temp_pdf_file.write(response.content)
            temp_pdf_path = temp_pdf_file.name

        # ... 기존 PDF 변환 코드 ...
        config = {"output_format": "markdown"}
        config_parser = ConfigParser(config)
        
        converter = PdfConverter(
            config=config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
            processor_list=config_parser.get_processors(),
            renderer=config_parser.get_renderer()
        )

        rendered = converter(temp_pdf_path)
        text, metadata, images = text_from_rendered(rendered)

        # 결과 저장
        with open(output_markdown_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        # 이미지 저장
        for name, image in images.items():
            image.save(name, "JPEG")

        return True

    except Exception as e:
        print(f"PDF 변환 중 오류 발생: {e}")
        return False

    finally:
        if 'temp_pdf_path' in locals() and os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)

def split_and_save_sections_by_keywords(md_file_path, output_dir):
    """마크다운 파일을 섹션별로 분리하여 저장하는 함수"""
    """
    Args:
        md_file_path: 마크다운 파일 경로
        output_dir: 저장할 디렉토리 경로
    """
    # AI 논문에서 주로 사용되는 키워드 정의
    keywords = [
        "ABSTRACT",
        "APPROACH",
        "BACKGROUND",
        "INTRODUCTION",
        "RELATED WORK",
        "METHODOLOGY",
        "PRE-TRAINING",
        "ALIGNMENT",
        "METHOD",
        "IMPLEMENTATION", 
        "EXPERIMENTAL SETUP",
        "EXPERIMENTS",
        "EVALUATIONS",
        "LIMITATIONS AND ETHICAL CONSIDERATIONS",
        "RESULTS",
        "DISCUSSION", 
        "CONCLUSION",
        "FUTURE WORK",
        "REFERENCES"
    ]
    
    # 대소문자 구분 없이 키워드 매칭을 위한 패턴 생성
    # '#' 또는 '##' 다음에 선택적 숫자와 키워드가 오는 패턴
    pattern = r'(?i)^\s*#{1,2}\s*(?:\d+\s+)?(' + '|'.join(keywords) + r')\s*$'
    
    # 파일 읽기
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 섹션 분리
    sections = re.split(pattern, content, flags=re.MULTILINE | re.IGNORECASE)
    
    # 각 섹션 저장
    current_title = None
    current_content = []
    
    for section in sections:
        if section and section.strip():
            if section.upper() in [k.upper() for k in keywords]:
                # 이전 섹션 저장
                if current_title:
                    filename = f"{output_dir}/{current_title.lower().replace(' ', '_')}.md"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(current_content))
                    print(f"저장됨: {filename}")
                
                # 새로운 섹션 시작
                current_title = section
                current_content = []
            else:
                if current_title:
                    current_content.append(section.strip())
    
    # 마지막 섹션 저장
    if current_title and current_content:
        filename = f"{output_dir}/{current_title.lower().replace(' ', '_')}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(current_content))
        print(f"저장됨: {filename}")

def stuff_summ(path):
    """각 섹션을 요약하는 함수"""
    prompt_template = """Please summarize the sentence according to the following REQUEST.
    REQUEST:
    1. Your job is professional researcher in AI, and you need to help other people to understand this study.
    2. Summarize the main points in bullet points in KOREAN.
    3. Translate the summary into Korean if it is written in English.
    4. If the context is divided, please summarize it separately.
    5. DO NOT translate any technical terms.
    6. If there is anything about table and figure, please put the table, figure link form, and caption in the summary as it is.
    7. Please convert the final summary into a markdown format in Korean.
    8. Please collect the English words(from 3) in the entire summary separately in KEYWORD.
    9. Don't put any markdown format (such as "'''markdown'''") other than text.

    CONTEXT:
    {context}

    SUMMARY:"

    KEYWORD:"
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    
    loader_m = UnstructuredMarkdownLoader(path)
    
    # 문서를 로드합니다.
    docs = loader_m.load()
    
    # LLM 체인 정의
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o")

    # StuffDocumentsChain 정의
    stuff_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    response = stuff_chain.invoke({"context": docs})
    current_file = os.path.basename(path)
    current_title, _ = os.path.splitext(current_file)
    filename = f"{path}/summ_{current_file}"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {current_title}\n")
        f.write(response)
    print(f"저장됨: {filename}")

def merge_markdown_files(input_dir, output_file):
    """요약된 마크다운 파일들을 하나로 병합하는 함수"""
    # 모든 키워드를 저장할 리스트
    all_keywords = []
    
    # 파일 순서 정의
    file_order = [
        "summ_abstract.md",
        "summ_introduction.md",
        "summ_pre-training.md",
        "summ_alignment.md",
        "summ_evaluations.md",
        "summ_limitations_and_ethical_considerations.md",
        "summ_conclusion.md"
    ]
    
    # 병합된 내용을 저장할 리스트
    merged_content = []
    
    # 각 파일 처리
    for filename in file_order:
        file_path = os.path.join(input_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # KEYWORD 섹션만 찾아서 처리
                sections = content.split('\n\n')
                filtered_sections = []
                
                for section in sections:
                    if section.strip().startswith('**KEYWORD:**'):
                        # 키워드 추출 및 저장
                        keywords = section.replace('**KEYWORD:**', '').strip()
                        all_keywords.extend([k.strip() for k in keywords.split('\n')])
                    elif section.strip().startswith('### KEYWORD'):
                        # 키워드 추출 및 저장
                        keywords = section.replace('### KEYWORD', '').strip()
                        all_keywords.extend([k.strip() for k in keywords.split('\n')])
                    else:
                        filtered_sections.append(section)
                
                # 키워드 섹션을 제외한 나머지 내용 저장
                merged_content.append('\n\n'.join(filtered_sections).strip())
    
    # 중복 제거된 키워드 리스트 생성
    unique_keywords = list(set([k.strip('- ') for k in all_keywords if k.strip('- ')]))
    
    # 최종 내용 작성
    final_content = '\n\n'.join(merged_content)
    final_content += '\n\n# 종합 키워드\n'
    final_content += '\n'.join([f'- {keyword}' for keyword in sorted(unique_keywords) if not keyword == ':'])
    
    # 결과 파일 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"파일이 성공적으로 병합되어 {output_file}에 저장되었습니다.")

def main():
    # 설정값
    URL = "http://arxiv.org/pdf/2412.11949v1"
    OUTPUT_MD = "./output.md"
    SECTIONS_DIR = "./sections_md"
    FINAL_OUTPUT = "merged_summary.md"

    # 디렉토리 생성
    os.makedirs(SECTIONS_DIR, exist_ok=True)

    # 1. PDF 다운로드 및 마크다운 변환
    if download_and_convert_pdf(URL, OUTPUT_MD):
        print(f"마크다운 파일 저장됨: {OUTPUT_MD}")

        # 2. 섹션별 분리
        split_and_save_sections_by_keywords(OUTPUT_MD, SECTIONS_DIR)

        # 3. 각 섹션 요약
        md_files = glob.glob(os.path.join(SECTIONS_DIR, "*.md"))
        for f in md_files:
            stuff_summ(f)

        # 4. 최종 병합
        merge_markdown_files(SECTIONS_DIR, FINAL_OUTPUT)
        print("처리가 완료되었습니다.")
    else:
        print("PDF 처리 중 오류가 발생했습니다.")

if __name__ == "__main__":
    main()