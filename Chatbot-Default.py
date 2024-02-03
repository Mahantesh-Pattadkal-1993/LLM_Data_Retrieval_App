"""
Desc: This code show how to build a Chat bot, the chatbot expects conversations in AI-Human format
Next, to chat with this chatbot, you need to send in the entire history of conversation
"""



import os
from Credentials import api_key
os.environ["OPENAI_API_KEY"] = api_key

import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"

# use chat model instead of retrival model
chat = ChatOpenAI(
   
    model='gpt-3.5-turbo'
)


# Standardize the text into human and AI chat messages

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to understand string theory.")
]

res = chat(messages)

#This is what the response is 
"""
AIMessage(content="String theory is a theoretical framework in physics 
that aims to provide a unified description of the fundamental particles 
and forces in the universe. It suggests that at the most fundamental level, 
particles are not point-like entities but instead tiny, vibrating strings.
\n\nHere are some key points to understand about string theory:\n\n1. 
Building blocks: According to string theory, the basic building blocks 
of the universe are not particles but rather tiny, one-dimensional strings. 

"""


# add latest AI response to messages
messages.append(res)

# now create a new user prompt, and notice that we dont mention string theory here, we refer "it" and still the LLM can understand
#that we are refering to string theory as it gets to see the whole message during API calls
prompt = HumanMessage(
    content="Why do physicists believe it can produce a 'unified theory'?"
)
# add to messages
messages.append(prompt) 

# send to chat-gpt
res = chat(messages)
print(res)
