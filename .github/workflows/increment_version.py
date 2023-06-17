name: Python Shell Script

on:
  push:
    branches:
      - main  # Replace with the branch you want to trigger the action on
  pull_request:
    branches:
      - main  # Replace with the branch you want to trigger the action on

jobs:
  build:
    runs-on: ubuntu-latest  # Choose the desired operating system
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x  # Replace with the desired Python version

    - name: Execute Python Shell Script
      run: python path/to/your/script.py  # Replace with the path to your Python shell script
