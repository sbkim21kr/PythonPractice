# 🐍 Python Project + GitHub Workflow Cheat Sheet

## 1️⃣ Project Setup & Git Initialization

```bash
# Create a new project folder and navigate into it
mkdir my_first_project
cd my_first_project

# Initialize a new Git repository
git init
```

---

## 2️⃣ Configure Git to Use `main` Branch

```bash
# Set 'main' as the default branch for all future projects (one-time setup)
git config --global init.defaultBranch main

# If your current branch is 'master', rename it to 'main'
git branch -M main
```

---

## 3️⃣ Create & Activate Virtual Environment

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

> ✅ Look for `(venv)` at the start of your prompt to confirm activation.

---

## 4️⃣ Install `ipykernel` (For Jupyter Notebooks)

```bash
pip install ipykernel
```

---

## 5️⃣ Create Code & First Commit

```bash
# Stage all files for commit
git add .

# Commit your changes with a message
git commit -m "Initial commit of project files"
```

---

## 6️⃣ Link to GitHub & Push

1. Create an **empty repository on GitHub** (no README).
2. Copy its URL.
3. Link local repo and push:

```bash
git remote add origin https://github.com/your_username/your_repo_name.git
git push -u origin main
```

---

## 7️⃣ Daily Workflow After Changes

```bash
# Stage changes
git add .

# Commit with a message
git commit -m "Describe your changes"

# Push to GitHub
git push
```

---

## 🧰 Extra Tips

* Use `.gitignore` to exclude venv and temporary files:

```
venv/
__pycache__/
*.py[cod]
.DS_Store
Thumbs.db
.vscode/
.idea/
```

* In VS Code: `Ctrl+Shift+P → Python: Select Interpreter → choose local venv`
