
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

template = """If you cannot answer, say "I don't know".
Question: {query}\n\n
Answer: \n
""".strip()

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

def template_single(company):
    # query = f'What industry does {company} specialize in?'
    # query = f'Is {company} a Product or Service company? Answer with a single word.'
    query = f'Which sector does {company} belong to? Also is it a product based company or a service based company? Answer in the particular format: (sector, product/service)'
    prompt = prompt_template.format(query=query)
    output = llm.invoke(prompt)
    res = output.split('\n')[-1]
    time.sleep(30) # To prevent rate limit from happening.
    try:
        if "I don't know" in res:
            return ""
        else:
            answer = res.split('?')[-1].replace('\n', '')\
                .strip().split(':')[-1].replace('.', '')\
                .replace('"', '')
            ans_parts = answer.split(',')
            sector = ans_parts[0].strip().lower()
            company_type = ans_parts[1].strip().lower()
            if 'product' in company_type:
                company_type = 'product'
            elif 'service' in company_type:
                company_type = 'service'
            else:
                company_type = ''
            about = sector + "+" + company_type
            print(answer)
            return about
    except:
        return ""

# template_single('Micron')

df = pd.read_excel('recruters.xlsx')

df["Industry"] = df["Company"].apply(template_single)

df.to_excel('recruters.xlsx')
