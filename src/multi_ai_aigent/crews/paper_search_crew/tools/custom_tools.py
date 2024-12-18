from typing import Type, List, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class SearchArxivInput(BaseModel):
    """Input schema for SearchArxivTool."""
    keywords: List[str] = Field(
        default_factory=list,
        description="List of keywords to search for in papers"
    )
    date_range: str = Field(
        default=None,
        description="Date range for the search in format 'YYYY-MM-DD to YYYY-MM-DD'"
    )
    number_of_papers: int = Field(
        default=3,
        description="Number of papers to return"
    )

class SearchArxivTool(BaseTool):
    name: str = "search_arxiv_tool"
    description: str = "Searches for academic papers on  keywords, and date range"
    args_schema: Type[BaseModel] = SearchArxivInput

    def _run(self, keywords: List[str] = None, 
            date_range: str = None, number_of_papers: int = 10) -> List[Dict[str, Any]]:
        """
        arXiv에서 논문을 검색하는 도구
        """
        import arxiv
        
        # 검색 쿼리 구성
        query_parts = []        
        # 키워드 추가 (recent와 papers 같은 일반적인 단어 제외)
        if keywords:
            filtered_keywords = [kw for kw in keywords if kw not in ["recent", "papers"]]
            if filtered_keywords:
                keyword_query = " AND ".join(f'"{kw}"' for kw in filtered_keywords)
                query_parts.append(f"({keyword_query})")
        
        # 최종 쿼리 생성
        query = " AND ".join(query_parts) if query_parts else "all"
        
        # arXiv 검색 실행
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=number_of_papers,
            sort_by=arxiv.SortCriterion.SubmittedDate
            
        )
        # 결과 수집
        papers = []
        for result in client.results(search):
            paper_info = {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "abstract": result.summary,
                "published": result.published.strftime("%Y-%m-%d"),
                "url": result.pdf_url,
                "arxiv_id": result.entry_id
            }
            papers.append(paper_info)
            
        return papers

    async def _arun(self, arxiv_category: str = None, keywords: List[str] = None, 
                    date_range: str = None, number_of_papers: int = 10) -> List[Dict[str, Any]]:
        """비동기 실행을 위한 메서드"""
        raise NotImplementedError("비동기 실행은 지원되지 않습니다")