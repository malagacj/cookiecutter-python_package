import os
import subprocess

# Read the Python version from the template
python_version = "{{ cookiecutter.python_version }}"

# Check if pyenv is installed and set the correct Python version
#if subprocess.run(["command", "-v", "pyenv"], capture_output=True, text=True).stdout.strip():
#    subprocess.run(["pyenv", "local", python_version], check=True)

# Initialize Git if not already done
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)

# Create uv virtual environment
subprocess.run(["uv", "venv"], check=True)

# Install dependencies if pyproject.toml exists
#if os.path.exists("pyproject.toml"):
#    subprocess.run(["uv", "pip", "install", "."], check=True)

print(f"✅ Git, Python {python_version} (via pyenv), and uv virtual environment initialized!")
