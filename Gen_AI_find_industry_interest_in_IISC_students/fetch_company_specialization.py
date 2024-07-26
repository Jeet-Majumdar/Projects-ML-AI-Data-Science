
import time
import pandas as pd
from decouple import config
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
# from langchain_huggingface import HuggingFaceEndpoint

# Set your Hugging Face API token
huggingfacehub_api_token = config('HUGGING_FACE_API_TOKEN')

llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', 
                     huggingfacehub_api_token=huggingfacehub_api_token)

template = """Answer the question in no more than 3 words, and if the answer is not contained within the text below, say "I don't know"
Question: {query}\n\n
Answer: \n
""".strip()

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

def template_single(company):
    query = f'What industry does {company} specialize in?'
    prompt = prompt_template.format(query=query)
    output = llm.invoke(prompt)
    res = output.split('\n')[-1]
    time.sleep(60) # To prevent rate limit from happening.
    try:
        if "I don't know" in res:
            return ""
        else:
            industry = res.split('?')[-1].replace('\n', '')\
                .strip().split(':')[-1].replace('.', '')\
                .replace('"', '')
            print(industry)
            return industry
    except:
        return ""


df = pd.read_excel('recruters.xlsx')

df["Industry"] = df["Company"].apply(template_single)

df.to_excel('recruters.xlsx')
