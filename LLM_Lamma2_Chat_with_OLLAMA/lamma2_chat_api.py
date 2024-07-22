import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'

headers = {
    'Content-Type':"application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data = {
        'model': 'llama2',
        'prompt': final_prompt,
        'stream': False
    }

    res = requests.post(url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        res_text = res.text
        data = json.load(res_text)
        actual_res = data['response']
        return actual_res
    else:
        print("Error: ", res.text)

interface = gr.Interface(
    fn = generate_response,
    input = gr.Textbox(lines = 4, placeholder = "Enter your prompt"),
    outputs = "text"
)

interface.launch()