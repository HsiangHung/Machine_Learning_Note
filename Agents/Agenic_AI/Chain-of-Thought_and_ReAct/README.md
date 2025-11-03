
# Chain-of-Thought and ReACT Prompting

CoT and ReAct together build AI agents to solve more complicated problems. 

The CoT-ReAct process has the following components:
* **Crafting Structured CoT Prompts**: You practiced writing a detailed Chain-of-Thought prompt that instructs an LLM to analyze multiple data sources and structure its reasoning to solve a complex problem.
* **Building a ReAct System Prompt**: You learned how to compose a comprehensive ReAct system prompt from scratch, defining the agent's role, the THINK/ACT cycle, a set of available tools, and a complete example to guide the agent's behavior.
* **Implementing the ReAct Orchestration Loop**: You wrote the Python code that serves as the agent's runtime, successfully parsing the AI's ACT responses and creating the observation loop that allows the agent to use tools and receive feedback.

Working with CoT and ReAct requires careful thought and well-structured code. You have now experienced how to make an AI not just generate text, but perform methodical reasoning and take action to solve problems.

Below we show a scenario by comparing the CoT + ReAct technique and one-shot LLM prompt.

## Scenario
A patient presents with a persistent cough and fatigue. Our goal is to determine the likely cause.

### Approach A: The "All Data Upfront" CoT Method

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



### Approach B: The Agentic ReAct Method

A more dynamic and powerful approach is to build an agent that can decide what information it needs and then go get it using tools. This is the **ReAct** framework in action.

Instead of one big prompt, we give the agent a role and access to tools:
* `order_lab_test`(test_name: str)
* `check_patient_history`(record_id: str)
* `final_answer`(diagnosis: str, reasoning: str)

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



## Craft the ReAct System Prompt

When using the ReACT technique, you'll need to create a comprehensive system prompt that **teaches an AI agent** how to use the ReAct framework. This is the most important part of building a **ReAct agent**, as this single prompt sets the rules, defines the tools, and teaches the AI how to "think."

A good ReAct system prompt has four key parts:
1. The Role and Goal: Who is the agent? What is its purpose?
2. The THINK/ACT Instruction: How must the agent format its reasoning and actions?
3. The Tool Definitions: What tools can the agent use, and how do they work?
4. A Complete Example: A full example of a multi-turn interaction.


Let's break down how to build such a prompt in a more concrete way.

### Scenario: We need an AI agent to help a logistics coordinator track a delayed shipment. 

Let's build the prompt piece by piece.
1. **Define the Role and Goal**: We start by telling the agent its identity and overall mission.
```Python
"""
You are a Supply Chain Logistics Coordinator. 
Your goal is to diagnose shipment delays by gathering information from different systems.
"""
```

2. **Explain the THINK/ACT Cycle**: Next, we give it explicit instructions on how to structure its response. This is the core of the ReAct framework.
```Python
"""
You must use a step-by-step reasoning process. For each step, respond with a single THINK/ACT message.

THINK: First, you will reason about the problem and determine the next logical action to take.
ACT: Based on your thought process, you will call ONE of the available tools.
"""
```

3. **Define the Available Tools**: You must clearly list every tool the agent can use. For each tool, you must provide its name, its parameters, a short description, and an example of its input (ACT) and output (OBSERVE).
```Python
"""
---
## Available Tools

1.  get_shipment_status(tracking_id: str)
    * Use this to get the last known location and status of a shipment.
    * Example Input: `ACT: get_shipment_status(tracking_id="XYZ123")`
    * Example Output: `OBSERVE: {"status": "Delayed", "location": "Chicago Rail Yard"}`

2.  check_facility_alerts(facility_name: str)
    * Use this to check for operational alerts (e.g., weather delays, closures) at a specific facility.
    * Example Input: `ACT: check_facility_alerts(facility_name="Chicago Rail Yard")`
    * Example Output: `OBSERVE: {"alert": "Severe Weather Alert: All operations suspended."}`

3.  final_answer(summary: str)
    * Use this tool ONLY when you have diagnosed the problem and can provide a complete summary.
    * Example Input: `ACT: final_answer(summary="Shipment XYZ123 is delayed in Chicago due to a severe weather-related closure at the rail yard.")`
"""
```

4. **Provide a Complete Example Interaction**: Finally, you put it all together by showing the agent a complete, multi-step example of how to use these components to solve a problem. This few-shot example is often the most effective way for the agent to learn the pattern.

```Python
"""
---
## Example

**User:** Find out why shipment XYZ123 is delayed.

**AI Assistant:**
THINK: I need to find out why shipment XYZ123 is delayed. My first step is to get the current status and location of the shipment using the `get_shipment_status` tool.
ACT: get_shipment_status(tracking_id="XYZ123")

**(System provides `OBSERVE: {"status": "Delayed", "location": "Chicago Rail Yard"}` and the AI continues...)**
"""
```

When you combine all four of these parts, you get a system prompt that gives the AI everything it needs to begin its task.




