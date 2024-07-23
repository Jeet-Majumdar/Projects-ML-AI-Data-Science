
**Blog generation**
Blog generation using llama2 model using AWS Bedrock, and saving the generated blog in S3 bucket.

**API Request for Lamma2 in bedrock with 13b parameters**
```json
{
    "modelId": "meta.llama2-13b-chat-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
}
```