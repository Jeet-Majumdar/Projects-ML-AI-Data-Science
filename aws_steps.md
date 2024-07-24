
**Set up awscli**
After `pip install awscli` in your environment, we need to configure it with `aws configure`
We need to know: `AWS Access Key`, and `AWS Secret Access Key`. 
You will get both of them when you create Users at AWS Users Portal

**Set up Amazon Bedrock**
Go to `Amazon Bedrock` and click on `Base models`.
Click on `Manage Model Access` and grant the access the models that you want.
These models access also depends on your choice of region. Models may not be available at some geographical region. Best region is 'us-east-1'
To check the availability in another way, select the models and click on `Request model access`

Basic structure of the app should be:
```python
import boto3
import json

prompt_data = """
Write me something about USA
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body = json.dumps(payload)
model_id = "meta.llama2-70b-chat-v1"
response = bedrock.invoke_model(
    modelId = model_id,
    accept = "application/json",
    contentType = "application/json",
    body = body,
)

response_body = json.loads(response.get("body").read())
repsonse_text = response_body['generation']
print(repsonse_text)
```

