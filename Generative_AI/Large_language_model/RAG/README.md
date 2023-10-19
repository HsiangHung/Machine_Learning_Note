
# Retrieval-Augmented Generation (RAG)

Large language models can be inconsistent. Sometimes they nail the answer to questions, other times they regurgitate random facts from their training data. If they occasionally sound like they have no idea what they’re saying, it’s because they don’t. LLMs know how words relate statistically, but not what they mean [[IBM Blog]][What is retrieval-augmented generation?].

## What Is Retrieval-augmented generation (RAG)?

RAG is an AI framework for retrieving facts from an external knowledge base to ground large language models (LLMs) on the most accurate, up-to-date information and to give users insight into LLMs' generative process [[IBM Blog]][What is retrieval-augmented generation?]. 


Implementing RAG in an LLM-based question answering system has two main benefits: 
1. It ensures that the model has access to the most current, reliable facts, and that users have access to the model’s sources, ensuring that its claims can be checked for accuracy and ultimately trusted.
2. By grounding an LLM on a set of external, verifiable facts, the model has fewer opportunities to pull information baked into its parameters. This reduces the chances that an LLM will leak sensitive data, or ‘hallucinate’ incorrect or misleading information.



## Use Case



* [What is retrieval-augmented generation?]: https://research.ibm.com/blog/retrieval-augmented-generation-RAG
[[IBM Blog] What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)