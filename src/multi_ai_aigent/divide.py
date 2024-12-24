import re
import os

def split_and_save_sections_by_keywords(text, output_dir,date):
    base_path = os.path.join(date, output_dir, "sections")
    print(f"=== Processing Start ===")
    print(f"Output directory: {output_dir}")
    
    main_sections = [
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
    
   # 단순화된 패턴
    patterns = [
        r'^#{1,4}\s*.*?(?:' + '|'.join(main_sections) + r')\s*$',  # #### Abstract
        r'^\d+\.\s*(?:' + '|'.join(main_sections) + r')\s*$',      # 1. Introduction
        r'^(?:' + '|'.join(main_sections) + r')\s*$'               # ABSTRACT
    ]
    
    lines = text.split('\n')
    sections = []
    current_section = []
    current_title = None
    
    for line in lines:
        line = line.strip()
        found_section = False
        
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                # 현재 라인에서 섹션 제목 찾기
                for section in main_sections:
                    if section.lower() in line.lower():
                        # 이전 섹션 저장
                        if current_title and current_section:
                            sections.append((current_title, '\n'.join(current_section)))
                        
                        current_title = section
                        current_section = []
                        found_section = True
                        print(f"\nFound section: {current_title}")
                        break
                break
        
        if not found_section and current_title:
            current_section.append(line)
    
    # 마지막 섹션 저장
    if current_title and current_section:
        sections.append((current_title, '\n'.join(current_section)))
    
    print(f"\nFound {len(sections)} sections")
    
    # 섹션 저장
    os.makedirs(base_path, exist_ok=True)
    for i, (title, content) in enumerate(sections, 1):
        safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '_')
        filename = f"{base_path}/{i}_{safe_title}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')
        print(f"Saved section: {filename}")
    
    print("\n=== Processing Complete ===")