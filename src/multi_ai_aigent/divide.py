import re
import os

def split_and_save_sections_by_keywords(text, output_dir,date):
    base_path = os.path.join(date, output_dir, "sections")
    print(f"=== Processing Start ===")
    print(f"Output directory: {output_dir}")
    
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
    
    print(f"\nLooking for these keywords: {keywords}")
    
    # 수정된 패턴: 줄 시작 부분에서 키워드를 찾되, 앞뒤 공백과 줄바꿈을 허용
    pattern = r'(?im)^\s*(?:#{1,2}\s*)?(?:\d+\s+)?(' + '|'.join(keywords) + r')\s*$'
    print(f"\nUsing regex pattern: {pattern}")
    
    # 텍스트를 줄 단위로 처리
    lines = text.split('\n')
    sections = []
    current_section = []
    current_title = None
    
    for line in lines:
        # 키워드 매칭 확인
        match = re.match(pattern, line.strip())
        if match:
            # 이전 섹션 저장
            if current_title and current_section:
                sections.append((current_title, '\n'.join(current_section)))
            # 새 섹션 시작
            current_title = match.group(1).upper()
            current_section = []
            print(f"\nFound section: {current_title}")
        elif current_title:
            current_section.append(line)
    
    # 마지막 섹션 저장
    if current_title and current_section:
        sections.append((current_title, '\n'.join(current_section)))
    
    print(f"\nFound {len(sections)} sections")
    
    # 섹션 저장
    # 전체 디렉토리 경로 생성
    os.makedirs(base_path, exist_ok=True)
    
    for title, content in sections:
        filename = f"{base_path}/{title.lower().replace(' ', '_')}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved section: {filename}")
    
    print("\n=== Processing Complete ===")