from utils import generate_befunge_code, generate_first_befunge_code, run_befunge_code, correct_befunge_code


desired_output = input("What is your desired output? ")

iteration = 0
threshold = 5

prev_code = generate_first_befunge_code(desired_output)
previous_character_count = len(prev_code)


while True:
    iteration += 1
    print(f"\nIteration {iteration}:")

    # Generate Befunge code
    current_code = generate_befunge_code(desired_output, prev_code)
    print("Generated Befunge Code:")
    print(current_code)

    # Count characters in the Befunge code
    current_character_count = len(current_code)
    print(f"Character Count: {current_character_count}")

    # Run the Befunge code and verify the output
    actual_output = run_befunge_code(current_code)
    print(f"Actual Output: {actual_output}")

    if actual_output != desired_output:
        print("Output does not match the desired output.")
        current_code = correct_befunge_code(current_code, desired_output, actual_output)
        continue

    # Check stopping condition
    if abs(previous_character_count - current_character_count) < threshold:
        print("Stopping criteria met. Final Befunge code:")
        print(current_code)
        break

    # Update for the next iteration
    previous_character_count = current_character_count
    prev_code = current_code