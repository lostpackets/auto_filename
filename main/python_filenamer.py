import ast
import os

# Read the code file
with open("code.py", "r") as f:
    code = f.read()

# Parse the code into an AST
root = ast.parse(code)

# Extract the function names
functions = [node.name for node in ast.walk(root) if isinstance(node, ast.FunctionDef)]

# Get the first function name
title = functions[0]

# Change the file name
os.rename("code.py", f"{title}.py")
