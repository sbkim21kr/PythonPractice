### Here is the step-by-step workflow:

## 1. Clone the Repository 📥

First, get your project onto your Windows machine. You can use GitHub Desktop or the Git command line.
Bash

If using the command line
# git clone https://github.com/your-username/your-repo-name.git

## 2. Create and Activate venv 💻

Navigate into your project folder in the Windows terminal and set up your new virtual environment.
Bash

Navigate into your project folder
# cd your-repo-name

Create a new virtual environment
# python -m venv venv

Activate the virtual environment (command is different on Windows)
# .\venv\Scripts\activate

## 3. Install Packages with requirements.txt 📦

With your virtual environment activated, use the pip install command to read the requirements.txt file and install all the listed packages automatically.
Bash

# pip install -r requirements.txt

This single command will install opencv-python, matplotlib, numpy, and any other packages you added to the file. This is the main reason why requirements.txt is a best practice for managing project dependencies.