"𝗛𝗼𝘄 𝗺𝘂𝗰𝗵 𝗚𝗣𝗨 𝗺𝗲𝗺𝗼𝗿𝘆 𝗶𝘀 𝗻𝗲𝗲𝗱𝗲𝗱 𝘁𝗼 𝘀𝗲𝗿𝘃𝗲 𝗮 𝗟𝗮𝗿𝗴𝗲 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗠𝗼𝗱𝗲𝗹 (𝗟𝗟𝗠)?"

Whether you're deploying a 7B parameter model or something larger, estimating the GPU memory is critical.
So, what's the math behind it? Here's a formula that can help you estimate the GPU memory required for serving an LLM:

**𝗠 = ((𝗣 * 𝟰𝗕) / (𝟯𝟮 / 𝗤)) * 𝟭.𝟮**

Where:

**𝐌** is the GPU memory in Gigabytes.
**𝐏** is the number of parameters in the model.
**𝟒𝐁** represents the 4 bytes used per parameter.
**𝐐** is the number of bits for loading the model.
**𝟏.𝟐** accounts for a 20% overhead.

**𝗧𝗵𝗶𝘀 𝗼𝘃𝗲𝗿𝗵𝗲𝗮𝗱 𝗶𝘀𝗻'𝘁 𝗷𝘂𝘀𝘁 𝗮 𝗯𝘂𝗳𝗳𝗲𝗿 —** it's crucial for additional memory used during inference, such as storing activations (intermediate results) of the model. Without accounting for this, you might underestimate the memory requirements, leading to bottlenecks during inference.

Ref:
1. [𝗛𝗼𝘄 𝗺𝘂𝗰𝗵 𝗚𝗣𝗨 𝗺𝗲𝗺𝗼𝗿𝘆 𝗶𝘀 𝗻𝗲𝗲𝗱𝗲𝗱 𝘁𝗼 s𝗲𝗿𝘃𝗲 𝗮 𝗟𝗮𝗿𝗴𝗲 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗠𝗼𝗱𝗲𝗹](https://ksingh7.medium.com/calculate-how-much-gpu-memory-you-need-to-serve-any-llm-67301a844f21)