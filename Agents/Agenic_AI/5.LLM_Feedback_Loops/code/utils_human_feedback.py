# from enum import Enum
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr


def execute_code(code, test_cases):
    """
    Executes Python code and returns the results of test cases.
    Args:
        code: String containing Python code
        test_cases: List of dictionaries with inputs and expected outputs
    Returns:
        Dictionary containing execution results and test outcomes
    """
    results = {"execution_error": None, "test_results": [], "passed": 0, "failed": 0}

    # Create a namespace for execution
    namespace = {}

    # Capture stdout and stderr
    output_buffer = io.StringIO()

    try:
        with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
            exec(code, namespace)

        # Run test cases
        for i, test in enumerate(test_cases):
            inputs = test["inputs"]
            expected = test["expected"]

            # Execute the function with test inputs
            try:
                if isinstance(inputs, dict):
                    actual = namespace["process_data"](**inputs)
                else:
                    actual = namespace["process_data"](*inputs)

                passed = actual == expected

                if passed:
                    results["passed"] += 1
                else:
                    results["failed"] += 1

                results["test_results"].append(
                    {
                        "test_id": i + 1,
                        "inputs": inputs,
                        "expected": expected,
                        "actual": actual,
                        "passed": passed,
                    }
                )
            except Exception as e:
                # If the error is the expected type, mark as passed
                passed = isinstance(expected, type) and isinstance(e, expected)
                results["test_results"].append(
                    {
                        "test_id": i + 1,
                        "inputs": inputs,
                        "expected": expected,
                        "error": str(e),
                        "passed": passed,
                    }
                )
                if passed:
                    results["passed"] += 1
                else:
                    results["failed"] += 1

    except Exception as e:
        results["execution_error"] = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc(),
        }

    results["stdout"] = output_buffer.getvalue()
    return results


# Function to format test results as feedback for the model
def format_feedback(results):
    """
    Formats test results into a clear feedback string for the model.
    Args:
        results: Dictionary containing execution results
    Returns:
        Formatted feedback string
    """
    feedback = []

    if results["execution_error"]:
        feedback.append(
            f"ERROR: Code execution failed with {results['execution_error']['error_type']}"
        )
        feedback.append(f"Message: {results['execution_error']['error_message']}")
        feedback.append("Traceback:")
        feedback.append(results["execution_error"]["traceback"])
        feedback.append("\nPlease fix the syntax or runtime errors in the code.")
        return "\n".join(feedback)

    feedback.append(
        f"Test Results: {results['passed']} passed, {results['failed']} failed"
    )

    if results["stdout"]:
        feedback.append(f"\nStandard output:\n{results['stdout']}")

    if results["failed"] > 0:
        feedback.append("\nFailed Test Cases:")
        for test in results["test_results"]:
            if not test.get("passed"):
                feedback.append(f"\nTest #{test['test_id']}:")
                feedback.append(f"  Inputs: {test['inputs']}")
                feedback.append(f"  Expected: {test['expected']}")
                if "actual" in test:
                    feedback.append(f"  Actual: {test['actual']}")
                if "error" in test:
                    feedback.append(f"  Error: {test['error']}")

    return "\n".join(feedback)
