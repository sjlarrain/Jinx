#!/bin/bash

# Detect the operating system
OS="$(uname -s)"

case "$OS" in
    Linux*)
        echo "Detected Linux environment"
        # Update package list and install pip
        sudo apt-get update
        sudo apt-get install -y python3-pip
        ;;
    MINGW*|MSYS*|CYGWIN*)
        echo "Detected Windows environment"
        # Install pip for Windows
        python -m ensurepip --upgrade
        ;;
    *)
        echo "Unsupported OS: $OS"
        exit 1
        ;;
esac

# Install required Python libraries
pip3 install pandas sqlite3 dash streamlit jupyter

echo "All required libraries have been installed."
