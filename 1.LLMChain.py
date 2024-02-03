import os
from Credentials import api_key
os.environ["OPENAI_API_KEY"] = api_key

#specify the model of choice
model = "gpt-3.5-turbo-instruct"

from langchain.llms import OpenAI 
llm = OpenAI(model=model, temperature = 0.7 )
#place = llm("Suggest me one famous tourist place from India")
#print(place)

#---------------------------------------------------------------
# Create a prompt template where you can specify the country of choice
#---------------------------------------------------------------

from langchain.prompts import PromptTemplate
prompt_TouristPlace = PromptTemplate(

    input_variables= ["Country"],
    template=  "Suggest me one famous tourist place from {Country}"
)

#-----------------------------------------------------
# Use LLMChain function to build this as a pipeline
#-----------------------------------------------------

from langchain.chains import LLMChain

TouristPlace_chain = LLMChain(llm=llm,prompt=prompt_TouristPlace)
out = TouristPlace_chain.run("England")
print(out)


