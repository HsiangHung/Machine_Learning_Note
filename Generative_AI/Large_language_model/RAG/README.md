
# Retrieval-Augmented Generation (RAG)


## What Is RAG?


Large language models (LLMs) sometimes can nail the answer to questions, but other times they regurgitate random facts from their training data. We might observe hallucination in LLMs: they have no idea what they’re saying. LLMs know how words relate statistically, but not what they mean [[IBM Blog]][What is retrieval-augmented generation?].

RAG is an AI framework for retrieving facts from an **external** knowledge base to ground LLMs on the most accurate, **up-to-date** information and to give users insight into LLMs' generative process [[Meta AI]][Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models][[IBM Blog]][What is retrieval-augmented generation?].  This flexibility makes RAG adaptive for situations where facts could evolve over time. 

RAG can be fine-tuned and its internal knowledge can be modified in an efficient manner and without needing retraining of the entire model.


### Benfits Using RAG

Implementing RAG in an LLM-based question answering system has the following main benefits [[IBM Blog]][What is retrieval-augmented generation?]: 
1. It ensures that the model has access to the most current, reliable facts, and that users have access to the model’s sources, ensuring that its claims can be checked for accuracy and ultimately trusted.
2. By grounding an LLM on a set of external, verifiable facts, the model has fewer opportunities to pull information baked into its parameters. This reduces the chances that an LLM will leak sensitive data, or hallucinate incorrect or misleading information.
3. RAG also reduces the need for users to continuously train the model on new data and update its parameters as circumstances evolve (fine-tuning). In this way, RAG can lower the computational and financial costs of running LLM-powered chatbots in an enterprise setting. 


In a RAG system, you are asking the model to respond to a question by browsing through the content in a book, as opposed to trying to remember facts from memory. It is like an open-book exam.

LLMs need to be explicitly trained to recognize questions they can’t answer, rather than being prone to making things up.


### Use Case

Alice has learned that her son’s school will have early dismissal on Wednesdays for the rest of the year. She wants to know if she can take vacation in half-day increments and if she has enough vacation to finish the year. 

To craft its response, the LLM first pulls data from Alice’s HR files to find out how much vacation she gets as a longtime employee, and how many days she has left for the year. It also searches the company’s policies to verify that her vacation can be taken in half-days. These facts are injected into Alice’s initial query and passed to the LLM, which generates a concise, personalized answer. A chatbot delivers the response, with links to its sources.

For example, Alice wants to know how many days of maternity leave she gets. A chatbot that does not use RAG responds cheerfully (and incorrectly): “Take as long as you want.” When the LLM failed to find a precise answer, it should have responded, “I’m sorry, I don’t know,”


## Implementing RAG

Today, LLM-powered chatbots can give customers more personalized answers without humans having to write out new scripts. And RAG allows LLMs to go one step further by greatly reducing the need to feed and retrain the model on **fresh examples**. Simply upload the **latest documents** or **policies**, and the model retrieves the information in open-book mode to answer the question.

RAG has two phases, retrieval and content generation:

### Retrieval

In the retrieval phase, algorithms search for and retrieve snippets of information relevant to the user’s prompt or question. In an open-domain, consumer setting, those facts can come from indexed documents on the internet; in a closed-domain, enterprise setting, a narrower set of sources are typically used for added security and reliability.

### Content generation

This assortment of external knowledge is appended to the user’s prompt and passed to the language model. In the generative phase, the LLM draws from the augmented prompt and its internal representation of its training data to synthesize an engaging answer tailored to the user in that instant. The answer can then be passed to a chatbot with links to its sources.






* [Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models]: https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/
[[Meta AI] Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/)


* [Retrieval Augmented Generation (RAG)]: https://www.promptingguide.ai/techniques/rag
[[Prompt Engineering Guide] Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag)


* [What is retrieval-augmented generation?]: https://research.ibm.com/blog/retrieval-augmented-generation-RAG
[[IBM Blog] What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)