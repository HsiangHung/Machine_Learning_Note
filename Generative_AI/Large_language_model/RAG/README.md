
# Retrieval-Augmented Generation (RAG)


## What Is (RAG)?


Large language models can be inconsistent: Sometimes they nail the answer to questions, other times they regurgitate random facts from their training data. If they occasionally sound like they have no idea what they’re saying, it’s because they don’t. LLMs know how words relate statistically, but not what they mean [[IBM Blog]][What is retrieval-augmented generation?].

RAG is an AI framework for retrieving facts from an external knowledge base to ground large language models (LLMs) on the most accurate, up-to-date information and to give users insight into LLMs' generative process [[IBM Blog]][What is retrieval-augmented generation?]. 

## Benfit Using RAG

Implementing RAG in an LLM-based question answering system has the following main benefits: 
1. It ensures that the model has access to the most current, reliable facts, and that users have access to the model’s sources, ensuring that its claims can be checked for accuracy and ultimately trusted.
2. By grounding an LLM on a set of external, verifiable facts, the model has fewer opportunities to pull information baked into its parameters. This reduces the chances that an LLM will leak sensitive data, or ‘hallucinate’ incorrect or misleading information.
3. RAG also reduces the need for users to continuously train the model on new data and update its parameters as circumstances evolve. In this way, RAG can lower the computational and financial costs of running LLM-powered chatbots in an enterprise setting. 


By [[IBM Blog]][What is retrieval-augmented generation?]: “It’s the difference between an open-book and a closed-book exam.” In a RAG system, you are asking the model to respond to a question by browsing through the content in a book, as opposed to trying to remember facts from memory.



## Use Case

Alice, has learned that her son’s school will have early dismissal on Wednesdays for the rest of the year. She wants to know if she can take vacation in half-day increments and if she has enough vacation to finish the year.

To craft its response, the LLM first pulls data from Alice’s HR files to find out how much vacation she gets as a longtime employee, and how many days she has left for the year. It also searches the company’s policies to verify that her vacation can be taken in half-days. These facts are injected into Alice’s initial query and passed to the LLM, which generates a concise, personalized answer. A chatbot delivers the response, with links to its sources.


## Implementing RAG

Today, LLM-powered chatbots can give customers more personalized answers without humans having to write out new scripts. And RAG allows LLMs to go one step further by greatly reducing the need to feed and retrain the model on **fresh examples**. Simply upload the **latest documents** or **policies**, and the model retrieves the information in open-book mode to answer the question.

RAG has two phases: 
1. retrieval
2. content generation. 

### Retrieval

In the retrieval phase, algorithms search for and retrieve snippets of information relevant to the user’s prompt or question. In an open-domain, consumer setting, those facts can come from indexed documents on the internet; in a closed-domain, enterprise setting, a narrower set of sources are typically used for added security and reliability.

### Content generation

This assortment of external knowledge is appended to the user’s prompt and passed to the language model. In the generative phase, the LLM draws from the augmented prompt and its internal representation of its training data to synthesize an engaging answer tailored to the user in that instant. The answer can then be passed to a chatbot with links to its sources.





* [What is retrieval-augmented generation?]: https://research.ibm.com/blog/retrieval-augmented-generation-RAG
[[IBM Blog] What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)