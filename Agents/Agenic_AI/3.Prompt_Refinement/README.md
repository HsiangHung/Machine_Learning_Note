# 3. Prompt Instruction Refinement

$${\color{red}The \space content \space here \space corresponds \space to \space Sec. \space 7-8 \space of \space Udacity \space **Agentic \space AI** \space course.}$$


## From Vague Ideas to Precise Instructions

Start simple prompts, test and refine based on the results

* **Systematic Prompt Analysis**: You can now look at a prompt, identify its different parts (Role, Task, Context, Examples, Output Format), and pinpoint areas that need improvement.
* **Iterative Prompt Development**: You've practiced the core technique of making targeted changes, testing, and building upon your prompts to steadily enhance the AI's output. 
This includes:
    - **Assigning Roles** for specialized behavior.
    - **Enriching Context** to give the AI the knowledge and rules it needs.
    - **Clarifying Tasks** to remove doubt about the AI's objective.
    - **Controlling Output Formats** for structured and useful information.
    - **Guiding with Examples** (Few-Shot Prompting) to demonstrate desired responses.
* **Troubleshooting AI Outputs**: By understanding prompt components, you're better equipped to figure out why an AI might not be giving you the response you want and how to fix it by adjusting the prompt.


## Scenario

We need an AI to categorize incoming customer support emails for an automated ticketing system.

### Attempt 1: The Vague Prompt

Let's start with a simple, vague prompt and see what we get.

```Python
# The customer's email
customer_email = """
Hi, I'm writing because I was charged twice for my last order (Order #8675309).
I thought my subscription was paused. Can you please look into this and reverse the extra charge?
Thanks,
Alex
"""

# The vague system and user prompts
system_prompt_vague = "You are a helpful assistant."
user_prompt_vague = f"Please categorize the following email:\n\n{customer_email}"

# Let's see the likely response
# response = get_completion(system_prompt_vague, user_prompt_vague)
# print(response)
```

**Likely Output**: This email appears to be a billing issue related to a double charge on an order.

This response is correct, but it's not very useful for an automated system. A downstream program can't easily parse this sentence to create a support ticket, assign it to the right department, or set its priority. We need more structure.

### Attempt 2: The Refined, Structured Prompt
Now, let's refine our instructions:
* We will add a specific Role,
* clear Task instructions
* with Context (definitions of the categories),
* and a required Output Format (JSON).

```Python
system_prompt_refined = """
You are an expert customer support agent responsible for categorizing incoming emails for a ticketing system.

Your task is to analyze the user's email and provide a structured JSON output.

## Email Categories:
- **Billing:** For issues related to charges, subscriptions, or refunds.
- **Technical Support:** For problems with product functionality or bugs.
- **General Inquiry:** For questions that do not fit the other categories.

## Output Format:
You must respond with a single JSON object containing the following keys:
- `category`: (string) One of "Billing", "Technical Support", or "General Inquiry".
- `summary`: (string) A one-sentence summary of the user's issue.
- `urgency`: (string) "High", "Medium", or "Low".
- `customer_id`: (string) Extract the order number or customer ID if available, otherwise "N/A".
"""

user_prompt_refined = f"Please analyze and categorize this email:\n\n{customer_email}"

# response = get_completion(system_prompt_refined, user_prompt_refined)
# print(response)
```

**Likely Output**:
```json
{
  "category": "Billing",
  "summary": "The customer was charged twice for order #8675309 and is requesting a refund for the extra charge.",
  "urgency": "High",
  "customer_id": "8675309"
}
```
