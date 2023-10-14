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
llm = OpenAI(openai_api_key=api_key)


#chat_model = ChatOpenAI(openai_api_key=api_key)


# Ask Question based on my text.txt file
loader = TextLoader("text.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query("What is my Name?"))