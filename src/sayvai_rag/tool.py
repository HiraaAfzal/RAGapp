from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.tools import BaseTool, StructuredTool, tool

load_dotenv()


# this is our tool
@tool 
def search_index(query: str) -> str:
    """
    this fuction will provide the information about india and its geography
    args:
      query: str anything related to india
    """
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name="indiatour", embedding=embeddings)

    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"score_threshold": 0.5, "k": 1},
    )

    return retriever.invoke(query)[0].page_content
