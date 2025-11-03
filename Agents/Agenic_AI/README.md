
# Agentic AI

This document is a note from Udacity course **Agentic AI**.

## Common components of an AI Agent:

* **Large Language Model (LLM)**: The "brain" for understanding, reasoning, acting.
* **Tools**: External functions, APIs for interaction and enhanced capabilities.
* **Instructions**: Guidelines (system prompts) defining behavior and goals.
* **Memory**: Short-term (context) & Long-term (history) for learning and consistency.
* **Runtime/Orchestration Layer**: Manages execution flow, tool usage, observation processing.
 


## Chain-of-Thought (CoT) and ReAct

CoT and ReAct together helps agents to solve more complicated problems. The CoT-ReAct process has the following components:
* **Crafting Structured CoT Prompts**: You practiced writing a detailed Chain-of-Thought prompt that instructs an LLM to analyze multiple data sources and structure its reasoning to solve a complex problem.
* **Building a ReAct System Prompt**: You learned how to compose a comprehensive ReAct system prompt from scratch, defining the agent's role, the THINK/ACT cycle, a set of available tools, and a complete example to guide the agent's behavior.
* **Implementing the ReAct Orchestration Loop**: You wrote the Python code that serves as the agent's runtime, successfully parsing the AI's ACT responses and creating the observation loop that allows the agent to use tools and receive feedback.



### Scenario 1: 

A patient presents with a persistent cough and fatigue. Our goal is to determine the likely cause.

#### Approach A: The "All Data Upfront" CoT Method

One way to solve this is to give the AI a single, large prompt containing all the information we have about the patient and ask it to reason through the data.

```Python
system_prompt_cot = """
You are a diagnostic physician. 
Think step by step, correlating the symptoms with the provided patient data to form a differential diagnosis. 
Explain your reasoning.
"""

user_prompt_with_data = """
A patient presents with a persistent cough and fatigue.

Here is their patient chart:
- Age: 45
- History: Non-smoker, works indoors as an accountant. No recent travel.
- Lab Results: White blood cell count is slightly elevated.
- Vitals: Temperature is normal.

Based on all this information, what is the likely diagnosis?
"""

response = get_completion(system_prompt_cot, user_prompt_with_data)
print(response)
```

This is a **Chain-of-Thought** approach. We provide all the context and ask the model to "think step by step" to connect the dots. It's powerful, but it has a key limitation: it's static. What if we didn't have the lab results yet? We wouldn't be able to run the prompt.



#### Approach B: The Agentic ReAct Method

A more dynamic and powerful approach is to build an agent that can decide what information it needs and then go get it using tools. This is the **ReAct** framework in action.

Instead of one big prompt, we give the agent a role and access to tools:
* `order_lab_test`(test_name: str)
* `check_patient_history`(record_id: str)
* final_answer(diagnosis: str, reasoning: str)

Now, watch how the interaction unfolds turn-by-turn:
* **Interaction turn 1**
    * User: "A patient presents with a persistent cough and fatigue."
    * AI Assistant Response:
        * THINK: The symptoms 'cough' and 'fatigue' are non-specific. I need more information to form a hypothesis. I will start by ordering a standard blood panel (CBC) to check for signs of infection or other abnormalities.
        * ACT: `order_lab_test`(test_name="CBC")

    The system runs the `order_lab_test` tool and provides the result back to the agent.
* **Interaction turn 2**
    * System Observation: RESULTS: White blood cell count elevated.
    * AI Assistant Response:
        * THINK: The elevated white blood cell count suggests an underlying infection is likely. Given the respiratory symptom (cough), I should now investigate the lungs. I will order a chest X-ray.
        * ACT: `order_lab_test`(test_name="Chest X-Ray")
    
    Notice the difference. The ReAct agent is not passively analyzing a data file. It is actively participating in a diagnostic process, deciding what information is relevant at each step.




* [Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models]: https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/
[[Meta AI] Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/)


* [Retrieval Augmented Generation (RAG)]: https://www.promptingguide.ai/techniques/rag
[[Prompt Engineering Guide] Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag)


* [Retrieval Augmented Generation (RAG) for LLMs]: https://www.hopsworks.ai/dictionary/retrieval-augmented-generation-llm
[[HopsWorks] Retrieval Augmented Generation (RAG) for LLMs](https://www.hopsworks.ai/dictionary/retrieval-augmented-generation-llm)


* [What is retrieval-augmented generation?]: https://research.ibm.com/blog/retrieval-augmented-generation-RAG
[[IBM Blog] What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)