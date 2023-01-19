import subprocess
import os

# Get the file path
file_path = "code.cpp"

# Use libclang to extract function names
output = subprocess.check_output(["clang", "-Xclang", "-ast-dump", "-fsyntax-only", file_path])
output = output.decode("utf-8")

# Extract the function names
function_names = []
for line in output.split("\n"):
    if "FunctionDecl" in line and "<anonymous>" not in line:
        function_names.append(line.split()[-1])

# Get the first function name
title = function_names[0]

# Change the file name
os.rename(file_path, f"{title}.cpp")
