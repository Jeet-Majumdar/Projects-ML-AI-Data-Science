
# RAG application to answer questions from a bunch of pdfs.

```meramid
flowchart LR
A[Question] --> B((LLM))
A --> |Similarity Search| C[(Vectorstore)]
C --> D[Relevant Chunks]
D --> B
B --> E([Answer])
```
**Essentially at the core of the project involves two steps:**
1. The pdf will be stored in a Vector store
2. From this Vector store we can query any information that we want.

Doccument -> Split into Chunks -> Create Embeddings -> Vector Store

We are going to create embeddings using `Amazon Titan` and store in `Fiass`. We will also perform simmilarity search using `Fiass`.

--------

**API Request for Titan Embeddings**
```json
{
    "modelId": "amazon.titan-embed-text-v1",
    "contentType": "application/json",
    "accept": "*/*",
    "body": "{\"inputText\":\"this is where you place your input text\"}"
}
```

**API Request for Claude anthropic model**

```json
{
    "modelId": "anthropic.claude-v2",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"prompt\":\"\\n\\nHuman: You are an expert of physics\\n\\n\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
  }
```