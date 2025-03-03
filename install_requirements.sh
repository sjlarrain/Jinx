#!/bin/bash

# Update package list and install pip
sudo apt-get update
sudo apt-get install -y python3-pip

# Install required Python libraries
pip3 install pandas sqlite3 dash streamlit jupyter

echo "All required libraries have been installed."
