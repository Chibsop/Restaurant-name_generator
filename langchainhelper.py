from langchain.chains import SequentialChain, LLMChain
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

# Instantiate your language model (Ollama), assuming 'llama3' is the model name
llm = Ollama(model='llama3')


def generate_bike_name_and_items(bike_requirements):
    prompt_template = PromptTemplate(
        input_variables=['bike_requirements'],
        template=f"I am looking for a bike and i am looking for some options to buy, i want you to give me a list of "
                 f"name of bikes according to my need, my need are as follows: {bike_requirements}, make sure to give only the names of the bike as a list nothing more, i do not want any kind of description."
    )
    chain = LLMChain(llm=llm, prompt=prompt_template, output_key="bike_name_and_items")

    response = chain({'bike_requirements': bike_requirements})
    return response