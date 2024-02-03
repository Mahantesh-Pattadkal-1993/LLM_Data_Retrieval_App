"""
Desc: This code show how to build a Q&A bot on top of your custom text.
Here, the text is vectorised and stored in the vector store 
Further the vector store is queried
"""


import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from Credentials import api_key


os.environ["OPENAI_API_KEY"]= api_key

#specify the model of choice
model = "gpt-3.5-turbo-instruct"

llm = OpenAI(model=model, temperature = 0.7 )



#chat_model = ChatOpenAI(openai_api_key=api_key)


# Ask Question based on my text.txt file
loader = TextLoader("text.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query("What is my Name?"))


"""  
To fix: with deprecation of da-vinci-03, this code fails

"""