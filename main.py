from utils import generate_befunge_code, generate_first_befunge_code, run_befunge_code, correct_befunge_code, count_non_whitespace_characters, generate_safe_befunge_code_after_timeout

file_path = "desired_output.txt"

try:
    with open(file_path, "r") as file:
        desired_output = file.read().strip()  # Read and strip unnecessary whitespace
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit(1)

iteration = 0
threshold = 5
max_iteration = 20

prev_code = generate_first_befunge_code(desired_output)
previous_character_count = len(prev_code)

output_code = "Sorry, I couldn't find a code for your requested output"
print(f"Initial Code: {prev_code}")

while True:
    if(iteration == max_iteration):
        break
    iteration += 1
    print(f"\nIteration {iteration}:")

    # Count characters in the Befunge code
    current_character_count = count_non_whitespace_characters(prev_code)
    print(f"Character Count: {current_character_count}")

    # Run the Befunge code and verify the output
    actual_output = run_befunge_code(prev_code)
    print(f"Actual Output: {actual_output}")

    if actual_output != desired_output:
        print("Output does not match the desired output.")
        if actual_output == "Execution timed out":
            current_code = generate_safe_befunge_code_after_timeout(desired_output)
        else: 
            current_code = correct_befunge_code(prev_code, desired_output, actual_output)
    
    else :
        output_code = prev_code
        current_code = generate_befunge_code(desired_output, prev_code)
        print("Generated Befunge Code:")
        print(current_code)
        if abs(previous_character_count - current_character_count) < threshold:
            print("Stopping criteria met. Final Befunge code:")
            print(current_code)
            break

    # Check stopping condition

    # Update for the next iteration
    previous_character_count = current_character_count
    prev_code = current_code

print("The final Befunge code to get your desired output is : " + output_code)