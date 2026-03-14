from langchain_openai import ChatOpenAI
from app.config.settings import MODEL_NAME

def get_llm():

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    return llm