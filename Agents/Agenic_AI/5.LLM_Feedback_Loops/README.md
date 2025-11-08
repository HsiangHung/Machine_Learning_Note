# 5. LLM Feedback Loops

$${\color{red}The \space content \space here \space corresponds \space to \space Sec \space 11-12 \space of \space Udacity \space **Agentic \space AI** \space course.}$$


## Sources of Feedback for LLMs:

The core mechanism is prompt chaining. The output of one step becomes input for the next. In a feedback loop, the `feedback` from evaluating an LLM's output is incorporated into a new prompt for the next iteration, guiding the model towards a better result:

* **Self-Correction**: Prompt the LLM to evaluate its own previous response based on your criteria. For example, asking the same LLM to review our coffee email for politeness and then correct it. Its suggestions become feedback for the next iteration.
* **External Tools**: If it generates code, running that code and getting errors or test results provides concrete feedback.
* **Validation Checks**: Programmatic checks. If extracting info into JSON, code can parse the output and check validity or missing fields. The result (e.g., "Missing 'email_address' field") becomes feedback.
* **User Input**: Direct feedback. A user might say, "This itinerary doesn't include any outdoor activities." This is sent back to the LLM agent to regenerate. A blocking tool call can wait for user input.

Building the loop is the first step; knowing if it's working is next! Monitoring helps you:
* **Evaluate effectiveness**: Are outputs improving? Converging to the desired result?
* **Debug Issues**: If stuck in a loop or outputs worsen, monitoring helps identify why. Inspect prompts, intermediate outputs, and feedback.
* **Optimize Process**: Find if outputs stop improving after a certain number of iterations or if the process is too long.



## Metrics for Success: What to Monitor?

* **Output Quality**: Subjective (politeness, assessed manually or by an evaluator LLM during development) or objective (error rate, closeness to target format/content for code generation or data extraction).
* **Error Rate**: For tasks with objective criteria.
* **Goal Adherence**: How close is the current output to the overall objective? Are all initial requirements met?
* **Step-by-step Trace (Log)**: Crucial. What was the prompt for each step? LLM's response? Feedback generated? This detailed log is invaluable for understanding the agent's "thought" process and debugging.




## Feedback Loop Example

### Scenario
We need an AI to generate the HTML and CSS for a simple, styled user profile card.

### Step 1: The Initial (Flawed) Generation

First, we'll give the AI a prompt with our initial request.

```Python
# The initial prompt for the profile card
prompt_initial = """
You are a web developer. Generate the HTML and CSS for a user profile card.
It should have:
- A container with a light grey background and a subtle shadow.
- An avatar image placeholder.
- The user's name and title below the avatar.
"""

# Let's assume we call the LLM and get a response
# initial_code = get_completion(prompt_initial)
# print(initial_code)
```

**Likely (Flawed) Output**: Let's imagine the AI returns code that is functional but has a design flaw. For example, maybe it forgets to center the text, making the card look unprofessional.


### Step 2: The Feedback Mechanism

Instead of fixing the CSS ourselves, we will act as a code reviewer and provide feedback. In a real application, this feedback could come from an automated linter, a visual regression test, or, as we'll see in the exercise, a suite of unit tests.

For this demonstration, our feedback will be a simple, natural language description of the problem:

```Python
# The feedback describes the problem with the initial code
feedback = "The generated code is a good start, but it has a design flaw: The user's name and title text are not centered within the card. Please fix the CSS to center-align the text."
```

### Step 3: The Feedback Loop (The Corrective Prompt)

Now for the most important part. We will create a new prompt that includes both the AI's original, flawed code and our specific feedback.

```Python
# A new prompt that asks the AI to revise its own work
prompt_corrective = f"""
You are a web developer. You previously generated some code that had an error.
Please revise the code to fix the issue described in the feedback.

Your previous code:
---
<HTML_AND_CSS_FROM_INITIAL_CODE>
---

Feedback on your code:
---
{feedback}
---

Please provide the complete, corrected HTML and CSS.
"""

# The AI now receives its own work plus our correction
# corrected_code = get_completion(prompt_corrective)
# print(corrected_code)
```

**Likely Output**: The AI now returns a corrected version of the code where the CSS text-align: center; property has been correctly applied.

This simple loop—`Generate` -> `Evaluate` -> `Feedback` -> `Revise` —is the foundation of creating self-improving AI systems.

Next, you will build an automated loop where the "feedback" comes from a suite of Python unit tests, creating an agent that can iteratively debug its own code until it passes all the tests.

