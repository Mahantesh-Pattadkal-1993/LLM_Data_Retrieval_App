import os
from Credentials import api_key
os.environ["OPENAI_API_KEY"] = api_key

from langchain.llms import OpenAI 
llm = OpenAI(temperature = 0.7 )


"""
Build two chains and use Sequential Chain functions
------------------------------------

we can get output of the previous chain- ie Tourist Place name (this is not possible with simple chains)

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

TouristPlace_chain = LLMChain(llm=llm, prompt=prompt_TouristPlace, output_key="TouristPlace")

#------------------------------------------------
# Chain 2 -  Generate Itinerary
#------------------------------------------------


prompt_Itinerary = PromptTemplate(

    input_variables= ["TouristPlace"],
    template=  "Create an itinerary to reach {TouristPlace} from Mumbai and specify means of transport, return the ouput as commma separated list "
)

Itinerary_chain = LLMChain(llm=llm, prompt=prompt_Itinerary, output_key="Itinerary")

# Combine both the chains

from langchain.chains import SequentialChain

final_chain = SequentialChain(
    chains = [TouristPlace_chain,Itinerary_chain],
    input_variables= ["Country"],
    output_variables= ["TouristPlace","Itinerary"]
)

response = final_chain({"Country":"Egypt"})  # here as the sequential chain can have multiple input, we use dictionary to send inputs
print(response)
