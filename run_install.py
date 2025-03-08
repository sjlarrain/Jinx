import subprocess
import os
import platform
import sys

# Get the full path to the install_requirements.sh script
script_path_unix = os.path.join(os.path.dirname(__file__), 'install_requirements.sh')
script_path_windows = os.path.join(os.path.dirname(__file__), 'install_requirements_windows.py')

# Print the path of the script being executed
if platform.system() == "Windows":
    print(f"Executing script at: {script_path_windows}")
    subprocess.run([sys.executable, script_path_windows], shell=True)
else:
    print(f"Executing script at: {script_path_unix}")
    subprocess.run(["/bin/bash", script_path_unix], shell=True)
