import openai
import os
from openapiKEY import api_key
# Set your OpenAI API key
openai.api_key = api_key
 # Ensure your API key is set in your environment variables

def generate_befunge_code(output, original_code):
    """Generate a shorter Befunge code for the same desired output."""
    prompt = (
        f"Here is Befunge code that outputs '{output}':\n\n{original_code}\n\n"
        "Write a shorter Befunge code that produces the same output using fewer characters. Only provide the code nothing else"
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
    """Generate Befunge code for a desired output."""
    prompt = f"Write Befunge code that outputs : {output}. Only provide the code nothing else. Dont Explain the code I only want the code as the output"
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
    """Generate a shorter Befunge code for the same desired output."""
    prompt = (
        f"Your code {current_code} outputs {actual_output} I want {desired_output}"
        "Only provide the code nothing else"
    )
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in esoteric programming languages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

