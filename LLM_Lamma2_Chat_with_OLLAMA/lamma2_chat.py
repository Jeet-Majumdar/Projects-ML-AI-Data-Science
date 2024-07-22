from langchain_community.llms import Ollama

llama2 = Ollama(base_url='http://localhost:11434', model='llama2')

print(llama2("why is the sky blue?"))