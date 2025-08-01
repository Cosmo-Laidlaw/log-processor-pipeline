# Log Processor
import json
import os


#---- Step 1: Read lines from the log file -----
def read_log_file(path):
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


#---- Step 2: Count SUCCESS and ERROR lines -----
def count_key_words(lines):
    error_count = 0
    success_count = 0
    for line in lines:
        if "success" in line.lower():
            success_count += 1
        if "error" in line.lower():
            error_count += 1
    
    summary = {"success_count" : success_count,
               "error_count": error_count
               }
    return summary


#----- Step 3: Extract only error lines -----
def extract_errors(lines):
    errors = []
    for line in lines:
        if "error" in line.lower():
            errors.append(line)
    return errors


#----- Step 4: Write Summary JSON -----
def write_summary(data, path):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent = 2)
    except Exception as e:
        print(f"Failed to write summary: {e}")


#----- Step 5: Write errors only file -----
def write_error(lines, path):
    try:
        with open(path, "w") as file:
            for line in lines:
                if "error" in line.lower():
                    file.write(line + "\n")
    except Exception as e:
        return f"Unable to write errors:{e}"


#---- Step 6: Bring it all together -----
def main():
    input_path = "logs/sample_log.txt"
    summary_path = "output/summary.json"
    errors_path = "output/errors_only.txt"

    os.makedirs("output", exist_ok=True)

    lines = read_log_file(input_path)
    if not lines:
        print(f"Lines not found in {input_path}. Exiting!")
        return
    
    summary = count_key_words(lines)
    error_lines = extract_errors(lines)

    write_summary(summary, summary_path)
    write_error(error_lines, errors_path)

    print("Log processing complete.")
    print(f"Summary: {summary}")
    print(f"Saved errors to: {errors_path}")

        
#------Run Main------
if __name__ == "__main__":
    main()
