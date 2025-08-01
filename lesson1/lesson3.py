#1. Functions WHY & HOW
# Functions let you wrap up code logic that you want to reuse, test, or modularize.

def greet(name):
    print(f"Hello, {name}!")

greet("Cosmo")


#Functions with Defaults & Keyword arguments
def log_message(message, level = "INFO"):
    print(f"[{level}] {message}")

log_message("ETL Started")
log_message("Disk almost full", level="WARNING")

#2. Writin Functions That Process Data

def errors_count(path):
    error_count = 0
    with open(path, "r") as f:
        for line in f:
            if "ERROR" in line.lower():
                error_count += 1
    return error_count

#3. Error Handling with Try / except
# Basic Pattern:

try:
    with open("data.csv", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("The file not found.")


# Catching multiple errors
try:
    result = 10/0
except ZeroDivisionError:
    print("Oops! Division by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")

