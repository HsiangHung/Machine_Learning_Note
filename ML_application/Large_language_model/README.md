
# Large Language Model

## What Was the First Large Language Model?

The first model that really caught people's attention was the GPT (Generative Pre-trained Transformer) model developed by OpenAI in 2018. The well-known ChatGPT is basically GPT-3.5.

The GPT model was one of the first language models to use the **transformer architecture**. This is a type of neural network that's great at understanding **long-range dependencies** in text data, which made it possible for the model to generate highly coherent and contextually relevant language output. With **117 million** parameters, the GPT model was a real game-changer for natural language processing.
Since then, we've seen the development of even larger and more impressive language models, like GPT-2, GPT-3, and BERT. [[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]

OpenAI's ChatGPT is a fine-tuned version of the base GPT model to make it more suitable for generating conversational responses. Examples of GPT models include GPT-2, GPT-3, and GPT-4. OpenAI’s ChatGPT is a large language model. 

There are other large language models. See [What’s the difference between a Large Language Model (LLM) and a General Pre-trained Transformer (GPT)?](https://www.brinwilson.com/whats-the-difference-between-a-large-language-model-llm-and-a-general-pre-trained-transformer-gpt/).



## Types of Pre-trained Large Language Models

The following table is summarized from Coursera course (Generative AI):

| Type | Model  | approach | objective | Use Case |  Model Example |
| --- | --- | --- | --- | --- | --- |
| Encoder Only | autoEncoding | masked language modeling (MLM), bidirectional | reconstruct test ("denoising")| sentiment analysis, name entity recognition, word classification | BERT, ROBERTA |
| Encoder-Decoder | sequence-to-sequence | span corruption | reconstruct span | translation, text summarization, Q&A | T5, BART |
| Decoder Only | autoregression | causal language modeling (CML), unidirectional  | predict next token | text generation | GPT, BLOOM | 

BERT utilizes a bi-directional transformer architecture, which means that it can process input text in both forward and backward directions to better understand the context and relationships between words.


## How Do Large Language Models Work?

The most well-known Large Language Model (LLM) architecture is the **transformer architecture** shown below (picture from the paper **Attention Is All You Need** [[Ashish Vaswani et al.]][Attention Is All You Need]). 

![transformer](images/transformer.png)

A typical Transformer model consists of four main steps [[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]:

### 1. Word Embedding 

[[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]

To give another example, let's consider the words "cat" and "dog". These two words will usually be closer to each other when compared to another pair of words, such as "cat" and "burgers. In word embedding, these words would be represented as vectors that are located close to each other in the vector space. 

Another example of trained Word2Vec Vectors with Semantic and Syntactic relationship is illustrated below (from [Word2Vec Research Paper Explained](https://towardsdatascience.com/word2vec-research-paper-explained-205cb7eecc30))

![word2vec](images/word_embedding.png)

Creating word embeddings involves training a neural network on a large corpus of text data, such as news articles or books. During training, the network learns to predict the likelihood of a word appearing in a given context based on the words that come before and after it in a sentence. The vectors that are learned through this process capture the semantic relationships between different words in the corpus.

### 2. Positional Encoding

[[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]

Positional encoding is all about helping the model figure out where words are in a sequence.  For example, when translating a sentence like "The cat is on the mat" to another language, it's crucial to know that "cat" comes before "mat".

The position embeddings are computed as [[Data Science StackExchange]][What is the positional encoding in the transformer model?]

$$PE_{(pos, 2i)} = \sin \Big( \frac{pos}{10000^{\frac{2i}{d}}} \Big),$$

where $pos$ refers to the position of the “word” in the sequence, $d$ means the size of the word/token embedding, and $i$ refers to each of the 5 individual dimensions of the embedding (i.e. 0, 1,2,3,4).

* [A Gentle Introduction to Positional Encoding in Transformer Models, Part 1]: https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/#:~:text=Positional%20encoding%20describes%20the%20location,item%27s%20position%20in%20transformer%20models.
[[Jason Brownlee] A Gentle Introduction to Positional Encoding in Transformer Models, Part 1](https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/#:~:text=Positional%20encoding%20describes%20the%20location,item%27s%20position%20in%20transformer%20models.)
* [What is the positional encoding in the transformer model?]: https://datascience.stackexchange.com/questions/51065/what-is-the-positional-encoding-in-the-transformer-model
[[Data Science StackExchange] What is the positional encoding in the transformer model?](https://datascience.stackexchange.com/questions/51065/what-is-the-positional-encoding-in-the-transformer-model)



### 3. Transformers

[[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]

Advanced large language models utilize a certain architecture known as Transformers. The transformer layer is often added as an additional layer to the traditional neural network architecture to improve the LLM's ability to model long-range dependencies in natural language text.

The transformer layer works by processing the entire input sequence **in parallel** rather than sequentially. It consists of two essential components: 
1. **self-attention mechanism**: The self-attention mechanism allows the model to assign a weight to each word in the sequence, depending on how valuable it is for the prediction. This enables the model to capture the relationships between words, regardless of their distance from each other.

2. **feedforward neural network**: After the self-attention layer finishes processing the sequence, the position-wise feed-forward layer takes in each position in the input sequence and processes it independently. For each position, a fully connected layer takes in a vector representation of the token (word or subword) at that position. This vector representation is the output from the preceding self-attention layer.

During training, the transformer layer's weights are updated repeatedly to reduce the difference between the predicted output and the actual output. This is done through the backpropagation algorithm, which is similar to the training process for traditional neural network layers.

### 4. Text  Generation

[[Mostafa Ibrahim]][An Overview of Large Language Models (LLMs)]

After the LLM has been trained and fine-tuned, the model can be used to generate highly sophisticated text in response to a prompt or question. The model is typically "primed" with a seed input, which can be a few words, a sentence, or even an entire paragraph. The LLM then uses its learned patterns to generate a coherent and contextually-relevant response.

Text generation relies on a technique called autoregression, where the model generates each word or token of the output sequence one at a time based on the previous words it has generated. The model uses the parameters it has learned during training to calculate the probability distribution of the next word or token and then selects the most likely choice as the next output.


* [An Overview of Large Language Models (LLMs)]: https://wandb.ai/mostafaibrahim17/ml-articles/reports/An-Overview-of-Large-Language-Models-LLMs---VmlldzozODA3MzQz
[[Mostafa Ibrahim] An Overview of Large Language Models (LLMs)](https://wandb.ai/mostafaibrahim17/ml-articles/reports/An-Overview-of-Large-Language-Models-LLMs---VmlldzozODA3MzQz)


* [Attention Is All You Need]: https://arxiv.org/abs/1706.03762
[[Ashish Vaswani et al.] Attention Is All You Need](https://arxiv.org/abs/1706.03762)


## LLMs Comparison


* Context Length: Context length refers to the number of tokens a language model can process. The longer the context length, the more information and the richer the context the model has for generating a response [[LinkedIn, Arun Kesavan]][Understanding the Context Length Hitch with GPT Models].

| Model | Parameter  | Context Length |  
| --- | --- | --- | 
| GPT3 | [175 billion](https://towardsdatascience.com/gpt-4-is-here-is-it-really-changing-the-game-for-language-ai-e49eb2d5022b#:~:text=The%20legend%20says%20that%20GPT,as%20input%2C%20not%20only%20text.) | 4,096 tokens | 
| GPT4 | [100 trillion](https://towardsdatascience.com/gpt-4-is-here-is-it-really-changing-the-game-for-language-ai-e49eb2d5022b#:~:text=The%20legend%20says%20that%20GPT,as%20input%2C%20not%20only%20text.) | 32,768 tokens |
| Claude (Anthropic AI) | | 100,000 tokens | 
| CodeT5+ (Salesforce)   | | | 
| LLaMa 1 (7B, 13B, 33B, 65B) | | 2,000 tokens | 
| LLaMa 2 (7B, 13B, 34B, 70B) | | 4,000 tokens | 
| Flacon () | |  tokens | 
|Flan-T5 (80M, 250M, 780M, )| | |


* [Understanding the Context Length Hitch with GPT Models]: https://www.linkedin.com/pulse/understanding-context-length-hitch-gpt-models-arun-kesavan/
[[LinkedIn, Arun Kesavan] Understanding the Context Length Hitch with GPT Models](https://www.linkedin.com/pulse/understanding-context-length-hitch-gpt-models-arun-kesavan/)



## Fine-Tuning 



1. **Instruction fine-tuning**: Instruction fine-tuning, where **all** of the model's weights are updated is known as **full fine-tuning**. The process results in a **new version** of the model with **updated weights**. It is important to note that just like pre-training, full fine tuning requires enough memory and compute budget to store and process all the gradients, optimizers and other components that are being updated during training [[Coursera, Generative AI with Large Language Models] ][Week2 Instruction fine-tuning]. 

* [Week2 - Instruction fine-tuning]: https://www.coursera.org/learn/generative-ai-with-llms/lecture/exyNC/instruction-fine-tuning
[[Coursera, Generative AI with Large Language Models] Week2 - Instruction fine-tuning](https://www.coursera.org/learn/generative-ai-with-llms/lecture/exyNC/instruction-fine-tuning)


## LLaMa

LLaMa 2, an updated version of LlaMa 1, trained on a new mix of publicly available data. We also increased the size of the pretraining corpus by 40%, doubled the context length of the model, and adopted grouped-query attention (Ainslie et al., 2023). We are releasing variants of LLaMa 2 with 7B, 13B, and 70B parameters. See [Meta AI page](https://ai.meta.com/llama/)


We can perform inference of LLaMA model in pure C/C++ code. Intsall LLaMa 2 in M1/M2 chip Mac:
* [Tutorial: Install a Chat Large Language Model (LLM) on your M1/M2 Mac](https://www.youtube.com/watch?v=rStOK2FfyEY)
* [How to install LLaMA on Mac (llama.cpp)](https://agi-sphere.com/install-llama-mac/#Step_1_Install_Homebrew)


Fine-tuning on LLaMa 2:

* [Youtube - Tutorial on LLaMa 2 and How to Fine-tune It]: https://www.youtube.com/watch?v=ntJUXgaTJIM
[[Junling Hu] Youtube -  Tutorial on LLaMa 2 and How to Fine-tune It](https://www.youtube.com/watch?v=ntJUXgaTJIM)



