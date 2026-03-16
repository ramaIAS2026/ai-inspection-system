from langchain_openai import ChatOpenAI
import os

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

# from langchain_openai import ChatOpenAI
# from app.config.settings import MODEL_NAME

# from langchain_openai import ChatOpenAI

# def get_llm():
#     return ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature=0
#     )

#def get_llm():

#    llm = ChatOpenAI(
#        model=MODEL_NAME,
#       temperature=0
#   )

#   return llm
