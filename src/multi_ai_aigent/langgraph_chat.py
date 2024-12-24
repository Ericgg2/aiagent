# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama import ChatOllama, OllamaEmbeddings
# from langchain_milvus import Milvus
# from typing import Annotated, TypedDict
# from langgraph.graph import END, StateGraph, add_messages
# from langgraph.checkpoint.memory import MemorySaver
# from langchain_core.runnables import RunnableConfig
# from langchain_teddynote.messages import stream_graph, random_uuid

# import os



# # GraphState 상태 정의
# class GraphState(TypedDict):
#     question: Annotated[str, "Question"]  # 질문
#     context: Annotated[str, "Context"]  # 문서의 검색 결과
#     answer: Annotated[str, "Answer"]  # 답변
#     messages: Annotated[list, add_messages]  # 메시지(누적되는 list)

# # DB 내 검색 기능, URI db 있는 위치로 수정
# def create_retriever():
#     URI = "./milvus_rag.db"
#     embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")
#     vector_store = Milvus(
#         embedding_function=embeddings,
#         connection_args={"uri": URI},
#     )
#     return vector_store.as_retriever()

# # 검색 체인 생성
# def create_retriever_chain(retriever):
#     template = """
#     1. 당신은 AI, ML와 관련된 지식을 갖고 있는 AI 연구 개발자입니다.
#     2. 주어진 context를 참고하세요. 만약 관련 내용을 찾을 수 없다면 그냥 모른다고 답하세요.
#     3. 쉽게 이해할 수 있도록 한국어로 친절히 답변하세요.
#     4. 답변 첫 문장엔 참고한 논문의 title을 적어주세요.
#     Context: {context}

#     Question: {question}

#     Answer:
#     """
#     prompt = ChatPromptTemplate.from_template(template)
#     llm = ChatOllama(model="benedict/linkbricks-llama3.1-korean:8b", temperature=0)
#     return (
#         {"context": retriever, "question": RunnablePassthrough()}
#         | prompt
#         | llm
#         | StrOutputParser()
#     )

# # 문서 형식 수정
# def format_docs(docs):
#     return "\n\n".join(
#         [
#             f'<document><content>{doc.page_content}</content></document>'
#             for doc in docs
#         ]
#     )

# # 문서 검색 노드
# def retrieve_document(state: GraphState) -> GraphState:
#     # 질문을 상태에서 가져옵니다.
#     latest_question = state["question"]

#     # 문서에서 검색하여 관련성 있는 문서를 찾습니다.
#     retriever = create_retriever()
#     retrieved_docs = retriever.invoke(latest_question)

#     # 검색된 문서를 형식화합니다.(프롬프트 입력으로 넣어주기 위함)
#     retrieved_docs = format_docs(retrieved_docs)

#     # 검색된 문서를 context 키에 저장합니다.
#     return GraphState(context=retrieved_docs)


# # 답변 생성 노드
# def llm_answer(state: GraphState) -> GraphState:
#     # 질문을 상태에서 가져옵니다.
#     latest_question = state["question"]

#     # 검색된 문서를 상태에서 가져옵니다.
#     context = state["context"]
    
#     template = """
#     1. 당신은 AI, ML와 관련된 지식을 갖고 있는 AI 연구 개발자입니다.
#     2. 주어진 context를 참고하세요. 만약 관련 내용을 찾을 수 없다면 그냥 모른다고 답하세요.
#     3. 쉽게 이해할 수 있도록 한국어로 친절히 답변하세요.
#     4. 답변 첫 문장엔 참고한 논문의 title을 적어주세요.
#     Context: {context}

#     Question: {question}

#     Answer:
#     """
#     prompt = ChatPromptTemplate.from_template(template)

#     llm = ChatOllama(model="benedict/linkbricks-llama3.1-korean:8b", temperature=0)

#     rag_chain = (
#     {"context": lambda x: context, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
#     )
#     # 체인을 호출하여 답변을 생성합니다.
#     response = rag_chain.invoke(latest_question)
    
#     # 생성된 답변, (유저의 질문, 답변) 메시지를 상태에 저장합니다.
#     return GraphState(
#         answer=response, messages=[("user", latest_question), ("assistant", response)]
#     )

# def create_workflow():
#     workflow = StateGraph(GraphState)
#     workflow.add_node("retrieve", retrieve_document)
#     workflow.add_node("llm_answer", llm_answer)
#     workflow.add_edge("retrieve", "llm_answer")
#     workflow.add_edge("llm_answer", END)
#     workflow.set_entry_point("retrieve")
#     return workflow

# def main(user_question: str):
#     # 워크플로우 생성 및 컴파일
#     workflow = create_workflow()
#     memory = MemorySaver()
#     app = workflow.compile(checkpointer=memory)
    
#     # config 설정
#     config = RunnableConfig(
#         recursion_limit=20, 
#         configurable={"thread_id": random_uuid()}
#     )
    
#     # 질문 입력 및 그래프 실행 => 사용자에게 받은 입력을 question으로 넣으면 될듯
#     inputs = GraphState(question=user_question)
#     result = stream_graph(app, inputs, config, ["llm_answer"])
#     return result

# # if __name__ == "__main__":
# #     main()