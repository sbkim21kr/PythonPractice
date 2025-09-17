### 1. Project Setup and Git Initialization

First, create your project directory and initialize it as a Git repository. This is the foundation of your entire workflow.
Bash

# Create a new project folder and navigate into it
mkdir my_first_project
cd my_first_project

# Initialize a new Git repository
git init

### 2. Configure Git for the main Branch

Git's default branch name is sometimes master. To align with modern standards like GitHub's, you should configure Git to use main as the default branch for all future projects. This is a one-time setup on your machine.
Bash

# Set the default branch name to 'main' for all future projects
git config --global init.defaultBranch main

If you've already run git init and the branch is named master, you can rename it right away.
Bash

# If your branch is currently 'master', rename it to 'main'
git branch -M main

### 3. Create a Virtual Environment (venv)

Creating a virtual environment is a crucial step to isolate your project's dependencies from your system's Python installation. This prevents conflicts and makes your project portable.
Bash

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

You'll know it's active when you see (venv) at the beginning of your command prompt.

### 4. Install ipykernel

If you plan on using Jupyter Notebooks (.ipynb files), you must install ipykernel into your virtual environment.
Bash

# Install ipykernel into the active virtual environment
pip install ipykernel

This is the correct way to ensure your Jupyter Notebooks run using your isolated environment's packages.

### 5. Create Your Code and First Commit

Now you can start coding. After creating your initial files (e.g., main.py or a notebook), you'll add and commit them to your local Git repository.

    Open your project in VS Code and create your files.

    In the terminal, stage your files to prepare them for the commit.
    Bash

git add .

Create your first commit.
Bash

    git commit -m "Initial commit of project files"

### 6. Link to GitHub and Push

Finally, you will connect your local repository to a remote one on GitHub.

    Create a new, empty repository on GitHub (do not check the box to add a README.md file).

    Copy the URL of the repository.

    Link your local repository to the GitHub one.
    Bash

git remote add origin https://github.com/your_username/your_repo_name.git

Push your code to GitHub for the first time.
Bash

    git push -u origin main

From now on, your workflow will be the simple git add ., git commit, and git push sequence.