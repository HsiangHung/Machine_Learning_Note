
# Large Language Model


* Context Length: Context length refers to the number of tokens a language model can process. The longer the context length, the more information and the richer the context the model has for generating a response [[LinkedIn, Arun Kesavan]][Understanding the Context Length Hitch with GPT Models].

| Model |  Context Length |  
| --- | --- | 
| ChatGPT | 4,096 tokens | 
| GPT4 | 32,768 tokens |
| Claude (Anthropic AI) | 100,000 tokens | 
| CodeT5+ (Salesforce)   | 3. softmax regression | 



* [Understanding the Context Length Hitch with GPT Models]: https://www.linkedin.com/pulse/understanding-context-length-hitch-gpt-models-arun-kesavan/
[[LinkedIn, Arun Kesavan] Understanding the Context Length Hitch with GPT Models](https://www.linkedin.com/pulse/understanding-context-length-hitch-gpt-models-arun-kesavan/)



## Fine-Tuning 



1. **Instruction fine-tuning**: Instruction fine-tuning, where **all** of the model's weights are updated is known as **full fine-tuning**. The process results in a **new version** of the model with **updated weights**. It is important to note that just like pre-training, full fine tuning requires enough memory and compute budget to store and process all the gradients, optimizers and other components that are being updated during training [[Coursera, Generative AI with Large Language Models] ][Week2 Instruction fine-tuning]. 

* [Week2 - Instruction fine-tuning]: https://www.coursera.org/learn/generative-ai-with-llms/lecture/exyNC/instruction-fine-tuning
[[Coursera, Generative AI with Large Language Models] Week2 - Instruction fine-tuning](https://www.coursera.org/learn/generative-ai-with-llms/lecture/exyNC/instruction-fine-tuning)


## LlaMa

Intsall LlaMa 2 in M1/M2 chip Mac:
* [Tutorial: Install a Chat Large Language Model (LLM) on your M1/M2 Mac](https://www.youtube.com/watch?v=rStOK2FfyEY)
* [How to install LLaMA on Mac (llama.cpp)](https://agi-sphere.com/install-llama-mac/#Step_1_Install_Homebrew)


Fine-tuning on LlaMa 2:

* [Youtube - Tutorial on Llama 2 and How to Fine-tune It]: https://www.youtube.com/watch?v=ntJUXgaTJIM
[[Junling Hu] Youtube -  Tutorial on Llama 2 and How to Fine-tune It](https://www.youtube.com/watch?v=ntJUXgaTJIM)



## LangChain

### What is LangChain?

[[Mostafa Ibrahim]][What is LangChain? — A 101 overview]

LangChain is a library that helps developers build applications powered by large language models (LLMs). It does this by providing a framework for connecting LLMs to other sources of data, such as the internet or your personal files. This allows developers to chain together multiple commands to create more complex applications.

LLMs are complex models that can be difficult to use directly. LangChain provides a simple interface that makes it easy to connect LLMs to your application.


### Examples of LangChain applications

There are many different ways that LangChain can be used to build applications. Here are a few examples [[Mostafa Ibrahim]][What is LangChain? — A 101 overview]:
* **Chatbots**: LangChain can be used to create chatbots that are powered by LLMs. These chatbots can be used to provide customer service, answer questions, or even generate creative content.
* **Question-answering systems**: LangChain can be used to create question-answering systems that are powered by LLMs. These systems can be used to answer questions about a wide range of topics
* **Summarization systems**: LangChain can be used to create summarization systems that are powered by LLMs. These systems can be used to summarize long pieces of text, such as articles or books.
* **Code generation systems**: LangChain can be used to create code generation systems that are powered by LLMs. These systems can be used to generate code for a variety of programming languages.


### Reference

* [What is LangChain? Why Use LangChain?]: https://www.einblick.ai/blog/what-is-langchain-why-use-it/#:~:text=At%20a%20high%20level%2C%20LangChain,way%20to%20build%20user%20interfaces.
[[Paul Yang, Einblick] What is LangChain? Why Use LangChain?](https://www.einblick.ai/blog/what-is-langchain-why-use-it/#:~:text=At%20a%20high%20level%2C%20LangChain,way%20to%20build%20user%20interfaces.)


* [What is LangChain? — A 101 overview]: https://medium.com/the-techlife/what-is-langchain-a-101-overview-c2bed339b08f
[[Mostafa Ibrahim] What is LangChain? — A 101 overview](https://medium.com/the-techlife/what-is-langchain-a-101-overview-c2bed339b08f)








