
# Agentic AI

This document is a note from Udacity course **Agentic AI**.

## Common components of an AI Agent:

* **Large Language Model (LLM)**: The "brain" for understanding, reasoning, acting.
* **Tools**: External functions, APIs for interaction and enhanced capabilities.
* **Instructions**: Guidelines (system prompts) defining behavior and goals.
* **Memory**: Short-term (context) & Long-term (history) for learning and consistency.
* **Runtime/Orchestration Layer**: Manages execution flow, tool usage, observation processing.
 


## Chain-of-Thought (CoT) and ReAct

A detailed Chain-of-Thought (CoT) prompt instructs an LLM to analyze multiple data sources and structure its reasoning to solve a complex problem.


### Scenario 1: 

A patient presents with a persistent cough and fatigue. Our goal is to determine the likely cause.

#### Approach a: The "All Data Upfront" CoT Method

One way to solve this is to give the AI a single, large prompt containing all the information we have about the patient and ask it to reason through the data.

```
system_prompt_cot = """
You are a diagnostic physician. Think step by step, correlating the symptoms with the provided patient data to form a differential diagnosis. Explain your reasoning.
"""
```







* [Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models]: https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/
[[Meta AI] Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/)


* [Retrieval Augmented Generation (RAG)]: https://www.promptingguide.ai/techniques/rag
[[Prompt Engineering Guide] Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag)


* [Retrieval Augmented Generation (RAG) for LLMs]: https://www.hopsworks.ai/dictionary/retrieval-augmented-generation-llm
[[HopsWorks] Retrieval Augmented Generation (RAG) for LLMs](https://www.hopsworks.ai/dictionary/retrieval-augmented-generation-llm)


* [What is retrieval-augmented generation?]: https://research.ibm.com/blog/retrieval-augmented-generation-RAG
[[IBM Blog] What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)