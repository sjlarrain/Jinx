import subprocess
import sys

# Install required Python libraries
libraries = ["pandas", "sqlite3", "dash", "streamlit", "jupyter"]

for lib in libraries:
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

print("All required libraries have been installed.")
