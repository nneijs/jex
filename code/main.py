def detect_language(file_name):
    if file_name.endswith(".py"):
        return "Python"
    elif file_name.endswith(".java"):
        return "Java"
    elif file_name.endswith(".js"):
        return "JavaScript"
    elif file_name.endswith(".cpp") or file_name.endswith(".h"):
        return "C++"
    elif file_name.endswith(".html"):
        return "HTML"
    elif file_name.endswith(".css"):
        return "CSS"
    else:
        return "Unknown"

# Example usage:
file_name = "example.py"
programming_language = detect_language(file_name)
print(f"The programming language for {file_name} is {programming_language}.")
