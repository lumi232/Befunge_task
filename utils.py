import openai
import os
from openapiKEY import api_key
# Set your OpenAI API key
openai.api_key = api_key
 # Ensure your API key is set in your environment variables

def generate_befunge_code(output, original_code):
    """Generate a shorter Befunge code for the same desired output using few-shot prompting."""
    few_shot_examples = (
        "Here is an example of Befunge code generation:\n"
        "Input: 'Hello, World!'\n"
        "Code: >25*""!dlroW ,olleH"",@\n\n"
        "Input: '123'\n"
        "Code: >321,@\n\n"
        "Input: 'Hello\\nWorld'\n"
        "Code: >dlroW ,olleH@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Input: '123\\n456'\n"
        "Code: >654\\n321,@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Now, given the following input, write Befunge code:\n"
    )

    prompt = (
        f"{few_shot_examples}Input: '{output}'\n\n"
        f"Original Code: {original_code}\n\n"
        "Write a shorter Befunge code that produces the same output using fewer non-whitespace characters. Only provide the code, nothing else."
    )

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in esoteric programming languages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def generate_first_befunge_code(output):
    """Generate Befunge code for a desired output using few-shot prompting."""
    few_shot_examples = (
        "Here is an example of Befunge code generation:\n"
        "Input: 'Hello, World!'\n"
        "Code: >25*""!dlroW ,olleH"",@\n\n"
        "Input: '123'\n"
        "Code: >321,@\n\n"
        "Input: 'Hello\\nWorld'\n"
        "Code: >dlroW ,olleH@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Input: '123\\n456'\n"
        "Code: >654\\n321,@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Now, given the following input, write Befunge code:\n"
    )

    prompt = (
        f"{few_shot_examples}Input: '{output}'\n\n"
        "Write Befunge code that produces the same output. Only provide the code, nothing else."
    )

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in esoteric programming languages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def run_befunge_code(code):
    """
    Runs the Befunge code using the Befunge interpreter and captures its output,
    removing extra spaces between characters. Times out after 5 seconds if execution takes too long.
    """
    import subprocess
    import tempfile

    # Write the Befunge code to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bf") as temp_file:
        temp_file.write(code.encode())
        temp_file_path = temp_file.name

    try:
        # Run the Befunge interpreter with a timeout
        result = subprocess.run(
            ["python2", "BefungeInterpreter.py", temp_file_path],
            capture_output=True,
            text=True,
            timeout=5  # Timeout in seconds
        )
        # Extract output and remove spaces after each character
        output = result.stdout
        output = ''.join(output[i] for i in range(len(output)) if i % 2 == 0)
        return output
    except subprocess.TimeoutExpired:
        return "Execution timed out"
    except Exception as e:
        print(f"Error running Befunge interpreter: {e}")
        return None


def correct_befunge_code(current_code, desired_output, actual_output):
    """Generate corrected Befunge code for the same desired output using few-shot prompting."""
    few_shot_examples = (
        "Here is an example of correcting Befunge code:\n"
        "Current Code: >25*\"!dlroW ,olleH\",@\n"
        "Actual Output: 'dlroW ,olleH'\n"
        "Desired Output: 'Hello, World!'\n"
        "Corrected Code: >25*\"!dlroW ,olleH\",@\n\n"
        "Current Code: >321,@\n"
        "Actual Output: '321'\n"
        "Desired Output: '123'\n"
        "Corrected Code: >123,@\n\n"
        "Current Code: >dlroW ,olleH@\"\n"
        "v\n"
        "@\n"
        ">\n"
        "Actual Output: 'dlroW\nHello'\n"
        "Desired Output: 'Hello\nWorld'\n"
        "Corrected Code: >dlroW ,olleH@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Current Code: >654\\n321,@\"\n"
        "v\n"
        "@\n"
        ">\n"
        "Actual Output: '654\\n321'\n"
        "Desired Output: '123\\n456'\n"
        "Corrected Code: >123\\n456,@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Now, given the following details, provide the corrected Befunge code:\n"
    )

    prompt = (
        f"{few_shot_examples}Current Code: {current_code}\n"
        f"Actual Output: {actual_output}\n"
        f"Desired Output: {desired_output}\n\n"
        "Correct the code to produce the desired output. Only provide the code, nothing else."
    )

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in esoteric programming languages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def count_non_whitespace_characters(code):
    """Count all non-whitespace characters in the given Befunge code."""
    return sum(1 for char in code if not char.isspace())

def generate_safe_befunge_code_after_timeout(output):
    """
    Generate Befunge code for a desired output, ensuring it avoids infinite loops.
    
    Args:
    - output: Desired output as a string.
    
    Returns:
    - Corrected Befunge code as a string.
    """
    few_shot_examples = (
        "Here is an example of Befunge code generation:\n"
        "Input: 'Hello, World!'\n"
        "Code: >25*\"!dlroW ,olleH\",@\n\n"
        "Input: '123'\n"
        "Code: >321,@\n\n"
        "Input: 'Hello\\nWorld'\n"
        "Code: >dlroW ,olleH@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
        "Input: '123\\n456'\n"
        "Code: >654\\n321,@\"\n"
        "v\n"
        "@\n"
        ">\n\n"
    )

    issue_description = (
        f"The Befunge interpreter entered an infinite loop while executing the provided code. "
        f"Please write Befunge code that avoids infinite loops and correctly outputs: '{output}'.\n\n"
    )

    prompt = (
        f"{few_shot_examples}"
        f"Now, given the following scenario, write Befunge code:\n"
        f"{issue_description}"
        "Only provide the corrected code, nothing else."
    )

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in esoteric programming languages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content


