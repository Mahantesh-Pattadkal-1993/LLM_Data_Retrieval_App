import os
from Credentials import api_key
os.environ["OPENAI_API_KEY"] = api_key

from langchain.llms import OpenAI 
llm = OpenAI(temperature = 0.7 )


"""
Build two chains and use Chain functions
----------------------------------------------------------

The SimpleSeqChain outputs only the response of the last chain ie Itinerary, 
but we cant get output of the previous chain- ie Tourist Place name

"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#------------------------------------------------------------
# Chain 1 -  Identify Tourist Place
#------------------------------------------------------------

prompt_TouristPlace = PromptTemplate(

    input_variables= ["Country"],
    template=  "Suggest me one famous tourist place from {Country}"
)

TouristPlace_chain = LLMChain(llm=llm, prompt=prompt_TouristPlace)

#------------------------------------------------
# Chain 2 -  Generate Itinerary
#------------------------------------------------


prompt_Itinerary = PromptTemplate(

    input_variables= ["TouristPlace"],
    template=  "Create an itinerary to reach {TouristPlace} from Mumbai and specify means of transport, return the ouput as commma separated list "
)

Itinerary_chain = LLMChain(llm=llm, prompt=prompt_Itinerary )

# Combine both the chains

from langchain.chains import SimpleSequentialChain

final_chain = SimpleSequentialChain(chains=[TouristPlace_chain,Itinerary_chain])
response = final_chain.run("Egypt")
print(response)
