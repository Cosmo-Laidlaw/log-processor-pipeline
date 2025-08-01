from unittest import result


def square(num):
    result = int(num) * int(num)
    return result

def format_log(msg, level="INFO"):
    return f"[{level}] {msg}"


def read_lines_clean(path):
    try:
        with open(path, "r") as f:
             for line in path:
                  return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def divide(a, b):
    try:
        result = int(a) / int(b)
        return result
    except ZeroDivisionError:
        return "Error: Cannot Divide by Zero"


def get_file_summary(path):
    count = 0
    try:
        with open(path, "r") as f:
            for line in f:
                count += 1
        return count
    except FileNotFoundError:
        return f"File {path} not found"
